from matcher import match_resumes_to_jobs
from resume_dataset import RESUME_DATASET
from job_desc_dataset import JOB_DESCRIPTION_DATASET

def rank_resumes_for_job(job_id, matches):
    """
    Rank resumes for a specific job based on match scores.
    
    Args:
        job_id (int): ID of the job to rank resumes for.
        matches (list): List of tuples containing the resume ID, job ID, and match score.
    
    Returns:
        list: List of tuples containing the resume ID and match score, sorted in descending order of match score.
    """
    job_matches = [match for match in matches if match[1] == job_id]
    ranked_matches = sorted(job_matches, key=lambda x: x[2], reverse=True)
    
    return ranked_matches

def rank_resumes_for_all_jobs(matches):
    """
    Rank resumes for all jobs based on match scores.
    
    Args:
        matches (list): List of tuples containing the resume ID, job ID, and match score.
    
    Returns:
        dict: Dictionary with job IDs as keys and lists of tuples containing the resume ID and match score as values.
    """
    ranked_matches = {}
    for job in JOB_DESCRIPTION_DATASET:
        job_id = job["id"]
        ranked_matches[job_id] = rank_resumes_for_job(job_id, matches)
    
    return ranked_matches

# Example usage
matches = match_resumes_to_jobs(RESUME_DATASET, JOB_DESCRIPTION_DATASET)
ranked_matches = rank_resumes_for_all_jobs(matches)
for job_id, matches in ranked_matches.items():
    print(f"Job {job_id}:")
    for match in matches[:3]:  # Print top 3 matches
        print(f"  Resume {match[0]}: {match[2]:.2f}")
    print()