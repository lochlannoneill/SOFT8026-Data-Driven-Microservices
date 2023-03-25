from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

import random
import time


def sayHello():
    with grpc.insecure_channel('greeter_server:50052') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.SayHello(helloworld_pb2.HelloRequest(name='Lochlann'))
        print("stub.SayHello(): " + response.message)

        response_again = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='Lochlann'))
        print("stub.SayHelloAgain(): " + response_again.message)


def run():
    sayHello()


if __name__ == '__main__':
    logging.basicConfig()
    run()