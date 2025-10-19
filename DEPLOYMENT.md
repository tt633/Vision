# Deployment Guide for Milestone Savings App on Render

## Prerequisites
- A GitHub account
- A Render account (sign up at https://render.com)
- Git installed on your machine

## Step 1: Push Your Code to GitHub

1. Initialize git repository (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub

3. Push your code:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Render

1. Log in to your Render dashboard (https://dashboard.render.com)

2. Click "New +" and select "Blueprint"

3. Connect your GitHub repository

4. Render will automatically detect the `render.yaml` file and create:
   - A PostgreSQL database (`milestone-db`)
   - A web service (`milestone-app`)

5. Click "Apply" to start the deployment

6. Wait for the build to complete (this may take 5-10 minutes)

## Step 3: Access Your Database Connection Details

1. In the Render dashboard, go to your `milestone-db` database

2. Click on "Info" tab

3. You'll see connection details:
   - **Hostname**: (e.g., `dpg-xxxxx-a.oregon-postgres.render.com`)
   - **Port**: `5432`
   - **Database**: `milestone_db`
   - **Username**: `milestone_admin`
   - **Password**: (auto-generated)
   - **Internal Database URL**: (for connecting from your app)
   - **External Database URL**: (for connecting from DBeaver)

## Step 4: Create Read-Only User

1. Connect to your database using the Render dashboard's built-in SQL editor:
   - Go to your database in Render
   - Click on "Connect" → "PSQL Command"
   - Copy the command and run it in your terminal

2. Once connected, run the SQL commands from `setup_db_users.sql`:

```sql
-- Create read-only user
CREATE USER milestone_readonly WITH PASSWORD 'YourSecurePassword123!';

-- Grant connect privilege
GRANT CONNECT ON DATABASE milestone_db TO milestone_readonly;

-- Grant usage on schema
GRANT USAGE ON SCHEMA public TO milestone_readonly;

-- Grant select on all existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO milestone_readonly;

-- Grant select on future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO milestone_readonly;

-- Grant select on all sequences
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO milestone_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO milestone_readonly;
```

## Step 5: Connect DBeaver to Your Database

### For Admin User (Full Access):

1. Open DBeaver
2. Click "New Database Connection"
3. Select "PostgreSQL"
4. Enter connection details from Render:
   - **Host**: (from Render dashboard)
   - **Port**: `5432`
   - **Database**: `milestone_db`
   - **Username**: `milestone_admin`
   - **Password**: (from Render dashboard)
5. Click "Test Connection"
6. Click "Finish"

### For Read-Only User:

1. Open DBeaver
2. Click "New Database Connection"
3. Select "PostgreSQL"
4. Enter connection details:
   - **Host**: (same as admin)
   - **Port**: `5432`
   - **Database**: `milestone_db`
   - **Username**: `milestone_readonly`
   - **Password**: (the password you set in Step 4)
5. Click "Test Connection"
6. Click "Finish"

## Step 6: Verify Your Deployment

1. Visit your app URL (provided by Render, e.g., `https://milestone-app.onrender.com`)

2. You should see the login page

3. Log in with the test credentials:
   - **Username**: `gowrisankar`
   - **Password**: `pass`

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify `render-build.sh` has execute permissions

### Database Connection Issues
- Verify the `DATABASE_URL` environment variable is set correctly
- Check that the database is running in Render dashboard
- Ensure your IP is not blocked (Render allows connections from anywhere by default)

### App Crashes on Startup
- Check the logs in Render dashboard
- Verify `gunicorn` is installed
- Ensure `app:app` points to your Flask app correctly

## Environment Variables

The following environment variables are automatically set by Render:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Auto-generated secret key for Flask sessions
- `FLASK_APP`: Set to `app.py`

## Database Users Summary

| User | Access Level | Use Case |
|------|-------------|----------|
| `milestone_admin` | Full access (read/write/delete) | Application runtime, migrations, admin tasks |
| `milestone_readonly` | Read-only access | Analytics, reporting, DBeaver queries |

## Security Notes

1. **Never commit passwords** to your repository
2. **Use strong passwords** for database users
3. **Rotate credentials** regularly
4. **Use environment variables** for sensitive data
5. **Enable SSL** for database connections in production

## Next Steps

- Set up monitoring and alerts in Render
- Configure custom domain (if needed)
- Set up automated backups
- Implement logging and error tracking
- Add CI/CD pipeline for automated deployments
