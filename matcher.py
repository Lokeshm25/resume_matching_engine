from config import SKILL_ALIASES
from resume_dataset import RESUME_DATASET
from job_desc_dataset import JOB_DESCRIPTION_DATASET

def match_resume_to_job(resume, job):
    """
    Match a resume to a job description based on skills.
    
    Args:
        resume (dict): Resume dictionary with skills.
        job (dict): Job description dictionary with required and preferred skills.
    
    Returns:
        float: Match score between 0 and 1.
    """
    required_skills = job["required_skills"]
    preferred_skills = job["preferred_skills"]
    resume_skills = resume["skills"]
    
    # Normalize skills to their aliases
    normalized_required_skills = [SKILL_ALIASES.get(skill.lower(), skill.lower()) for skill in required_skills]
    normalized_preferred_skills = [SKILL_ALIASES.get(skill.lower(), skill.lower()) for skill in preferred_skills]
    normalized_resume_skills = [SKILL_ALIASES.get(skill.lower(), skill.lower()) for skill in resume_skills]
    
    # Calculate match score
    required_match = sum(1 for skill in normalized_required_skills if skill in normalized_resume_skills)
    preferred_match = sum(1 for skill in normalized_preferred_skills if skill in normalized_resume_skills)
    total_required = len(normalized_required_skills)
    total_preferred = len(normalized_preferred_skills)
    
    required_score = required_match / total_required if total_required > 0 else 0
    preferred_score = preferred_match / total_preferred if total_preferred > 0 else 0
    
    # Weight required skills more heavily than preferred skills
    match_score = (required_score * 0.7) + (preferred_score * 0.3)
    
    return match_score

def match_resumes_to_jobs(resumes, jobs):
    """
    Match a list of resumes to a list of job descriptions.
    
    Args:
        resumes (list): List of resume dictionaries.
        jobs (list): List of job description dictionaries.
    
    Returns:
        list: List of tuples containing the resume ID, job ID, and match score.
    """
    matches = []
    for resume in resumes:
        for job in jobs:
            match_score = match_resume_to_job(resume, job)
            matches.append((resume["id"], job["id"], match_score))
    
    return matches

# Example usage
matches = match_resumes_to_jobs(RESUME_DATASET, JOB_DESCRIPTION_DATASET)
for match in matches:
    print(f"Resume {match[0]} matches Job {match[1]} with score {match[2]:.2f}")