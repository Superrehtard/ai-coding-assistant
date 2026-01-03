from fastapi import FastAPI
from app.schemas import ExplainRequest, ExplainResponse

app = FastAPI(title="AI Code Assistant")


@app.post("/explain", response_model=ExplainResponse)
def explain_code(request: ExplainRequest) -> ExplainResponse:
    return ExplainResponse(
        explanation="Coming soon...",
        improvements=[],
        edge_cases=[],
    )