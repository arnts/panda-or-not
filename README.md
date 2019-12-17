# panda-or-not

A first attempt at a machine learning API based on fastai, using a pre-calculated model trained using images from Google Images searches. 

The model is bears.pkl - an 87MB file.

The notebook big-bears.ipynb shows the model is trained, using fastai.

panda.py is a very tiny Starlette API server which simply accepts a file image URL and runs it against the pre-calculated model.

## Install and run

Ensure all required modules installed

- pip3 install torch torchvision
- pip3 install fastai
- pip3 install starlette
- pip3 install aiohttp
- pip3 install uvicorn

### Run server 

Start from command line

```python
> uvicorn example:app
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
