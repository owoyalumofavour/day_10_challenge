# day_10_challenge
| Endpoint | Method | Description             | Example Response |
|----------|--------|-------------------------|------------------|
| '/'      | GET    | Root welcome message    | '{"message": "Welcome to my RESTful API!", "docs": "/docs"}' |
| '/about' | GET    | API metadata            | '{"name": "Day_10 Challenge API", "version": "Latest One", "author": "xoxo_firegirl_dmz"}' |
| '/status'| GET    | Health check            | '{"status": "Up and Ready!", "timestamp": "..."}' |

## How to Run

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies: `pip install fastapi uvicorn`
4. Run: `uvicorn day_10:day_10app --reload`
5. Open http://127.0.0.1:8000

## Built With
- FastAPI
- Python 3.9+
- vs code
