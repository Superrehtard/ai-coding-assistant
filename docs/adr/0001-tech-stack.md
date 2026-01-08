## Refined ADR 0001

### Context

We are building an AI-assisted code explainer service. The system takes a request with code and the programming language and responds with a simple, human-readable explanation of the code.

- API calls need low latency.
- System may scale in the future, though scaling isn’t implemented yet.

### Decision

We will use:

- Python 3.13 – modern Python version with new features and performance improvements.
- FastAPI – for the API layer.
- OpenAI API – for LLM inference.
- uv – for dependency and environment management.
- Docker – for containerization and reproducible deployments.
- AWS – for hosting and deployment.

#### Why FastAPI?

- Async-first: Supports async/await natively, which is important for handling many concurrent API calls with low latency.
- Modern: Actively maintained with strong community support and modern Python features.
- OpenAPI / docs: Automatically generates Swagger docs, making testing and integrations easier.
- Performance: Benchmarks show FastAPI is one of the fastest Python web frameworks, close to Node.js in some cases.
- Type safety: Integrates tightly with Pydantic for request validation and data serialization.

### Alternatives Considered

- Bottle – Simple microframework, lightweight, but lacks async support and modern tooling. Good for tiny scripts, but less suitable for production APIs.
- Gemini API – Alternative LLM provider. Less mature and less widely used than OpenAI for this use case.
- Poetry vs requirements.txt vs pip vs uv – uv chosen for modern dependency management, deterministic builds, and fast dev cycles.

### Consequences

- FastAPI allows low-latency API calls and scales well when needed.
- Dependency and deployment tooling (uv + Docker + AWS) ensures reproducible, portable environments.
- OpenAI API dependency introduces cost and external network dependency.