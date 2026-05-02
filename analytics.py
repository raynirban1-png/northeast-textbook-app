import sqlite3
from datetime import datetime

conn = sqlite3.connect("analytics.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    section TEXT,
    unit TEXT,
    topic TEXT
)
""")
conn.commit()

def log_usage(section, unit=None, topic=None):
    cursor.execute(
        "INSERT INTO usage (timestamp, section, unit, topic) VALUES (?, ?, ?, ?)",
        (datetime.now().isoformat(), section, unit, topic)
    )
    conn.commit()