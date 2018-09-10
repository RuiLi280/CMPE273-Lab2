from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc

import sys


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        response = stub.Add(
            calculator_pb2.AddRequest(a=num1, b=num2))
    print("Sum: %d" % response.sum)


if __name__ == '__main__':
    run()
