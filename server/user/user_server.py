from concurrent import futures
import datetime
import logging

import grpc
import redis
from tinydb import TinyDB, Query
import pika

import user_pb2
import user_pb2_grpc

class User(user_pb2_grpc.UserServicer):
    
    def Register(self, request, context):
        db = TinyDB('users.json')

        user_data = {
            'email': request.email,
            'firstname': request.firstname,
            'lastname': request.lastname,
            'password': request.password
        }
        db.insert(user_data)
        
        # Weblog
        try:
            conn = redis.StrictRedis(host='redis', port=6379)
            conn.set("log.user_server." + str(datetime.datetime.now()), "User.Register: " + request.email + "")
        except Exception as ex:
            print('Error:', ex)
        
        return user_pb2.RegisterRequest(email=request.email, firstname=request.firstname, lastname=request.lastname)
    

    def GetDetails(self, request, context):
        db = TinyDB('../db/users.json')
        User = Query()
        result = db.search(User.email == request.email)
        response = user_pb2.GetDetailsResponse(email=result[0]['email'], firstname=result[0]['firstname'], lastname=result[0]['lastname'])
        
        # RabbitMQ
        # conn_rabbitmq = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
        # channel = conn_rabbitmq.channel()
        # channel.queue_declare(queue='user_getdetails')
        # message = f',{request.firstname},{request.lastname}'
        # channel.basic_publish(exchange='', routing_key='user_getdetails', body=message)
        # conn_rabbitmq.close()
        
        # Weblog
        try:
            conn_log = redis.StrictRedis(host='redis', port=6379)
            conn_log.set("log.catalogue_server." + str(datetime.datetime.now()), "user.GetDetails: (" + response + ")")
        except Exception as ex:
            print('Error:', ex)
            
        return response


def serve(port = 50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'Server started, listening on port {port}')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
