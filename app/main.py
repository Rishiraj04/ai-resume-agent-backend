from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze_resume/")
async def analyze_resume(data: ResumeRequest):
    prompt = f"""
    Resume:
    {data.resume_text}

    Job Description:
    {data.job_description}
    """

    result = agent.run_sync(prompt)
    return result.data
