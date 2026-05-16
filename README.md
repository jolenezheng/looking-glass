# Looking Glass

A weekly mix exchange. Submit an hour-long mix, get matched with someone, swap feedback by Friday. Book club for electronic music.

## Stack

| Layer | Tech |
|---|---|
| Frontend | Plain HTML/CSS/JS (React later) |
| Backend | FastAPI (Python) |
| Database + Auth + Storage | Supabase |
| Email | Resend |
| Hosting | Vercel (frontend) + Vercel Serverless or Fly.io (backend) |

## Structure

```
looking-glass/
├── frontend/
│   ├── index.html      # Landing page + waitlist form
│   └── video1.mp4      # Not committed — host externally
├── backend/
│   ├── main.py         # FastAPI app
│   ├── requirements.txt
│   └── .env.example    # Copy to .env and fill in secrets
└── README.md
```

## Local dev

**Frontend** — open with Live Server (VS Code extension) or any static file server:
```bash
cd frontend
npx serve .
# visit http://localhost:3000
```

**Backend:**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your keys
uvicorn main:app --reload
# API at http://localhost:8000
# Docs at http://localhost:8000/docs
```

## Supabase setup (waitlist)

Run in the Supabase SQL editor:

```sql
create table waitlist (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  created_at timestamptz default now()
);
```

Then uncomment the Supabase block in `backend/main.py` and remove the placeholder `raise`.

## Video hosting

`video1.mp4` is gitignored (too large). Upload to Supabase Storage or Cloudflare R2 and update the `video.src` in `index.html` to the public URL.
