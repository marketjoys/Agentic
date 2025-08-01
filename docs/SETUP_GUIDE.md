# AI Email Responder - Quick Setup Guide

## One-Command Setup 🚀

Run the complete setup with a single command:

```bash
./setup.sh
```

This script will:

1. ✅ **Check system dependencies** (Python, Node.js, install MongoDB if needed)
2. 🗄️ **Install MongoDB** if not already present (Community Edition)
3. 🐍 **Install Python dependencies** (FastAPI, MongoDB drivers, AI libraries)
4. 🌟 **Install Node.js dependencies** (React, Tailwind, Axios)
5. 🗄️ **Setup MongoDB database** with test data
6. 👤 **Create test user account** (testuser/testpass123)
7. 🚀 **Start all services** (Backend, Frontend, MongoDB)
8. 🔍 **Perform health checks** and display status

## Access Information

After setup completes, you can access:

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:8001
- **API Health Check**: http://localhost:8001/api/health

## Test User Credentials

- **Username**: `testuser`
- **Password**: `testpass123`
- **Email**: `test@example.com`

## Service Management

### MongoDB Installation Methods

1. **Official MongoDB Repository** (preferred)
   - Installs latest MongoDB Community Edition
   - Includes proper systemd service configuration

2. **Ubuntu Repository** (fallback)
   - Uses system package manager
   - Guaranteed compatibility with Ubuntu/Debian

3. **Direct Process** (final fallback)
   - Starts MongoDB directly if services fail
   - Creates basic configuration for immediate use

Use the included management script for easy service control:

```bash
# Start all services
./manage.sh start

# Stop all services  
./manage.sh stop

# Check service status
./manage.sh status

# Restart all services
./manage.sh restart
```

## Manual Service Commands

If you need to manage services manually:

```bash
# Check what's running
ps aux | grep uvicorn     # Backend
ps aux | grep yarn        # Frontend

# Stop services
pkill -f 'uvicorn.*backend.server'  # Stop backend
pkill -f 'yarn.*start'             # Stop frontend

# View logs
tail -f /tmp/backend.log   # Backend logs
tail -f /tmp/frontend.log  # Frontend logs
```

## Database Information

- **Database Name**: `email_responder`
- **MongoDB URL**: `mongodb://localhost:27017`
- **Collections**: users, prospects, templates, campaigns, intents, lists, email_providers

## Sample Data Included

The setup automatically creates:
- 1 test user account
- 5 sample prospects
- 4 email templates
- 2 sample campaigns
- 4 intent configurations
- 4 prospect lists
- 2 email providers

## Troubleshooting

If setup fails:

1. **Check logs**: `tail -f /tmp/backend.log` or `tail -f /tmp/frontend.log`
2. **Verify ports**: Make sure ports 3000 and 8001 are available
3. **Check MongoDB**: Ensure MongoDB service is running
4. **MongoDB installation issues**: The script tries multiple installation methods
5. **Permission issues**: Make sure you have sudo access
6. **Network issues**: Check internet connectivity for package downloads
7. **Re-run setup**: The script is idempotent - safe to run multiple times

### MongoDB Specific Issues

- **Installation fails**: Script tries official repo first, then Ubuntu repo
- **Service won't start**: Script attempts systemd, service command, then direct process
- **Permission errors**: Script creates necessary directories with proper ownership
- **Port conflicts**: MongoDB uses port 27017 by default
- **Log files**: Check `/tmp/mongod.log` for MongoDB startup errors

## Features Available

Once setup is complete, you can:

- 📊 **View Dashboard** with real-time metrics
- 👥 **Manage Prospects** and contact lists
- 📧 **Create Email Templates** with variables
- 🚀 **Launch Campaigns** with scheduling
- 🤖 **Configure AI Intent Detection** 
- 📈 **View Analytics** and performance metrics
- ⚙️ **Manage Email Providers** (Gmail, Outlook)

## Quick Start

1. Run `./setup.sh` and wait for completion
2. Open browser to http://localhost:3000
3. Login with `testuser` / `testpass123`
4. Explore the dashboard and features!

---

*The AI Email Responder is powered by Groq AI and includes comprehensive email campaign management, intent detection, and automated response capabilities.*