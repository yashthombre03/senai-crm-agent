from fastapi import FastAPI

from backend.api.routes.ingest import router as ingest_router
from backend.api.routes.threads import router as thread_router
from backend.api.routes.contacts import router as contact_router
from backend.api.routes.analytics import router as analytics_router
from backend.api.routes.intelligence import router as intelligence_router
from backend.api.routes.rag import router as rag_router
from backend.api.routes.audit import router as audit_router
from backend.api.routes.actions import router as actions_router



app = FastAPI(
    title="SenAI CRM"
)

app.include_router(
    ingest_router
)

app.include_router(
    thread_router
)

app.include_router(
    contact_router
)

app.include_router(
    analytics_router
)

app.include_router(
    intelligence_router
)

app.include_router(
    rag_router
)

app.include_router(
    audit_router
)

app.include_router(
    actions_router
)

@app.get("/")
def home():
    return {
        "message":"CRM Running"
    }