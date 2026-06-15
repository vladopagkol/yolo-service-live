# CPU Inference Strategy

The inference path should target CPU execution only.

Preferred direction:
- export models to ONNX
- run inference with ONNX Runtime CPU
- keep runtime dependencies minimal
