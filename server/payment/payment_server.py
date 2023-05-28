from concurrent import futures
import datetime
import logging

import grpc
import redis
from tinydb import TinyDB, Query

import payment_pb2
import payment_pb2_grpc

class Payment(payment_pb2_grpc.UserServicer):
    
    def Purchase(self, request, context):
        db = TinyDB('users.json')
        User = Query()
        
        # Weblog
        try:
            conn = redis.StrictRedis(host='redis', port=6379)
            conn.set("log.payment-server." + str(datetime.datetime.now()), "Payment.Purchase: ")
        except Exception as ex:
            print('Error:', ex)
        
        return payment_pb2.RegisterRequest(email=request.email, game_name=request.price, price=request.price)
    

def serve(port = 50054):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServicer_to_server(Payment(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'Server started, listening on port {port}')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
