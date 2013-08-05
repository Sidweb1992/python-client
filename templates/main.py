#!/usr/bin/env python

import sys
import time
import socket
import json
import ClientJSON
from AI import *
import argparse
import Utility
from Game import *


def main():
    parser = argparse.ArgumentParser(description="Python client for SIG-GAME framework.")
    parser.add_argument("-a", "--address", dest='conn_address', default="localhost",
                        help="The address of the game server.", type=str)
    parser.add_argument("-p", "--port", dest='conn_port', default="19000",
                        help="The port of the game server.", type=int)
    parser.add_argument("-n", "--name", dest='game_name', default=None,
                        help="The name of game to connect to on the server.")
    args = parser.parse_args()

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    game = Game(conn=connection, addr=args.conn_address, port=args.conn_port, name=args.game_name)
    game.run()

    print("CLIENT: Closing connection.")
    connection.close()

    return


########## RUN MAIN ##########
if __name__ == '__main__':
    main()
