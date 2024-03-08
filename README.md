# Traffic Devils test task

Simple web-service via FastAPI that accepts POST requests with JSON 
and sends messages to Telegram using the values from given JSON.

## Installation

Python 3 should be installed.

    https://github.com/Oomamchur/TD-test-task
    cd TD-test-task
    python -m venv venv

On Windows:

    source venv\Scripts\activate

On macOS or Linux:

    source venv/bin/activate

Install requirements:

    pip install -r requirements.txt

Run FastAPI

    python -m uvicorn main:app --reload

### Getting access

    http://127.0.0.1:8000/docs#/