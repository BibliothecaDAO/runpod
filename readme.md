# setup

Download the cached huggingface model

`$ python scripts/download_weights.py` (do it in some torch env)

install cog:

```console
$ sudo curl -o /usr/local/bin/cog -L "https://github.com/replicate/cog/releases/latest/download/cog_$(uname -s)_$(uname -m)"
$ sudo chmod +x /usr/local/bin/cog
```

Then run 

`$ cog build -t realms_adventurers_v1`

Tag it

`$ docker tag realms_adventurers_v1 aventau/realms_adventurers_v1:tagname`

Create a repo on docker hub with the name `aventau/realms_adventurers_v1`.

Then run

`$ docker push aventau/realms_adventurers_v1:tagname`

Then go to runpod:

Create template -> add `python runpod_infer.py` to the exec window
And add your s3 bucket variables to the environment variables.

you need [this](https://github.com/runpod/runpod-python/blob/7461d9ec6dc8ff15e45143ae071262d0bc59fb9b/runpod/serverless/utils/rp_upload.py#L24) to work

```python
BUCKET_ENDPOINT_URL
BUCKET_ACCESS_KEY_ID
BUCKET_SECRET_ACCESS_KEY
```

Then setup the api via the GUI

# Test

fill in `.env`

`$ pipenv install`

`$ pipenv shell && python test_endpoint.py`
