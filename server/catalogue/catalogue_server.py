from concurrent import futures
import datetime
import logging

import grpc
import redis
from tinydb import TinyDB, Query

import catalogue_pb2
import catalogue_pb2_grpc

class Catalogue(catalogue_pb2_grpc.CatalogueServicer):

    def GetGames(self, request, context):
        db = TinyDB('games.json')
        result = db.all()
        print('result" ' + str(result))
        
        response = catalogue_pb2.GetGamesResponse(games=result)
        print('response: ' + str(response))
        
        # Weblog
        try:
            conn = redis.StrictRedis(host='redis', port=6379)
            conn.set("log.catalogue-server." + str(datetime.datetime.now()), "Catalogue.GetGames: " + str(len(response.games)) + " games")
        except Exception as ex:
            print('Error:', ex)
        
        return response


def serve(port='50053'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    catalogue_pb2_grpc.add_CatalogueServicer_to_server(Catalogue(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'Server started, listening on port {port}')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()