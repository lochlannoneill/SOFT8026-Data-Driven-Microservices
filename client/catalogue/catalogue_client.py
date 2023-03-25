from __future__ import print_function

import logging

import grpc
import catalogue_pb2
import catalogue_pb2_grpc

import random
import time


def get_games():
    with grpc.insecure_channel('catalogue_server:50053') as channel:
        stub = catalogue_pb2_grpc.CatalogueStub(channel)
        response = stub.GetGames(catalogue_pb2.GetGamesRequest())
        return response


def run():
    games = get_games()
    print("get_games(): " + str(games))


if __name__ == '__main__':
    logging.basicConfig()
    run()
