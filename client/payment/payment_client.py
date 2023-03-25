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
import payment_pb2
import payment_pb2_grpc

import random
import time

    
def purchase(email_param, game_name_param, price_param,):
    with grpc.insecure_channel('purchase_server:50054') as channel:
        stub = payment_pb2_grpc.PaymentStub(channel)
        response = stub.Purchase(payment_pb2.GetDetailsRequest(email=email_param, game_name=game_name_param, price=price_param))
        return response


def run():
    purchase_result = purchase("l.carroll-oneill@mycit.ie", "Counter-Strike: Global Offensive", 14.99)
    print("purchase(): " + purchase_result.sucess + purchase_result.message)
    


if __name__ == '__main__':
    logging.basicConfig()
    run()
