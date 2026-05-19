from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Travel Planner Running"}

@app.get("/plan")
def plan(location: str, days: int, budget: int):
    return {
        "location": location,
        "days": days,
        "budget": budget,
        "itinerary": [
            f"Day 1: Explore {location}",
            f"Day 2: Local sightseeing in {location}",
            f"Day 3: Adventure + food tour",
            "Day 4: Shopping + relaxation",
            "Day 5: Return plan"
        ]
    }