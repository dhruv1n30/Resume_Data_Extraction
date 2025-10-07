# import requests

# # URL of your running FastAPI server
# BASE_URL = "http://127.0.0.1:8000/api/v1/genai"

# # Sample PDF file to test
# PDF_PATH = "sample_resume.pdf"

# def test_health_check():
#     url = f"{BASE_URL}/check"
#     response = requests.get(url)
#     print("Health Check:", response.status_code, response.json())

# def test_extract_resume():
#     url = f"{BASE_URL}/extract-resume"
#     with open(PDF_PATH, "rb") as f:
#         files = {"file": (PDF_PATH, f, "application/pdf")}
#         response = requests.post(url, files=files)

#     print("Extract Resume:", response.status_code)
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print("Error:", response.text)

# if __name__ == "__main__":
#     test_health_check()
#     test_extract_resume()
