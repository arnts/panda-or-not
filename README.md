# panda-or-not

A first attempt at a machine learning API, using a pre-calculated model trained using images from Google Image searches. 

The model is bears.pkl - an 87MB file.

The notebook big-bears.ipynb shows how the model is trained, using fastai.

panda.py is a tiny Starlette API server which simply accepts an image URL and runs it against the pre-calculated model.

![](https://media.pri.org/s3fs-public/styles/story_main/public/images/2019/11/2019-11-19-beibeipanda.jpg?itok=xex8MzPS)

## Local Setup  

To test this API locally (on a Mac), you can follow these steps.

#### Install requirements
Ensure Python 3 (includes pip3) and virtualenv are installed

```bash
$ brew install python3
```

```bash
$ pip3 install virtualenv
```

#### Pull down the project

Clone the GitHub repository

#### Setup the virtual env (fancy new command prompt)
Create a virtual environment inside the project’s root directory

```bash
$ cd panda-or-not
```

```bash
$ python3 -m venv venv/
```

Install the project’s dependencies inside an active virtual environment
```bash
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

#### Run server 

Start the server from command line

```bash
(venv)$ uvicorn panda:app
```

#### Test endpoint 

Run from command line (in another window)

```bash
$ curl http://127.0.0.1:8000/classify-url?url=https%3A%2F%2Fmedia.pri.org%2Fs3fs-public%2Fstyles%2Fstory_main%2Fpublic%2Fimages%2F2019%2F11%2F2019-11-19-beibeipanda.jpg | python -m json.tool
```

The output should be something like this:

```json
{
    "predictions": [
        [
            "panda_bear",
            0.9997597336769104
        ],
        [
            "brown_bear",
            0.00010128997382707894
        ],
        [
            "black_bear",
            9.877605771180242e-05
        ],
        [
            "polar_bear",
            4.0194041503127664e-05
        ]
    ]
}
```

#### Deactivate (old familiar command prompt)

Stop server, and deactivate the virtualenv:
```bash
(venv)$ deactivate
```
