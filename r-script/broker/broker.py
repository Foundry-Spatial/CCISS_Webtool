#!/usr/bin/env python3

import time

import os
import sys
import json

import zmq
import argparse

from subprocess import Popen

def initWorker(workerId, wport = 7433):
    pidfile = 'cciss-worker-{}.pid'.format(workerId)
    # if not os.path.isfile(pidfile) :
        #start the worker and get the pid
        # Rscript CCISS.R <port>
    Popen(['Rscript', 'CCISS.R','-p {}'.format(wport)])
        #write the proc pid to file
    #subscribe to the zmq.REP port as a broker

parser = argparse.ArgumentParser()
# get the geoJson file from the cli params
parser.add_argument('-t', '--threads', default=2, type=int, help="Set the number of concurrent Rscripts \"threads\" that should be run at the same time.")
parser.add_argument('-p', '--port', default=5555, help="Default port to listen on for clients.")
parser.add_argument('-w', '--wport', default=7433, help="Default port to listen on for clients.")

cli_args = parser.parse_args()

#start Rscripts equal to the number of threads we've defined.
# are there PIDs for these processes? let's stop them and then start some more

def main():
    context = zmq.Context()

    print("Clients on: {}".format(cli_args.port))
    frontend = context.socket(zmq.ROUTER)
    frontend.bind("tcp://*:{}".format(cli_args.port))

    print("Workers on: {}".format(cli_args.wport))
    backend = context.socket(zmq.DEALER)
    backend.bind("tcp://*:{}".format(cli_args.wport))

    for i in range(0, cli_args.threads):
        #find the pid
        initWorker(i)

    zmq.proxy(frontend, backend)

    # We never get here...
    frontend.close()
    backend.close()
    context.term()


if __name__ == "__main__":
    main()
