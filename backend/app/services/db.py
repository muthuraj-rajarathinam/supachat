from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def run_query(sql: str):
    # TEMP: return mock data (safe for now)
    if "group by topic" in sql.lower():
        return [
            {"topic": "AI", "total_views": 2700},
            {"topic": "DevOps", "total_views": 2000}
        ]

    return [
        {"title": "AI Trends", "views": 1200}
    ]