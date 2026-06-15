from fastapi import APIRouter

router = APIRouter()


@router.get("/models")
def list_models() -> dict[str, list[dict[str, str]]]:
    return {
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
