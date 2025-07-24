from pathlib import Path
from datetime import datetime

LATEST_TIMESTAMP_PATH = Path("data_output/latest_timestamp_seen.txt")


def read_latest_timestamp():
    try:
        return LATEST_TIMESTAMP_PATH.read_text().strip()
    except FileNotFoundError:
        return None


def to_dt_obj(ts_str):
    try:
        ts_str = ts_str.rstrip("Z")
        return datetime.strptime(ts_str, "%Y%m%dT%H%M%S")
    except Exception:
        return None


def write_latest_timestamp(timestamp):
    Path("data_output").mkdir(parents=True, exist_ok=True)
    try:
        LATEST_TIMESTAMP_PATH.write_text(timestamp)
        print(f"📝 Updated latest timestamp file: {timestamp}")
    except Exception as e:
        print(f"❌ Failed to write latest timestamp: {e}")


LATEST_TIMESTAMP = to_dt_obj(read_latest_timestamp())
