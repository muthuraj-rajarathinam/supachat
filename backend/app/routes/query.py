from fastapi import APIRouter
from pydantic import BaseModel
from app.services.sql_generator import generate_sql
from app.services.db import run_query

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
def query_data(req: QueryRequest):
    sql = generate_sql(req.query)
    data = run_query(sql)

    return {
        "query": req.query,
        "sql": sql,
        "data": data
    }