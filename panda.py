from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route
from fastai.vision import (
    open_image,
    load_learner,
)
from io import BytesIO
import sys
import uvicorn
import aiohttp
import asyncio
import socket

async def get_bytes(url):
    # fix to network unreachable from local mac https://github.com/aio-libs/aiohttp/issues/2522    
    conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    )
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            return await response.read()

app = Starlette()

bear_learner = load_learner('.', "bears.pkl")

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

if __name__ == "__main__":
    if "serve" in sys.argv:
        uvicorn.run(app, host="0.0.0.0", port=8008)