# Running in Docker

## Add a CCISS Rdata model

For example:

```sh
cp <dir>/Model ./r-script/data/BGCv10_2000Pt_Rnd_Normal_1961_1990MSY_RFmodelKiriFinal
```

If you want to change the name of the model or change the model, make sure you modify `r-script/CCISS.R` first. Future scripts should allow the system to specify which model to load.

## Build it

```sh
docker build -t cciss -f tree-s9y-cciss.Dockerfile .
```

## Run it, exposing the client port

```sh
docker run -p 5555:5555 cciss
```

after the above steps, you should be able to communicate with the CCISS.R client by sending it a JSON object over zmq. See `r-script/example-client/example-client.py`
