# panda-or-not

A first attempt at a machine learning API, using a pre-calculated model trained using images from Google Images searches. 

The model is bears.pkl - an 87MB file.

The notebook big-bears.ipynb shows how the model is trained, using fastai.

panda.py is a very tiny Starlette API server which simply accepts a file image URL and runs it against the pre-calculated model.

## Install 

#### Requirements
Install Python 3 (includes pip3) and virtualenv

```bash
$ brew install python3
```

```bash
$ pip3 install virtualenv
```

#### Virtual env
Create and activate a virtualenv:
```bash
$ virtualenv -p python3 <desired-path>
```
```bash
$ source <desired-path>/bin/activate
```

#### Install dependencies 

Ensure all required dependencies are available

```bash
$ pip install torch torchvision
$ pip install fastai
$ pip install starlette
$ pip install aiohttp
$ pip install uvicorn
```

#### Run server 

Start from command line

```bash
$ uvicorn panda:app
```

#### Test 

```bash
$ curl http://127.0.0.1:8000/classify-url?url=https%3A%2F%2Fmedia.pri.org%2Fs3fs-public%2Fstyles%2Fstory_main%2Fpublic%2Fimages%2F2019%2F11%2F2019-11-19-beibeipanda.jpg
```

#### Deactivate

Deactivate the virtualenv:
```bash
$ deactivate
```

## Example

Input image: https://media.pri.org/s3fs-public/styles/story_main/public/images/2019/11/2019-11-19-beibeipanda.jpg?itok=xex8MzPS

![](https://media.pri.org/s3fs-public/styles/story_main/public/images/2019/11/2019-11-19-beibeipanda.jpg?itok=xex8MzPS)

### Result

JSON response:
```json
{
  "predictions": [
    ["panda_bear", 0.9997597336769104],
    ["brown_bear", 0.00010128997382707894],
    ["black_bear", 0.00009877605771180242],
    ["polar_bear", 0.000040194041503127664]
  ]
}
```
