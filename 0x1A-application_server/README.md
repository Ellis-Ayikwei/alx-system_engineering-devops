# 0x1A. Application Server

## Overview
This project involves setting up and configuring an application server to serve dynamic content, connecting it to Nginx, and integrating it with your Airbnb clone project. The tasks will guide you through development and production setup using Flask, Gunicorn, and Nginx.

## Project Timeline
- **Start:** Jun 10, 2024, 6:00 AM
- **End:** Jun 14, 2024, 6:00 AM
- **Checker Release:** Jun 12, 2024, 8:24 PM
- **Auto Review:** At the deadline

## Concepts
- Web Server
- Server
- Web Stack Debugging

## Background
Your web infrastructure currently serves web pages via Nginx. This project will add an application server to your setup, allowing it to serve your Airbnb clone project dynamically.

## Resources
- [Application server vs web server](https://www.youtube.com/watch?v=5jfqYwdj8KQ)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Flask strict_slashes](https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Requirements
- **General**
  - A `README.md` file at the root of the project is mandatory.
  - All Python-related tasks must use Python 3.
  - All configuration files must include comments.
- **Bash Scripts**
  - Interpreted on Ubuntu 16.04 LTS.
  - End with a new line.
  - Must be executable.
  - Must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without errors.
  - The first line should be `#!/usr/bin/env bash`.
  - The second line should be a comment explaining the script's purpose.

## Server Information
| Name           | Username | IP             | State   |
|----------------|----------|----------------|---------|
| 313389-web-01  | ubuntu   | 100.27.11.38   | running |
| 313389-web-02  | ubuntu   | 107.23.156.4   | running |
| 313389-lb-01   | ubuntu   | 52.91.116.240  | running |

## Tasks

### 0. Set up Development with Python
- **Objective:** Serve the Airbnb clone v2 on web-01.
- **Steps:**
  1. Complete task #3 of your SSH project for web-01.
  2. Install `net-tools`: `sudo apt install -y net-tools`.
  3. Clone the repository on web-01: `git clone https://github.com/your_repo/AirBnB_clone_v2`.
  4. Configure `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000.
  5. Ensure the Flask application object is named `app`.

### 1. Set up Production with Gunicorn
- **Objective:** Serve the application with Gunicorn on web-01, port 5000.
- **Steps:**
  1. Install Gunicorn and other required libraries.
  2. Serve the same content from the previous task using Gunicorn.
  3. Ensure the Flask application object is named `app`.

### 2. Serve a Page with Nginx
- **Objective:** Configure Nginx to serve your page from the route `/airbnb-onepage/`.
- **Steps:**
  1. Ensure Nginx serves the page locally and on its public IP on port 80.
  2. Proxy requests to the process on port 5000.
  3. Include the Nginx config file as `2-app_server-nginx_config`.

### 3. Add a Route with Query Parameters
- **Objective:** Expand the web application by adding a service for Gunicorn to handle.
- **Steps:**
  1. Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/<int:n>` to Gunicorn on port 5001.
  2. Include the Nginx config file as `3-app_server-nginx_config`.

### 4. Serve Your API
- **Objective:** Serve the Airbnb clone v3 RESTful API on web-01.
- **Steps:**
  1. Clone `AirBnB_clone_v3`.
  2. Setup Nginx to route `/api/` to Gunicorn on port 5002.
  3. Include the Nginx config file as `4-app_server-nginx_config`.

### 5. Serve Your AirBnB Clone
- **Objective:** Serve the Airbnb clone - Web dynamic on web-01.
- **Steps:**
  1. Clone `AirBnB_clone_v4`.
  2. Setup Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
  3. Setup Nginx to point to Gunicorn on port 5003.
  4. Include the Nginx config file as `5-app_server-nginx_config`.

### 6. Deploy It! (Advanced)
- **Objective:** Use `systemd` to run your application server on Linux startup.
- **Steps:**
  1. Write a `systemd` script to start a Gunicorn process serving `web_dynamic/2-hbnb.py`.
  2. Spawn 3 worker processes.
  3. Log errors to `/tmp/airbnb-error.log` and access to `/tmp/airbnb-access.log`.
  4. Bind to port 5003.
  5. Start and enable the `systemd` service.
  6. Upload `gunicorn.service` to GitHub.

### 7. No Service Interruption (Advanced)
- **Objective:** Reload Gunicorn gracefully to avoid downtime.
- **Steps:**
  1. Write a Bash script to reload Gunicorn without downtime.

## Repository Structure
- **GitHub Repository:** `alx-system_engineering-devops`
- **Directory:** `0x1A-application_server`

### Files
- `README.md`
- `2-app_server-nginx_config`
- `3-app_server-nginx_config`
- `4-app_server-nginx_config`
- `5-app_server-nginx_config`
- `gunicorn.service`
