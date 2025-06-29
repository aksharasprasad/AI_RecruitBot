# recruitbot.py

def read_resume(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def mock_granite_response(resume_text, job_title):
    # Simulating IBM Granite response (for demo purpose)
    return {
        "summary": "Candidate has strong skills in Python, SQL, and data visualization with 2 years at TCS.",
        "match_score": "87%",
        "recommendation": "Strong match for the Data Analyst role. Recommend to shortlist."
    }

def main():
    job_title = "Data Analyst"
    resume = read_resume("sample_resume.txt")
    
    print("\n🔍 Analyzing Resume for role:", job_title)
    print("\n📄 Resume Text:\n", resume)

    result = mock_granite_response(resume, job_title)
    
    print("\n✅ AI Summary:", result["summary"])
    print("📊 Match Score:", result["match_score"])
    print("📝 Recommendation:", result["recommendation"])

if __name__ == "__main__":
    main()
