from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agent import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def root():
    return {"message": "AI Resume Agent backend running 🚀"}


@app.post("/analyze_resume")
async def analyze_resume(data: ResumeRequest):
    result = agent.run_sync(
        f"""
        Resume:
        {data.resume_text}

        Job Description:
        {data.job_description}
        """
    )
    return result.data
