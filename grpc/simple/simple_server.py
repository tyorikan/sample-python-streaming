import time
from concurrent import futures
import grpc
import simple_pb2
import simple_pb2_grpc


class SimpleServiceServicer(simple_pb2_grpc.SimpleServiceServicer):

    def __init__(self):
        pass

    def HelloServer(self, request_iterator, context):
        for new_msg in request_iterator:
            reply_msgs = []
            print('Receive new message! [name: {}, msg: {}]'.format(
                new_msg.name, new_msg.msg))
            reply_msgs.append(simple_pb2.ReplyMessage(
                reply_msg='{} {}'.format(new_msg.msg, new_msg.name)))
            reply_msgs.append(simple_pb2.ReplyMessage(
                reply_msg='Nice to meet you!!!'))
            for message in reply_msgs:
                yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_pb2_grpc.add_SimpleServiceServicer_to_server(
        SimpleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC simple server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
