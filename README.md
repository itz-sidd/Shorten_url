⚡ High-Performance URL Shortener Dock (FlashURL clone)

## Table of Contents

* [About The Project](#about-the-project)
* [Features](#features)
* [Architecture & Tech Stack](#architecture--tech-stack)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation & Running Locally](#installation--running-locally)
* [Usage](#usage)

  * [API Endpoints](#api-endpoints)
  * [Web UI](#web-ui)
* [Deployment](#deployment)
* [Configuration / Environment Variables](#configuration--environment-variables)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## About The Project

Shorten_url is a modern, efficient link-shortening service built to handle high traffic and deliver fast redirects. Unlike a basic CRUD prototype, this project is architected for performance and scalability, employing caching, horizontal scaling, containerisation and persistence.

This repository includes:

* A web service built with Flask (Python)
* Persistent storage via PostgreSQL
* Caching via Redis to serve popular links in-memory
* Container-ready setup with Docker & Docker Compose
* A simple user interface for creating + using short links

---

## Features

* Ultra-fast link redirect via caching layer (Redis)
* Stateless application tier optimized for horizontal scaling
* Persistent storage via PostgreSQL for durability
* Containerised environment for development & deployment consistency
* Clean, responsive web UI (with dark mode)
* API endpoint to programmatically create short URLs
* Easy to deploy via Docker / Docker Compose

---

## Architecture & Tech Stack

**Tech Stack:**

* Backend: Python + Flask
* Cache: Redis
* Database: PostgreSQL
* Containerisation: Docker, Docker Compose
* Web UI: HTML / CSS / JavaScript

**Architecture in a nutshell:**
User → Web UI/API → Application (Flask + Gunicorn) →

* On each redirect: Check Redis cache → if hit, return redirect; if miss, fetch from PostgreSQL and then populate cache.
* On creation: Validate URL → generate unique short code → store in DB → optionally warm cache.

This design ensures that read-heavy redirect traffic is served from memory (Redis) quickly, reducing load on the primary database.

---

## Getting Started

### Prerequisites

* Docker & Docker Compose installed on your machine
* (Optional) Local installation of PostgreSQL & Redis if you prefer non-containerised setup

### Installation & Running Locally

```bash
# Clone repository  
git clone https://github.com/itz-sidd/Shorten_url.git  
cd Shorten_url  

# Build and run via Docker Compose  
docker-compose up --build  
```

Once up, the service will typically be available at `http://localhost:5000`.

---

## Usage

### API Endpoints

* **Create Short Link**

  * **Endpoint:** `POST /shorten`
  * **Headers:** `Content-Type: application/json`
  * **Request Body:**

    ```json
    {
      "original_url": "https://www.google.com"
    }
    ```
  * **Response Example:**

    ```json
    {
      "original_url": "https://www.google.com",
      "short_url": "http://your-domain.com/1a"
    }
    ```
* **Redirect via Short Code**

  * **Endpoint:** `GET /<short_code>`
  * **Behavior:** Redirects the user to the original long URL.

### Web UI

Navigate to the base URL of the service (e.g. `http://localhost:5000`) and use the simple interface to paste a long URL and get back a short link. The UI also supports default dark mode and is mobile responsive.

---

## Deployment

This project is designed to be deployed in a containerised production environment. You can use the provided `docker-compose.yml` or adapt it to your favourite orchestration platform (Kubernetes, ECS, etc.).
**Environment variables** such as `DATABASE_URL`, `REDIS_URL`, and `PORT` must be set in your production environment.

---

## Configuration / Environment Variables

Ensure the following environment variables are set:

| Variable       | Description                             | Example                                       |
| -------------- | --------------------------------------- | --------------------------------------------- |
| `DATABASE_URL` | Connection string for PostgreSQL        | `postgresql://user:password@host:5432/dbname` |
| `REDIS_URL`    | Connection for Redis cache              | `redis://host:6379/0`                         |
| `PORT`         | Port on which the Flask app will listen | `5000`                                        |

You may also configure other settings (e.g., short-code length, domain) by editing `config.py`.

---

## Contributing

Thanks for considering contribution! Here’s how you can help:

1. Fork the repository and create your branch (`git checkout -b feature/YourFeature`)
2. Make your changes, ensure code style / linting is maintained
3. Add tests (if applicable) and verify existing functionality
4. Submit a pull request with a clear description of your changes

Please follow best practices for commit messages and code structure. You can also open issues for discussion or bug reports.

---

## License

This project is under the MIT License. See the `LICENSE` file for details.

---

## Contact

Project maintained by **Siddharth** (GitHub: [@itz-sidd](https://github.com/itz-sidd)).
Feel free to reach out for questions, feedback or suggestions!

---

## Thank you for using / exploring Shorten_url! 🚀

