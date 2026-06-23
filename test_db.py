from sqlalchemy import text
from app.core.database import engine

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("Database connected successfully!")
except Exception as e:
    print("Connection failed")
    print(e)