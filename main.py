from matcher import match_resumes_to_jobs
from ranker import rank_resumes_for_all_jobs
from resume_dataset import RESUME_DATASET
from job_desc_dataset import JOB_DESCRIPTION_DATASET

def main():
    matches = match_resumes_to_jobs(RESUME_DATASET, JOB_DESCRIPTION_DATASET)
    ranked_matches = rank_resumes_for_all_jobs(matches)
    for job_id, matches in ranked_matches.items():
        print(f"Job {job_id}:")
        for match in matches[:3]:  # Print top 3 matches
            print(f"  Resume {match[0]}: {match[2]:.2f}")
        print()

if __name__ == "__main__":
    main()