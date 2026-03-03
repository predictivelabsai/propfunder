# Litfunder - Quick Start Deployment Guide

## 🚀 Choose Your Deployment Method

### Option 1: Render.com with render.yaml (Recommended - Easiest)
### Option 2: Render.com with Docker
### Option 3: Local Docker Testing

---

## Option 1: Render.com with render.yaml ⭐ (Recommended)

### What You Get
- ✅ Automatic database setup
- ✅ Automatic migrations
- ✅ Auto-scaling
- ✅ Free SSL/TLS
- ✅ Built-in monitoring

### Steps (5 minutes)

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Go to Render Dashboard**
   - Visit https://dashboard.render.com
   - Click "New +" → "Blueprint"

3. **Connect Repository**
   - Select "Public Git repository"
   - Paste: `https://github.com/predictivelabsai/litfunder-backend.git`
   - Click "Connect"

4. **Review Configuration**
   - Name: `litfunder-backend`
   - Branch: `main`
   - Click "Create Blueprint"

5. **Add Environment Variables**
   - Go to Web Service settings
   - Add these variables:
     ```
     POSTMARK_API_KEY=your-key
     TWILIO_ACCOUNT_SID=your-sid
     TWILIO_AUTH_TOKEN=your-token
     TWILIO_PHONE_NUMBER=+1234567890
     ```

6. **Deploy**
   - Click "Deploy Blueprint"
   - Wait for deployment (2-3 minutes)

### Access Your App
- **Web**: https://litfunder-backend.onrender.com
- **Admin**: https://litfunder-backend.onrender.com/admin/
- **API**: https://litfunder-backend.onrender.com/api/
- **Swagger**: https://litfunder-backend.onrender.com/api/docs/

### Default Credentials
- Email: `admin@litfunder.com`
- Password: `admin123`

---

## Option 2: Render.com with Docker

### What You Get
- More control over build process
- Faster deployments
- Version-controlled infrastructure

### Steps (10 minutes)

1. **Build Docker Image**
   ```bash
   docker build -t litfunder-backend:latest .
   ```

2. **Test Locally (Optional)**
   ```bash
   docker-compose up -d
   # Access at http://localhost:8000
   docker-compose down
   ```

3. **Push to Docker Registry**
   ```bash
   # Using Docker Hub
   docker tag litfunder-backend:latest your-username/litfunder-backend:latest
   docker push your-username/litfunder-backend:latest
   ```

4. **Create Services on Render**
   
   **A. Create PostgreSQL Database**
   - Go to https://dashboard.render.com
   - Click "New +" → "PostgreSQL"
   - Name: `litfunder-db`
   - Database: `indurent_db`
   - User: `indurent_db_user`
   - Region: Frankfurt
   - Click "Create Database"
   - Copy the connection string

   **B. Create Web Service**
   - Click "New +" → "Web Service"
   - Select "Deploy existing image"
   - Image: `your-username/litfunder-backend:latest`
   - Name: `litfunder-backend`
   - Plan: Standard
   - Click "Create Web Service"

5. **Configure Environment Variables**
   - Go to Web Service → Environment
   - Add variables:
     ```
     DEBUG=False
     SECRET_KEY=(generate with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
     DB_URL=(paste from PostgreSQL service)
     DATABASE_SCHEMA=litfunder
     POSTMARK_API_KEY=your-key
     TWILIO_ACCOUNT_SID=your-sid
     TWILIO_AUTH_TOKEN=your-token
     TWILIO_PHONE_NUMBER=+1234567890
     ```

6. **Deploy**
   - Click "Manual Deploy" or wait for auto-deploy
   - Check logs for any errors

### Access Your App
- Same as Option 1

---

## Option 3: Local Docker Testing

### What You Get
- Test before deploying to production
- Full control over environment
- Quick iteration

### Steps (5 minutes)

1. **Clone Repository**
   ```bash
   git clone https://github.com/predictivelabsai/litfunder-backend.git
   cd litfunder-backend
   ```

2. **Start Services**
   ```bash
   docker-compose up -d
   ```

3. **Initialize Database**
   ```bash
   # Migrations run automatically, but you can manually run:
   docker-compose exec web python manage.py migrate
   
   # Create superuser
   docker-compose exec web python manage.py createsuperuser
   
   # Generate mock data (optional)
   docker-compose exec web python manage.py shell < litfunder/utils/generate_date.py
   ```

4. **Access Services**
   - Web: http://localhost:8000
   - Admin: http://localhost:8000/admin/
   - API: http://localhost:8000/api/
   - Swagger: http://localhost:8000/api/docs/
   - Database: localhost:5432

5. **Useful Commands**
   ```bash
   # View logs
   docker-compose logs -f web
   
   # Access shell
   docker-compose exec web python manage.py shell
   
   # Stop services
   docker-compose down
   
   # Stop and remove data
   docker-compose down -v
   ```

---

## 📋 Pre-Deployment Checklist

- [ ] Code pushed to GitHub main branch
- [ ] All dependencies in requirements.txt
- [ ] render.yaml in repository root
- [ ] Dockerfile in repository root
- [ ] Environment variables prepared
- [ ] Database credentials ready
- [ ] Email service (Postmark) configured
- [ ] SMS service (Twilio) configured
- [ ] SECRET_KEY generated
- [ ] ALLOWED_HOSTS configured

---

## 🔧 Environment Variables Needed

### Minimum (Required)
```
DEBUG=False
SECRET_KEY=your-generated-key
DB_URL=postgresql://...
DATABASE_SCHEMA=litfunder
```

### Recommended (For Full Features)
```
POSTMARK_API_KEY=your-postmark-key
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890
```

### Generate SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🐛 Troubleshooting

### Build Fails
```bash
# Check logs in Render dashboard
# Or locally:
docker build -t litfunder-backend:latest .
```

### Database Connection Error
```bash
# Verify DB_URL format:
# postgresql://user:password@host:port/database

# Test connection:
docker-compose exec web python manage.py dbshell
```

### Migrations Not Running
```bash
# Manually run migrations:
docker-compose exec web python manage.py migrate

# Check status:
docker-compose exec web python manage.py showmigrations
```

### Static Files Not Loading
```bash
# Collect static files:
docker-compose exec web python manage.py collectstatic --noinput
```

---

## 📚 Full Documentation

For detailed information, see:
- [DEPLOYMENT.md](DEPLOYMENT.md) - Complete deployment guide
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API reference
- [README.md](README.md) - Project overview

---

## 🎉 Success!

Once deployed, you should see:
- ✅ Web service running
- ✅ Database connected
- ✅ Admin panel accessible
- ✅ API responding
- ✅ Swagger UI available

### Default Access
- **Admin**: admin@litfunder.com / admin123
- **API Base**: /api/
- **Swagger**: /api/docs/

---

## 📞 Support

If you encounter issues:

1. Check Render logs in dashboard
2. Review DEPLOYMENT.md troubleshooting section
3. Verify environment variables
4. Check database connectivity
5. Review application logs

---

**Recommended**: Use Option 1 (render.yaml) for fastest deployment!

**Last Updated**: November 28, 2025
