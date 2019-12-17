from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse
from starlette.routing import Route
from fastai.vision import (
    open_image,
    load_learner,
)
from pathlib import Path
from io import BytesIO
import sys
import uvicorn
import aiohttp
import asyncio

async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

app = Starlette()

bear_learner = load_learner('.', "bears.pkl")

@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)

@app.route("/classify-url", methods=["GET"])
async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)

def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    pred_class, pred_idx, losses = bear_learner.predict(img)
    return JSONResponse({
        "predictions": sorted(
            zip(bear_learner.data.classes, map(float, losses) ),
            key=lambda p: p[1],
            reverse=True
        )
    })

@app.route("/")
def form(request):
    return HTMLResponse(
        """
        Submit a URL:
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)

@app.route("/form")
def redirect_to_homepage(request):
    return RedirectResponse("/")

if __name__ == "__main__":
    if "serve" in sys.argv:
        uvicorn.run(app, host="0.0.0.0", port=8008)