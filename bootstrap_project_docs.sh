#!/usr/bin/env bash
set -euo pipefail

mkdir -p \
  docs/project \
  docs/architecture \
  docs/api \
  docs/security \
  docs/compatibility \
  docs/ml \
  docs/deployment \
  docs/quality \
  docs/decisions

cat > AGENTS.md <<'EOF'
# AGENTS.md

## Purpose

This file defines how coding agents and human contributors should work in this repository.

The project is a professional CPU-only object detection platform with:
- a web application,
- a REST API,
- camera/image detection,
- Ultralytics YOLO models exported to ONNX,
- ONNX Runtime CPU inference,
- non-Docker deployment,
- small, reviewable PRs.

Agents must preserve the long-term project decisions recorded in `docs/`.

---

## Core Rules

1. Keep changes small and focused.
2. Prefer one feature per PR.
3. Do not introduce GPU requirements.
4. Do not introduce Docker deployment unless the project direction changes through an ADR.
5. Do not introduce Redis before the planned Alpha stage unless explicitly requested.
6. Do not add dependencies without a clear reason.
7. Do not perform broad refactors inside feature PRs.
8. Update documentation when changing architecture, API behavior, security behavior, deployment behavior, or model behavior.
9. Add tests for backend logic and API behavior whenever practical.
10. Preserve existing public API contracts unless the change is explicitly versioned.

---

## PR Size Guidance

The coding agent is expected to work best with small chunks.

Recommended limits:
- 1 feature per PR
- 3-8 files changed when possible
- preferably under 300-500 changed lines
- no unrelated formatting churn
- no frontend/backend/inference mixing unless necessary

---

## Required Context Files

Before making changes, agents should review relevant files:

- `docs/project/PROJECT_BRIEF.md`
- `docs/project/MVP_SPEC.md`
- `docs/project/ROADMAP_TO_RC1.md`
- `docs/project/AGENT_EXECUTION_PLAN.md`
- `docs/architecture/ARCHITECTURE_OVERVIEW.md`
- `docs/architecture/CPU_INFERENCE_STRATEGY.md`
- `docs/api/API_CONTRACT.md`
- `docs/security/SECURITY_MODEL.md`
- `docs/security/PRIVACY_AND_DATA_RETENTION.md`
- `docs/compatibility/COMPATIBILITY_MATRIX.md`
- `docs/ml/MODEL_STRATEGY.md`
- `docs/deployment/NON_DOCKER_DEPLOYMENT.md`
- `docs/quality/REVIEW_CHECKLIST.md`
- `docs/decisions/`

---

## Technology Direction

Current intended stack:

- Frontend: Next.js + React
- Backend/API: FastAPI
- Model framework: Ultralytics YOLO
- Initial models: YOLOv8n first, YOLOv8s benchmark second
- Runtime: ONNX Runtime CPU
- Image processing: OpenCV + NumPy
- Database: PostgreSQL when persistence is needed
- Redis: introduced at Alpha for jobs/rate limiting
- Deployment: non-Docker using systemd + Caddy or Nginx

---

## Non-Goals Unless Explicitly Requested

Agents must not assume the following are required for MVP:

- GPU inference
- Docker deployment
- Kubernetes
- video upload processing
- public commercial API
- browser-side inference
- custom model training
- multi-tenant SaaS infrastructure
- complex user management

---

## Task Format for Coding Agents

Use or expect tasks in this structure:

```markdown
## Objective
Implement one specific change.

## Context
Where this fits in the object detection platform.

## Scope
- Do X
- Do Y
- Add tests for Z

## Non-goals
- Do not modify unrelated code.
- Do not refactor architecture.
- Do not add dependencies unless listed.

## Expected files
- path/to/file
- path/to/test

## Acceptance criteria
- Behavior works as described.
- Tests pass.
- Docs are updated if behavior changes.

## Validation
Run the relevant commands, for example:
- pytest
- ruff check
- npm test
- npm run lint
EOF
