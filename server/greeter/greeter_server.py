from concurrent import futures
import datetime
import logging

import grpc
import redis
import pika

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        response = helloworld_pb2.HelloReply(message=f'Hello, {request.name}!')
        
        # RabbitMQ
        # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
        # channel = connection.channel()
        # channel.queue_declare(queue='user_getdetails')
        # def callback(ch, method, properties, body):
        #     email, firstname, lastname, password = body.decode().split(',')
        #     logging.info(f'Received user details: {email}, {firstname}, {lastname}, {password}')
        # channel.basic_consume(queue='user_getdetails', on_message_callback=callback, auto_ack=True)

        # logging.info('Waiting for user details...')
        # channel.start_consuming()
        
        
        # Weblog
        try:
            conn = redis.StrictRedis(host='redis', port=6379)
            conn.set("log.greeter_server." + str(datetime.datetime.now()), "Greeter.SayHello: Hello, " + request.name + "!")
        except Exception as ex:
            print('Error:', ex)
        
        return response


    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message=f'Hello again, {request.name}!')


def serve(port='50052'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'Server started, listening on port {port}')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
