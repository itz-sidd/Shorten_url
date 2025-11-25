🚀 High-Performance URL Shortener

A full-stack, containerized URL shortening service built to demonstrate scalable microservices architecture. It features a persistent database layer, an in-memory caching layer for high performance, and a modern dark-mode UI.

🔴 Live Demo

🏗 Architecture

This project moves beyond simple scripts by implementing a 3-tier architecture orchestrated via Docker Compose:

Web Service (Flask + Gunicorn): Handles HTTP requests and business logic.

Caching Layer (Redis): Stores frequently accessed URL mappings in memory (RAM) to reduce database load and latency. Implements an LRU (Least Recently Used) eviction policy.

Persistence Layer (PostgreSQL): Stores all historical data permanently.

Performance Strategy

Write Operations: Saved to PostgreSQL first, then ID generated (Base62), then updated.

Read Operations:

Check Redis Cache first. (Speed: <5ms)

If Miss: Check PostgreSQL. (Speed: ~50ms)

Save result to Redis with a 1-hour expiration (TTL).

Redirect user.

🛠 Tech Stack

Backend: Python 3, Flask

Database: PostgreSQL 15

Cache: Redis (Alpine)

Containerization: Docker & Docker Compose

Server: Gunicorn (Production WSGI)

Frontend: HTML5, CSS3 (Responsive Dark Mode), JavaScript (Fetch API)

Deployment: Render Cloud

⚡ Local Installation & Setup

You can run the entire infrastructure locally with a single command using Docker.

Prerequisites

Docker Desktop installed and running.

Steps

Clone the repository

git clone [https://github.com/itz-sidd/Shorten_url.git](https://github.com/itz-sidd/Shorten_url.git)
cd Shorten_url


Run with Docker Compose

docker-compose up --build


Access the App

Open your browser to: http://localhost:5000

API is available at: http://localhost:5000/shorten

🔌 API Endpoints

1. Shorten a URL

Request:
POST /shorten

{
  "original_url": "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
}


Response:

{
  "original_url": "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
  "short_url": "[https://url-shorten-dock.onrender.com/1](https://url-shorten-dock.onrender.com/1)"
}


2. Redirect

Request:
GET /<short_code>

Behavior:

Redirects to the original long URL.

Returns 404 JSON if the code does not exist.

📂 Project Structure

/
├── app.py              # Application factory & entry point
├── routes.py           # API endpoints & Controller logic
├── models.py           # SQLAlchemy Database Models
├── config.py           # Environment Configuration
├── extensions.py       # Plugin initialization (DB, Redis)
├── utils.py            # Base62 Encoding/Decoding logic
├── Dockerfile          # Python/Flask Container instructions
├── docker-compose.yml  # Orchestration of App + DB + Redis
└── templates/
    └── index.html      # Frontend UI
