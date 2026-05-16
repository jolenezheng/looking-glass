from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import os

app = FastAPI(title="Looking Glass API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:5500").split(","),
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class WaitlistEntry(BaseModel):
    email: EmailStr


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/waitlist", status_code=201)
async def join_waitlist(entry: WaitlistEntry):
    """Add an email to the waitlist. Returns 409 if already registered."""
    # TODO: replace with Supabase insert
    # from supabase import create_client
    # supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])
    # result = supabase.table("waitlist").insert({"email": entry.email}).execute()
    raise HTTPException(status_code=501, detail="Supabase not yet wired up")
