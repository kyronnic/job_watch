import subprocess
import os
from typing import Optional

from dotenv import load_dotenv

def get_api_key() -> Optional[str]:
    load_dotenv()
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", "Gmail PS Emailer App", "-a",
             os.getenv('gmail_user'), "-w"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error retrieving API key: {e}")
        return None

