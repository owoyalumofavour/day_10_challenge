from fastapi import FastAPI

day_10app = FastAPI(title="My RESTful API", description="Day 10 Challenge", version="1.0.0")

@day_10app.get("/")
async def root():
    """Root endpoint – welcome message"""
    return {
        "message": "Welcome to my RESTful API!",
        "docs": "/docs",
        "available_endpoints": ["/", "/about", "/status"]
    }

@day_10app.get("/about")
async def about():
    """About endpoint – API information"""
    return {
        "name": "Day_10 Challenge API",
        "version": "Latest One",
        "author": "xoxo_firegirl_dmz",
        "description": "RESTful API built for #GDGoC30DayChallenge",
        "repository": "https://github.com/owoyalumofavour/day_10_challenge"
    }

@day_10app.get("/status")
async def status():
    """Health check endpoint"""
    return {
        "status": "Up and Ready!",
        "timestamp": "datetime.utcnow()" # You can use datetime.utcnow() for dynamic
    }