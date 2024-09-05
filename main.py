from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    cluster_info = {
        "pod_name": os.getenv("POD_NAME", "N/A"),
        "pod_namespace": os.getenv("POD_NAMESPACE", "N/A"),
        "pod_ip": os.getenv("POD_IP", "N/A"),
        "node_name": os.getenv("NODE_NAME", "N/A"),
    }
    return templates.TemplateResponse("index.html", {"request": request, "cluster_info": cluster_info})