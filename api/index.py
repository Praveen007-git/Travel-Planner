from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from groq import Groq

import os
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "AI Travel Planner is live"}



@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <body>

    <h1>AI Travel Planner 🌍</h1>

    <form action="/plan" method="post">

        <label>Budget:</label><br>
        <input type="text" name="budget"><br><br>

        <label>Days:</label><br>
        <input type="text" name="days"><br><br>

        <label>Location:</label><br>
        <input type="text" name="location"><br><br>

        <button type="submit">Generate Trip</button>

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
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    result = chat_completion.choices[0].message.content

    html_content = f"""
    <html>

    <head>

        <title>AI Travel Planner</title>

        <style>

            body {{
                font-family: Arial;
                background: #0f172a;
                color: white;
                padding: 40px;
            }}

            .card {{
                background: #1e293b;
                padding: 30px;
                border-radius: 20px;
                max-width: 900px;
                margin: auto;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: #38bdf8;
                text-align: center;
            }}

            pre {{
                white-space: pre-wrap;
                font-size: 16px;
                line-height: 1.8;
            }}

            .btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 12px 20px;
                background: #38bdf8;
                color: black;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>🌍 AI Travel Plan</h1>

            <pre>{result}</pre>

            <a href="/" class="btn">Plan Another Trip</a>

        </div>

    </body>

    </html>
    """

    return html_content