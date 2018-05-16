# Running in Docker

## Build it first

```sh
docker build -t cciss tree-s9y-cciss.Dockerfile
```

## Run it, exposing the client port

```sh
docker run -p 5555:5555 cciss
```

after the above steps, you should be able to communicate with the CCISS.R client by sending it a JSON object over zmq. See `r-script/example-client/example-client.py`
