from pydantic_ai import Agent

agent = Agent(
    model="openrouter:meta-llama/llama-3.1-8b-instruct",
    system_prompt="""
You are an expert ATS resume evaluator.
Analyze the resume against the job description.
Return a JSON object with:
- match_score (number 0–100)
- missing_skills (list of strings)
- ats_keywords (list of strings)
- resume_improvements (list of strings)
Be strict and professional.
"""
)
