# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import user_pb2
import user_pb2_grpc

import random
import time


def register_user(email_param, firstname_param, lastname_param, password_param):
    with grpc.insecure_channel('user_server:50051') as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = stub.Register(user_pb2.RegisterRequest(email=email_param, firstname=firstname_param, lastname=lastname_param, password=password_param))
        return response


def get_user_details(email_param):
    with grpc.insecure_channel('user_server:50051') as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = stub.GetDetails(user_pb2.GetDetailsRequest(email=email_param))
        return response


def run():
    register = register_user("l.carroll-oneill@mycit.ie", "Lochlann", "Oneill", "password123")
    print("register_user(): " + register.email)
    
    details = get_user_details(register.email)
    print("get_user_details(" + register.email + "): " + details.firstname + ", " + details.lastname)


if __name__ == '__main__':
    logging.basicConfig()
    run()
