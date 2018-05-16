FROM r-base
COPY r-script /usr/local/src/r-script
WORKDIR /usr/local/src/r-script
RUN apt-get update && apt-get install -y libpq-dev python3 python3-pip libzmq3-dev
RUN pip3 install pyzmq
ENV R_COMPILE_PKGS=1
RUN R CMD INSTALL lib/randomForest_4.6-12.tar.gz lib/iterators_1.0.8.tar.gz \
    lib/doBy_4.5-15.tar.gz lib/foreach_1.4.3.tar.gz lib/data.table_1.10.4.tar.gz \
    lib/Rcpp_0.12.16.tar.gz lib/plyr_1.8.4.tar.gz lib/reshape_0.8.6.tar.gz \
    lib/reshape2_1.4.2.tar.gz lib/doParallel_1.0.11.tar.gz lib/jsonlite_1.5.tar.gz \
    lib/proto_1.0.0.tar.gz lib/getopt_1.20.2.tar.gz lib/findpython_1.0.3.tar.gz \
    lib/argparse_1.1.1.tar.gz lib/rzmq_0.9.3.tar.gz
CMD [ "broker/broker.py", "-t 2" ]
