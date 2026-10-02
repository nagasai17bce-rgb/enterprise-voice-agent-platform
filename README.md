# Enterprise Voice Agent Platform

## Overview
A session-oriented voice-agent backend for transcripts, actions, handoffs, and future telephony and real-time model integrations.

This is a runnable engineering reference, not a notebook or mockup. The service separates the HTTP layer from domain logic and is designed so demo components can later be replaced by managed infrastructure.

## Architecture
```
Client -> FastAPI -> Domain Service -> Policies / Providers / State -> Structured response
```

## Repository structure
- `app/main.py` — API and validation
- `app/service.py` — domain behavior
- `tests/test_api.py` — regression tests
- `examples/request.sh` — runnable example
- `Dockerfile` — container packaging
- `pyproject.toml` — dependencies
- `.github/workflows/ci.yml` — CI

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Health:
```bash
curl http://localhost:8000/health
```

Example:
```bash
bash examples/request.sh
```

## API
### GET /health
Returns `{"status":"ok"}`.

### POST /v1/run
Request:
```json
{"value":"demo request"}
```

The response is structured JSON so clients do not need to parse prose.

## Testing
```bash
pytest -q
```

Production systems should add integration, contract, load, failure-injection, and security tests.

## Docker
```bash
docker build -t enterprise-voice-agent-platform .
docker run --rm -p 8000:8000 enterprise-voice-agent-platform
```

## Design principles
- Keep domain logic deterministic and testable.
- Keep model/provider integrations behind adapters.
- Require authorization before privileged tools.
- Emit structured audit and telemetry events.
- Treat untrusted input as hostile.
- Prefer explicit state transitions over implicit agent behavior.

## Production architecture
A production deployment can add API gateway authentication, OIDC/workload identity, PostgreSQL, Redis, Kafka or Pub/Sub, object storage, OpenTelemetry, Prometheus-compatible metrics, a secrets manager, Kubernetes, and CI/CD deployment gates.

## Reliability
Add timeouts, retries with backoff, circuit breakers, rate limits, idempotency keys, dead-letter queues, graceful shutdown, dependency health checks, structured logs, SLOs, and alerting.

## Security
Never commit credentials. Use environment variables locally and a managed secrets system in production. Add tenant isolation, least-privilege identities, input/output validation, PII and secret redaction, audit logs, dependency scanning, and network egress controls.

## CI/CD
The included workflow runs tests on pushes and pull requests. A production pipeline should add linting, integration tests, security scans, container scanning/signing, staging deployment, smoke tests, and production approval.

## Roadmap
1. Durable state
2. Authentication and multi-tenancy
3. Real provider adapters
4. OpenTelemetry tracing
5. Load and failure testing
6. Infrastructure as code
7. Kubernetes deployment
8. Operational dashboards and SLOs

## Project-specific design notes
**Core problem:** A session-oriented voice-agent backend for transcripts, actions, handoffs, and future telephony and real-time model integrations.

**Production extension:** Replace the local deterministic implementation with real infrastructure while preserving the domain service and API contracts.