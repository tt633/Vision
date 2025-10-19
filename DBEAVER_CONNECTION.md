# DBeaver Connection Guide

## Quick Setup for Two Users

### 1. Admin User (Full Access)
**Use this for:** Application management, running migrations, modifying data

**Connection Details:**
- **Connection Type**: PostgreSQL
- **Host**: `<from Render dashboard>`
- **Port**: `5432`
- **Database**: `milestone_db`
- **Username**: `milestone_admin`
- **Password**: `<from Render dashboard>`
- **SSL Mode**: Require (or Prefer)

**Permissions:**
- ✅ Read (SELECT)
- ✅ Write (INSERT, UPDATE)
- ✅ Delete (DELETE)
- ✅ Create/Drop tables
- ✅ Create/Drop indexes
- ✅ Manage users

---

### 2. Read-Only User (Query Access)
**Use this for:** Analytics, reporting, safe data exploration

**Connection Details:**
- **Connection Type**: PostgreSQL
- **Host**: `<same as admin>`
- **Port**: `5432`
- **Database**: `milestone_db`
- **Username**: `milestone_readonly`
- **Password**: `<password you set>`
- **SSL Mode**: Require (or Prefer)

**Permissions:**
- ✅ Read (SELECT)
- ❌ Write (INSERT, UPDATE)
- ❌ Delete (DELETE)
- ❌ Create/Drop tables
- ❌ Create/Drop indexes
- ❌ Manage users

---

## Step-by-Step DBeaver Setup

### Step 1: Open DBeaver
1. Launch DBeaver application
2. Click on **Database** → **New Database Connection**
3. Or click the plug icon (🔌) in the toolbar

### Step 2: Select Database Type
1. Choose **PostgreSQL**
2. Click **Next**

### Step 3: Configure Connection (Admin)
1. **Main** tab:
   - Host: `<your-render-hostname>`
   - Port: `5432`
   - Database: `milestone_db`
   - Username: `milestone_admin`
   - Password: `<from Render>`
   
2. **SSL** tab:
   - SSL Mode: `require` or `prefer`
   - Check "Use SSL"

3. Click **Test Connection**
   - If prompted, download PostgreSQL driver
   - Should see "Connected" message

4. Click **Finish**

### Step 4: Configure Connection (Read-Only)
Repeat Step 3 but use:
- Username: `milestone_readonly`
- Password: `<your chosen password>`

---

## Getting Connection Details from Render

1. Go to https://dashboard.render.com
2. Click on your **milestone-db** database
3. Click on **Info** tab
4. Copy the **External Database URL** or individual connection details:
   ```
   postgres://milestone_admin:PASSWORD@HOST:5432/milestone_db
   ```
   
   Extract:
   - **Host**: The part after `@` and before `:5432`
   - **Password**: The part between `:` and `@`

---

## Testing Your Connections

### Test Admin Connection:
```sql
-- Should work (read)
SELECT * FROM users LIMIT 5;

-- Should work (write)
INSERT INTO users (username, email, password_hash) 
VALUES ('test_user', 'test@example.com', 'hash123');

-- Should work (delete)
DELETE FROM users WHERE username = 'test_user';
```

### Test Read-Only Connection:
```sql
-- Should work (read)
SELECT * FROM users LIMIT 5;
SELECT * FROM goals;
SELECT * FROM transactions;

-- Should FAIL (write)
INSERT INTO users (username, email, password_hash) 
VALUES ('test_user', 'test@example.com', 'hash123');
-- Error: permission denied for table users

-- Should FAIL (delete)
DELETE FROM users WHERE id = 1;
-- Error: permission denied for table users
```

---

## Useful Queries

### View All Tables:
```sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

### View All Users and Their Goals:
```sql
SELECT u.username, g.name as goal_name, g.target_amount, g.current_amount
FROM users u
LEFT JOIN goals g ON u.id = g.user_id
ORDER BY u.username, g.name;
```

### View Savings Rules:
```sql
SELECT u.username, g.name as goal_name, sr.rule_name, sr.rule_type, sr.amount
FROM savings_rules sr
JOIN users u ON sr.user_id = u.id
JOIN goals g ON sr.goal_id = g.id
ORDER BY u.username, g.name;
```

### View Transactions:
```sql
SELECT t.created_at, u.username, g.name as goal_name, 
       t.transaction_type, t.amount, t.description
FROM transactions t
JOIN users u ON t.user_id = u.id
JOIN goals g ON t.goal_id = g.id
ORDER BY t.created_at DESC
LIMIT 20;
```

### Check User Permissions:
```sql
-- Run as admin to see what milestone_readonly can do
SELECT grantee, privilege_type 
FROM information_schema.role_table_grants 
WHERE grantee = 'milestone_readonly';
```

---

## Troubleshooting

### Cannot Connect
- ✅ Verify hostname and port are correct
- ✅ Check that password doesn't have special characters that need escaping
- ✅ Ensure SSL mode is set correctly
- ✅ Verify database name is `milestone_db`
- ✅ Check firewall settings

### "Permission Denied" Errors
- If using **milestone_readonly**: This is expected for INSERT/UPDATE/DELETE
- If using **milestone_admin**: Check that user was created correctly

### SSL Connection Issues
- Try changing SSL mode from "require" to "prefer"
- Or try "disable" for testing (not recommended for production)

### Driver Issues
- DBeaver will prompt to download PostgreSQL driver
- Click "Download" when prompted
- If it fails, manually download from DBeaver settings

---

## Security Best Practices

1. **Use milestone_readonly for daily queries** - Prevents accidental data modification
2. **Use milestone_admin only when needed** - For migrations, data fixes, admin tasks
3. **Never share passwords** - Each person should have their own credentials
4. **Use strong passwords** - At least 16 characters, mix of letters, numbers, symbols
5. **Enable SSL** - Always use encrypted connections
6. **Rotate passwords regularly** - Change passwords every 90 days
7. **Monitor access logs** - Check who's accessing the database

---

## Quick Reference

| Task | User to Use |
|------|-------------|
| View data / Run reports | `milestone_readonly` |
| Debug issues | `milestone_readonly` |
| Export data | `milestone_readonly` |
| Add/modify data | `milestone_admin` |
| Run migrations | `milestone_admin` |
| Create tables | `milestone_admin` |
| Delete data | `milestone_admin` |
| Manage users | `milestone_admin` |
