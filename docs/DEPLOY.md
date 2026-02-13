# Deployment Instructions

This guide covers deploying the Titanic Survival Prediction application to a production server.

---

## Prerequisites

- A Linux/Mac/Windows server (Ubuntu 20.04+) with Python 3.11+, pip, and git installed.
- Domain name (optional) pointed to your server IP.
- PostgreSQL (optional, recommended over SQLite for production).

---

## Option 1: Deploy with Gunicorn and Nginx

### 1. Clone the repository

```bash
git clone (git url)
cd titanic_capstone
```

### 2. Set up a virtual environment (example)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a .env file in the project root (or set system environment variables):

SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://user:password@localhost:5432/dbname

### 4.Set up PostgreSQL(optional)

```bash
sudo apt install postgresql postgresql-contrib
sudo -u postgres createdb titanic_db
sudo -u postgres createuser --interactive
```

Update DATABASE_URL in .env accordingly.

### 5. Run migrations and collect static files

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6. Install and configure Gunicorn

```bash
bash: pip install gunicorn
```

Create a systemd service file /etc/systemd/system/gunicorn.service:

[Unit]
Description=gunicorn daemon for titanic
After=network.target

[Service]
User=youruser
Group=www-data
WorkingDirectory=/path/to/titanic-survival-prediction
ExecStart=/path/to/titanic-survival-prediction/venv/bin/gunicorn --workers 3 --bind unix:/path/to/titanic-survival-prediction/titanic.sock titanic_project.wsgi:application

[Install]
WantedBy=multi-user.target

Start and enable the service:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 7. Install and configure Nginx

```bash
sudo apt install nginx
```

Create a Nginx config file /etc/nginx/sites-available/titanic:
server {
    listen 80;
    server_name yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /path/to/titanic-survival-prediction/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/titanic-survival-prediction/titanic.sock;
    }
}

Enable the site and test:

```bash
sudo ln -s /etc/nginx/sites-available/titanic /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 8. Secure with SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```
