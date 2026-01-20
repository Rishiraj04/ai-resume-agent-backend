from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import agent
from app.models import ResumeRequest

app = FastAPI(title="AI Resume Match Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze_resume(data: ResumeRequest):
    prompt = f"""
Resume:
{data.resume_text}

Job Description:
{data.job_description}
"""
    result = await agent.run(prompt)
    return result.data
