from fastapi import FastAPI, HTTPException
from app.llm_client import explain_code_with_llm
from app.schemas import ExplainRequest, ExplainResponse
import json
import traceback

app = FastAPI(title="AI Code Assistant")


@app.post("/explain", response_model=ExplainResponse)
def explain_code(request: ExplainRequest) -> ExplainResponse:
    try:
        response = explain_code_with_llm(
            code=request.code,
            language=request.language or "unspecified"
        )
        return ExplainResponse(**response)
    except Exception as e:
        error_detail = f"{str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)