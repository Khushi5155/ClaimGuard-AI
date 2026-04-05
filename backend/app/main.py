from fastapi import FastAPI
from app.routes import analyze
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ClaimGuard AI",
    description="Offline Claim-Based Fake News Verification System",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(analyze.router)

@app.get("/")
def root():
    return {"message": "ClaimGuard AI Backend Running 🚀"}
