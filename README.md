# Resume Data Extraction

## Project Setup and Installation

To set up and install the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd Resume_Data_Extractor
   ```

3. Install dependencies using the `uv` command:
   ```bash
   uv venv && uv sync
   ```

   If the `uv` command is unavailable, use the following PowerShell-friendly fallback:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application

To run the application in development mode, use the following command:
```powershell
python -m uvicorn app.main:app --reload
```

By default, the application will run on `http://127.0.0.1:8000`.

## API Documentation

Swagger API documentation is available at the following endpoint:
/docs
Access it locally by navigating to `http://127.0.0.1:8000/docs` in your browser.
