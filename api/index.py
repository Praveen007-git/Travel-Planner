from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Travel Planner is live on Vercel"}

# 🔥 IMPORTANT FOR VERCEL
def handler(request):
    return app