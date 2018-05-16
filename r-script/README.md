# CCISS.R

CCISS.R is a reworked Rscript for calculating Climate Change Informed Species Selection. It runs as a service listening on a zeromq messaging port.

## How it works

CCISS.R is initialized by a simple "broker" in the frontend, which listens for clients (ZMQ "REQ" clients) on port `5555`, and relays messages to a number of CCISS.R scripts specified by the number of "threads".  CCISS.R now expects JSON data. You can see an example client (with example data payload) in `./example-client/client-example.py`.

## Prerequisites

The way this script works, is it sets up a "broker" (basic python script) which is a frontend for receiving workloads on a queue, and it will pass it off to however many CCISS.R scripts you have running in the backend. You should install the requirements for the broker with the following command:

```sh
pip3 install -r requirements.txt
```

Once you have the requirements for the broker installed, make sure you have all the libs for CCISS.R installed:

```sh
R CMD INSTALL lib/randomForest_4.6-12.tar.gz lib/iterators_1.0.8.tar.gz \
    lib/doBy_4.5-15.tar.gz lib/foreach_1.4.3.tar.gz lib/data.table_1.10.4.tar.gz \
    lib/Rcpp_0.12.16.tar.gz lib/plyr_1.8.4.tar.gz lib/reshape_0.8.6.tar.gz \
    lib/reshape2_1.4.2.tar.gz lib/doParallel_1.0.11.tar.gz lib/jsonlite_1.5.tar.gz \
    lib/proto_1.0.0.tar.gz lib/getopt_1.20.2.tar.gz lib/findpython_1.0.3.tar.gz \
    lib/argparse_1.1.1.tar.gz lib/rzmq_0.9.3.tar.gz
```

Or, you can optionally install each of the above libs using R. (through `install.packages`).

You can also run CCISS.R on its own like so:

```sh
Rscript CCISS.R -v -p 7433
```

This runs the CCISS.R script in "verbose" mode (`-v`) and listens as a ZeroMQ "request worker" on port `7433` (`-p 7433`).  Run the command without any flags and it will default to the non-verbose and port 7433.

## Running A CCISS.R Service

You can start a CCISS Service by simply calling the broker:

```sh
./broker/broker.py -t 4
```

This will start 4 instances of the CCISS.R script and start listening on port 5555 for zeromq `REQ` clients. Run the example client to see it work:

```sh
./example-client/example-client.py
```
