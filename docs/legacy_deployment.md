# Litfunder Backend - Deployment Guide

This guide covers deploying Litfunder to Render.com using both render.yaml and Docker approaches, as well as local Docker testing.

## Table of Contents

1. [Render.com Deployment (render.yaml)](#rendercom-deployment-renderyaml)
2. [Render.com Deployment (Docker)](#rendercom-deployment-docker)
3. [Local Docker Testing](#local-docker-testing)
4. [Environment Variables](#environment-variables)
5. [Database Migration](#database-migration)
6. [Troubleshooting](#troubleshooting)

---

## Render.com Deployment (render.yaml)

### Overview

The `render.yaml` file defines the complete infrastructure for Render.com, including:
- Web service (Django application)
- PostgreSQL database
- Environment variables
- Build and start commands
- Automatic migrations

### Prerequisites

1. GitHub account with the repository pushed
2. Render.com account (https://render.com)
3. Repository with `render.yaml` in root directory

### Step 1: Connect GitHub to Render

1. Go to https://dashboard.render.com
2. Click "New +" → "Blueprint"
3. Select "Public Git repository"
4. Enter: `https://github.com/predictivelabsai/litfunder-backend.git`
5. Click "Connect"

### Step 2: Configure Blueprint

1. Name your service: `litfunder-backend`
2. Branch: `main`
3. Root directory: `/` (leave empty)
4. Click "Create Blueprint"

### Step 3: Set Environment Variables

The following variables need to be configured in Render dashboard:

```
POSTMARK_API_KEY=your-postmark-api-key
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890
```

### Step 4: Deploy

1. Click "Deploy Blueprint"
2. Render will:
   - Build the application
   - Create PostgreSQL database
   - Run migrations automatically
   - Start the web service

### Accessing Your Deployment

- **Web Service**: `https://litfunder-backend.onrender.com`
- **Admin Panel**: `https://litfunder-backend.onrender.com/admin/`
- **API**: `https://litfunder-backend.onrender.com/api/`
- **Swagger UI**: `https://litfunder-backend.onrender.com/api/docs/`

### render.yaml Configuration Details

```yaml
services:
  - type: web                          # Web service
    name: litfunder-backend
    runtime: python311                 # Python 3.11
    buildCommand: |                    # Build steps
      pip install --upgrade pip
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
      python manage.py migrate         # Auto-migrate
    startCommand: gunicorn ...         # Start with Gunicorn
    plan: standard                     # Standard plan
    envVars: [...]                     # Environment variables

  - type: pserv                        # PostgreSQL service
    name: litfunder-db
    runtime: postgresql15
    plan: standard
```

### Monitoring Deployment

1. Go to Render dashboard
2. Click on your service
3. View logs in real-time
4. Check deployment status

---

## Render.com Deployment (Docker)

### Overview

Alternative approach using Docker for more control over the deployment process.

### Prerequisites

1. Docker installed locally (for testing)
2. Render.com account
3. GitHub repository

### Step 1: Create Dockerfile

The `Dockerfile` includes:
- Multi-stage build for smaller image size
- Python 3.11 slim base image
- Automatic migrations
- Gunicorn server
- Health checks
- Non-root user for security

### Step 2: Create Docker Image

```bash
# Build locally first
docker build -t litfunder-backend:latest .

# Test locally
docker run -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY=test-key \
  -e DB_URL=postgresql://... \
  litfunder-backend:latest
```

### Step 3: Push to Docker Registry

```bash
# Tag image
docker tag litfunder-backend:latest your-registry/litfunder-backend:latest

# Push to Docker Hub or other registry
docker push your-registry/litfunder-backend:latest
```

### Step 4: Deploy to Render

1. Go to Render dashboard
2. Click "New +" → "Web Service"
3. Select "Deploy existing image"
4. Enter image URL: `your-registry/litfunder-backend:latest`
5. Configure environment variables
6. Click "Create Web Service"

### Step 5: Configure PostgreSQL

1. Click "New +" → "PostgreSQL"
2. Name: `litfunder-db`
3. Database: `indurent_db`
4. User: `indurent_db_user`
5. Region: Frankfurt (or preferred)
6. Click "Create Database"

### Step 6: Link Database

1. Go to Web Service settings
2. Add environment variable: `DB_URL` = (copy from PostgreSQL service)
3. Click "Save"

### Docker Deployment Advantages

- More control over build process
- Faster deployments (cached layers)
- Consistent environment
- Easy local testing
- Version control of infrastructure

---

## Local Docker Testing

### Prerequisites

- Docker installed
- Docker Compose installed
- Git repository cloned

### Step 1: Build and Start Services

```bash
# Clone repository
git clone https://github.com/predictivelabsai/litfunder-backend.git
cd litfunder-backend

# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f web
```

### Step 2: Run Migrations

Migrations run automatically, but you can manually run:

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Generate mock data
docker-compose exec web python manage.py shell < litfunder/utils/generate_date.py
```

### Step 3: Access Services

- **Web App**: http://localhost:8000
- **Admin**: http://localhost:8000/admin/
- **API**: http://localhost:8000/api/
- **Swagger**: http://localhost:8000/api/docs/
- **Database**: localhost:5432

### Step 4: Useful Docker Commands

```bash
# View all containers
docker-compose ps

# View logs
docker-compose logs -f web
docker-compose logs -f db

# Execute command in container
docker-compose exec web python manage.py shell

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Rebuild image
docker-compose build --no-cache

# Scale services
docker-compose up -d --scale web=3
```

### Step 5: Database Access

```bash
# Access PostgreSQL directly
docker-compose exec db psql -U indurent_db_user -d indurent_db

# Common SQL commands
\dt                    # List tables
\d table_name          # Describe table
SELECT * FROM table;   # Query data
```

---

## Environment Variables

### Required Variables

```bash
# Django Configuration
DEBUG=False                                    # Production: False
SECRET_KEY=your-secret-key-here              # Generate a strong key
ALLOWED_HOSTS=localhost,127.0.0.1,*.onrender.com

# Database
DB_URL=postgresql://user:password@host:port/database
DATABASE_SCHEMA=litfunder

# Email Service (Postmark)
POSTMARK_API_KEY=your-postmark-api-key

# SMS Service (Twilio)
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890
```

### Optional Variables

```bash
# Logging
LOG_LEVEL=INFO

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# CORS
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

### Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Database Migration

### Automatic Migration (render.yaml)

The `render.yaml` includes automatic migration in the build command:

```yaml
buildCommand: |
  pip install -r requirements.txt
  python manage.py migrate  # Runs automatically
```

### Manual Migration

If needed, run migrations manually:

```bash
# Using Render CLI
render exec litfunder-backend python manage.py migrate

# Using Docker
docker-compose exec web python manage.py migrate

# Using SSH (if available)
ssh into container and run:
python manage.py migrate
```

### Creating Migrations

```bash
# Create new migration
python manage.py makemigrations

# Show migration status
python manage.py showmigrations

# Migrate specific app
python manage.py migrate cases
```

### Rollback Migration

```bash
# Rollback last migration
python manage.py migrate cases 0001

# Show migration history
python manage.py showmigrations cases
```

---

## Troubleshooting

### Issue: Build Fails with "ModuleNotFoundError"

**Solution:**
```bash
# Ensure all dependencies are in requirements.txt
pip freeze > requirements.txt

# Rebuild
docker-compose build --no-cache
```

### Issue: Database Connection Error

**Solution:**
```bash
# Check database URL format
# Should be: postgresql://user:password@host:port/database

# Test connection
python manage.py dbshell

# Check environment variables
echo $DB_URL
```

### Issue: Static Files Not Loading

**Solution:**
```bash
# Collect static files
python manage.py collectstatic --noinput --clear

# In Docker:
docker-compose exec web python manage.py collectstatic --noinput
```

### Issue: Migrations Not Running

**Solution:**
```bash
# Check migration status
python manage.py showmigrations

# Run specific migration
python manage.py migrate cases 0001

# Force migration
python manage.py migrate --run-syncdb
```

### Issue: Permission Denied Errors

**Solution:**
```bash
# In Docker, ensure proper permissions
docker-compose exec web chown -R appuser:appuser /app

# Rebuild with correct Dockerfile
docker-compose build --no-cache
```

### Issue: Out of Memory

**Solution:**
```yaml
# In docker-compose.yml, add memory limits:
services:
  web:
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
```

### Issue: Port Already in Use

**Solution:**
```bash
# Change port in docker-compose.yml
ports:
  - "8001:8000"  # Map to different port

# Or kill existing process
lsof -ti:8000 | xargs kill -9
```

### Viewing Logs

```bash
# Render.com
# Dashboard → Service → Logs

# Docker Compose
docker-compose logs -f web
docker-compose logs -f db

# Docker (single container)
docker logs -f container_name

# Follow logs with timestamps
docker-compose logs -f --timestamps web
```

---

## Health Checks

### Render.com Health Check

The `render.yaml` includes health checks:

```yaml
healthCheck:
  path: /admin/
  expectedStatus: 200
```

### Docker Health Check

The `Dockerfile` includes health checks:

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/admin/ || exit 1
```

### Manual Health Check

```bash
# Test API
curl -s http://localhost:8000/api/legal-cases/ | python -m json.tool

# Test admin
curl -s http://localhost:8000/admin/ | head -20

# Check database
python manage.py dbshell
```

---

## Performance Optimization

### Gunicorn Workers

```bash
# In Dockerfile or render.yaml
gunicorn litfunder.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --worker-class sync \
  --timeout 60
```

### Database Connection Pooling

```python
# In settings.py
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 600,  # Connection pooling
        'OPTIONS': {
            'connect_timeout': 10,
        }
    }
}
```

### Caching

```python
# Add Redis for caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

---

## Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Generate strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` properly
- [ ] Use HTTPS (Render provides free SSL)
- [ ] Set secure cookie flags
- [ ] Enable CSRF protection
- [ ] Use environment variables for secrets
- [ ] Restrict database access
- [ ] Enable logging and monitoring
- [ ] Regular backups of database
- [ ] Keep dependencies updated

---

## Monitoring & Logging

### Render.com Monitoring

1. Dashboard → Service → Metrics
2. View CPU, Memory, Requests
3. Set up alerts

### Docker Logging

```bash
# View logs
docker-compose logs -f web

# Save logs to file
docker-compose logs web > logs.txt

# View specific number of lines
docker-compose logs --tail=100 web
```

### Application Logging

```python
# In settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/app/logs/django.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

---

## Backup & Recovery

### Database Backup

```bash
# Backup PostgreSQL
pg_dump -U indurent_db_user -h host -d indurent_db > backup.sql

# Restore from backup
psql -U indurent_db_user -h host -d indurent_db < backup.sql
```

### Render.com Backups

1. Dashboard → PostgreSQL → Backups
2. Automatic daily backups
3. Manual backup option available

---

## Scaling

### Horizontal Scaling (Multiple Instances)

```yaml
# In render.yaml
services:
  - type: web
    numInstances: 2  # Run 2 instances
```

### Vertical Scaling (Larger Instance)

```yaml
# In render.yaml
plan: standard_plus  # Upgrade plan
```

---

## Support & Resources

- [Render Documentation](https://render.com/docs)
- [Django Deployment Guide](https://docs.djangoproject.com/en/5.2/howto/deployment/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Gunicorn Documentation](https://gunicorn.org/)

---

**Last Updated**: November 28, 2025  
**Version**: 1.0.0  
**Status**: Production Ready
