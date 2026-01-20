from pydantic import BaseModel
from typing import List


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


class ResumeMatchResult(BaseModel):
    match_score: int
    missing_skills: List[str]
    ats_keywords: List[str]
    resume_improvements: List[str]
