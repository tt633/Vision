# 🎯 Milestone Savings App

A Flask-based web application for managing savings goals with automated savings rules, habit rewards, and progress tracking.

## Features

- 💰 **Multiple Savings Goals** - Create and track multiple financial goals
- 📊 **Progress Tracking** - Visual progress bars and statistics
- 🎯 **Savings Rules** - Automate your savings with:
  - **Recurring Deposits** - Regular automatic contributions
  - **Habit Rewards** - Save when you complete healthy habits
  - **Guilty Pleasure Tax** - Add a tax to indulgent purchases
- 🚀 **Savings Pace** - Choose your speed: Conservative, Moderate, or Aggressive
- 📱 **Modern UI** - Beautiful, responsive dashboard

## Tech Stack

- **Backend**: Flask 3.0.0
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Migrations**: Flask-Migrate
- **Deployment**: Render
- **Server**: Gunicorn

## Local Development

### Prerequisites

- Python 3.9+
- pip
- virtualenv (recommended)

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd milestone-app
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.flaskenv` file:
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///local.db
SECRET_KEY=your-secret-key-here
```

5. **Initialize database**
```bash
python seeds.py
```

6. **Run the application**
```bash
flask run --debug
```

7. **Access the app**
Open http://127.0.0.1:5000 in your browser

### Default Login Credentials

- **Username**: `gowrisankar`
- **Password**: `pass`

## Deployment to Render

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

Quick steps:
1. Push code to GitHub
2. Connect repository to Render
3. Render will auto-detect `render.yaml` and deploy
4. Set up database users (see DEPLOYMENT.md)

## Database Setup

### Two User Types

1. **Admin User** (`milestone_admin`)
   - Full read/write access
   - Used by the application
   - Can modify schema

2. **Read-Only User** (`milestone_readonly`)
   - Read-only access
   - For analytics and reporting
   - Safe for data exploration

See [DBEAVER_CONNECTION.md](DBEAVER_CONNECTION.md) for DBeaver setup instructions.

## Project Structure

```
milestone-app/
├── app.py                  # Main Flask application
├── models.py               # Database models
├── config.py               # Configuration settings
├── seeds.py                # Database seeding script
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment config
├── render-build.sh        # Build script for Render
├── templates/
│   └── index.html         # Dashboard UI
├── instance/              # Local database files (gitignored)
├── migrations/            # Database migrations (auto-generated)
└── README.md             # This file
```

## API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /logout` - Logout

### Goals
- `GET /api/goals` - List all goals
- `POST /api/goals/create` - Create new goal

### Rules
- `GET /api/savings-rules` - List all savings rules
- `POST /api/rules/create` - Create new rule

### Transactions
- `GET /api/transactions` - List transactions
- `POST /api/expense` - Log an expense with round-up
- `POST /api/frugality` - Log frugality savings
- `POST /api/habit/<rule_id>/log` - Log habit completion

## Database Schema

### Users
- `id`, `username`, `email`, `password_hash`

### Goals
- `id`, `user_id`, `name`, `target_amount`, `current_amount`, `savings_pace`, `description`, `image_url`

### Savings Rules
- `id`, `user_id`, `goal_id`, `rule_type`, `rule_name`, `amount`, `frequency`, `trigger_category`

### Transactions
- `id`, `user_id`, `goal_id`, `amount`, `transaction_type`, `description`, `original_expense_amount`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_APP` | Flask application entry point | `app.py` |
| `FLASK_ENV` | Environment (development/production) | `development` |
| `DATABASE_URL` | Database connection string | `sqlite:///local.db` |
| `SECRET_KEY` | Flask session secret key | `dev-secret` |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- Never commit `.env` or `.flaskenv` files with real credentials
- Use strong passwords for production databases
- Rotate `SECRET_KEY` regularly
- Enable SSL for database connections in production
- Use environment variables for sensitive data

## Troubleshooting

### Database Connection Issues
- Verify `DATABASE_URL` is set correctly
- Check database is running
- Ensure credentials are correct

### Login Not Working
- Clear browser cache
- Check database has seeded users
- Verify password hashing is working

### Build Fails on Render
- Check build logs in Render dashboard
- Verify `render-build.sh` has execute permissions
- Ensure all dependencies are in `requirements.txt`

## License

MIT License - feel free to use this project for learning or personal use.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review [DEPLOYMENT.md](DEPLOYMENT.md)
3. Check [DBEAVER_CONNECTION.md](DBEAVER_CONNECTION.md)
4. Open an issue on GitHub

## Roadmap

- [ ] Add expense tracking integration
- [ ] Implement email notifications
- [ ] Add goal completion celebrations
- [ ] Create mobile app
- [ ] Add social features (share goals)
- [ ] Implement budgeting tools
- [ ] Add data export functionality
- [ ] Create admin dashboard

---

Made with ❤️ for better financial habits
