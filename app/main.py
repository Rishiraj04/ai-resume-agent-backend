from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
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
