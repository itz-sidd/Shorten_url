⚡ URL-SHORTNER_DOCK: High-Performance Link Shortener

📖 About The Project

FlashURL is not just another URL shortener; it is a microservices-ready application designed to handle high-traffic loads efficiently.

Unlike basic CRUD applications, this project implements a Read-Through Caching Strategy using Redis. This ensures that popular links are served instantly from memory (RAM), protecting the primary database from being overwhelmed by read traffic.

🌟 Key Features

🚀 Ultra-Fast Redirects: Sub-millisecond read times using Redis caching.

🐳 Fully Containerized: Docker & Docker Compose setup for consistent development and deployment environments.

💾 Persistent Storage: PostgreSQL ensures data integrity and durability.

🔄 Scalable Architecture: Stateless application tier (Flask + Gunicorn) ready for horizontal scaling.

🌑 Modern UI: Clean, responsive dark-mode frontend for user interaction.

🏗️ System Architecture

The application follows a 3-tier architecture optimized for read-heavy workloads:

graph LR
    User -->|HTTP Request| LoadBalancer
    LoadBalancer --> App(Flask Service)
    App -->|1. Check Cache| Cache(Redis)
    Cache -- Hit --> App
    Cache -- Miss --> App
    App -->|2. Fetch Data| DB(PostgreSQL)
    App -->|3. Update Cache| Cache
    App -->|4. Response| User


🚀 Getting Started

Follow these steps to get a local copy up and running.

Prerequisites

Docker Desktop installed on your machine.

Installation & Run

Clone the repo

git clone [https://github.com/itz-sidd/Shorten_url.git](https://github.com/itz-sidd/Shorten_url.git)
cd Shorten_url


Start the services

docker-compose up --build


That's it!

Visit the UI: http://localhost:5000

API Endpoint: http://localhost:5000/shorten

🔌 API Reference

1. Create Short Link

URL: /shorten

Method: POST

Headers: Content-Type: application/json

Body:

{
  "original_url": "[https://www.google.com](https://www.google.com)"
}


Response:

{
  "original_url": "[https://www.google.com](https://www.google.com)",
  "short_url": "[https://url-shorten-dock.onrender.com/1a](https://url-shorten-dock.onrender.com/1a)"
}


2. Access Link

URL: /<short_code>

Method: GET

Description: Redirects the user to the original long URL.

☁️ Deployment

This project is deployed using a CI/CD workflow on Render.

Service Type: Web Service (Docker Runtime)

Database: Managed PostgreSQL 15

Cache: Managed Redis (Valkey)

Environment Variables Required:

DATABASE_URL: PostgreSQL connection string.

REDIS_URL: Redis connection string.

PORT: 5000

👤 Author

Siddharth

GitHub: @itz-sidd

📄 License
