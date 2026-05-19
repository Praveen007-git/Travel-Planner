from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from groq import Groq
import os

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>AI Travel Planner</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 50px;
            }
            input, button {
                padding: 10px;
                margin: 10px;
                width: 250px;
                border-radius: 8px;
                border: none;
            }
            button {
                background: #38bdf8;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <h1>🌍 AI Travel Planner</h1>

        <form action="/plan" method="post">

            <input name="location" placeholder="Location"><br>
            <input name="days" placeholder="Days"><br>
            <input name="budget" placeholder="Budget"><br>

            <button type="submit">Generate Plan</button>

        </form>

    </body>
    </html>
    """

@app.post("/plan", response_class=HTMLResponse)
async def plan_trip(
    budget: str = Form(...),
    days: str = Form(...),
    location: str = Form(...)
):

    prompt = f"""
    Create a beautiful travel itinerary.

    Budget: {budget}
    Days: {days}
    Location: {location}

    Include:
    - Day wise itinerary
    - Hotel suggestions
    - Tourist places
    - Food suggestions
    - Approx expenses
    """

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    result = chat_completion.choices[0].message.content

    return f"""
    <html>
    <body style="background:#0f172a;color:white;padding:40px;font-family:Arial">

        <h1>🌍 Your Travel Plan</h1>

        <pre style="white-space:pre-wrap;background:#1e293b;padding:20px;border-radius:10px">
{result}
        </pre>

        <a href="/" style="color:#38bdf8">⬅ Back</a>

    </body>
    </html>
    """