import os
from decimal import Decimal


class Config:
    # Database: Render will inject DATABASE_URL (use SSL mode if required)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Round-up configuration
    # mode: 'fixed' => always add FIXED_ROUND_UP_STEP
    # 'to_next_dollar' => ceil(expense) - expense (min floor applied)
    ROUND_UP_MODE = os.environ.get("ROUND_UP_MODE", "fixed")
    FIXED_ROUND_UP_STEP = Decimal(os.environ.get("FIXED_ROUND_UP_STEP", "0.50"))
    MIN_ROUND_UP_FLOOR = Decimal(os.environ.get("MIN_ROUND_UP_FLOOR", "0.00"))

    # Pace bonus mapping (Conservative/Moderate/Aggressive)
    PACE_BONUS = {
        "Conservative": Decimal(os.environ.get("PACE_BONUS_CONSERVATIVE", "0.50")),
        "Moderate": Decimal(os.environ.get("PACE_BONUS_MODERATE", "1.00")),
        "Aggressive": Decimal(os.environ.get("PACE_BONUS_AGGRESSIVE", "1.50")),
    }

    # Security (simple demo)
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")