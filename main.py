from fastapi import FastAPI

from ollama import Client
from fastapi.responses import HTMLResponse,StreamingResponse, JSONResponse, FileResponse
from fastapi.requests import Request
import markdown
import os
from prompts.feynman_filter import FEYNMAN_FILTER
from src.data.models.assistant_config import AssistantConfig
from src.data.models.user_query import UserQuery
from src.data.models.assistant_response import AssistantResponse

app = FastAPI()


assistant_config = AssistantConfig(model="llama3.2:1b",prompt=FEYNMAN_FILTER)
assistant_response = AssistantResponse()
user_query = UserQuery()
llm_client = Client()


@app.get("/models")
async def load_models():
    models = [model.model for model in llm_client.list().models]
    print(models)
    return JSONResponse({"models":models})

@app.post("/prompt")
async def process_prompt(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    assistant_config.set_prompt(prompt)
    return JSONResponse({"result": "Prompt is registered"})

@app.get("/assistant/{query}",response_class=FileResponse)
async def analyze(query:str):
    if query == user_query.get_query():
        return FileResponse(os.path.join("static", "index.html"))
        
    user_query.set_query(query=query)
    response = llm_client.chat(
        model=assistant_config.get_model(),
        messages=[
            {"role":"system","content":assistant_config.get_prompt()},
            {"role":"user","content":query}
        ],
        stream=False
        
    )
    md_response = markdown.markdown(response.message.content)
    assistant_response.set_response(md_response)
    return FileResponse(os.path.join("static", "index.html"))


@app.get("/response",response_class=JSONResponse)
async def get_response():
    return JSONResponse({"response":assistant_response.get_response()})
