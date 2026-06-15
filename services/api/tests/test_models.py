from fastapi.testclient import TestClient

from app.main import app


def test_models_endpoint() -> None:
    client = TestClient(app)

    response = client.get("/api/v1/models")

    assert response.status_code == 200
    assert response.json() == {
        "models": [
            {
                "id": "yolov8n",
                "name": "YOLOv8n",
                "status": "supported",
                "task": "image_detection",
                "runtime": "onnx_runtime_cpu",
                "description": "Baseline CPU-only model candidate",
            },
            {
                "id": "yolov8s",
                "name": "YOLOv8s",
                "status": "planned",
                "task": "image_detection",
                "runtime": "onnx_runtime_cpu",
                "description": "Benchmark CPU-only model candidate",
            },
        ]
    }
