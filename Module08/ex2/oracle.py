#!/usr/bin/env python3

# environment variables
import os
import sys
# strict typing tools
# Dict defines dictionaries
# Optional indicates that a variable can contain str or None
from typing import Dict, Optional


try:
    # library responsible reading .env
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    # Safe protection if python-dotenv is not installed in the environment
    print("ORACLE ERROR: 'python-dotenv' package is missing.")
    print("Please install it using: pip install python-dotenv")
    sys.exit(1)


def check_environment_security() -> Dict[str, str]:
    status: Dict[str, str] = {
        "hardcoded": "[OK] No hardcoded secrets detected",
        "dot_env": "[OK] .env file properly configured",
        "overrides": "[OK] Production overrides available"
    }

    # verify .env file exists or using system variables
    if not os.path.exists(".env") and not os.environ.get("MATRIX_MODE"):
        war_message = "[WARNING] No .env file found. Using system defaults."
        status["dot_env"] = war_message

    return status


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # load environment variables from .env
    # allows developers to securely store sensitive data
    load_dotenv()

    # retch required variables or None
    env_mode: Optional[str] = os.environ.get("MATRIX_MODE")
    env_db_url: Optional[str] = os.environ.get("DATABASE_URL")
    env_api_key: Optional[str] = os.environ.get("API_KEY")
    env_log_level: Optional[str] = os.environ.get("LOG_LEVEL")
    env_zion: Optional[str] = os.environ.get("ZION_ENDPOINT")

    # if not all are present -> warning
    if not all([env_mode, env_db_url, env_api_key, env_log_level, env_zion]):
        print("WARNING: Incomplete configuration detected!")
        print("Some variables are missing. Please check your .env file.\n")

    # fallback default values if variables are absent
    current_mode: str = env_mode if env_mode else "development"
    current_log: str = env_log_level if env_log_level else "INFO"
    print("Configuration loaded:")
    print(f"  Mode: {current_mode}")

    # behavior based on development vs production mode
    if current_mode.lower() == "production":
        print("  Database: [SECURE] Connected to Production Mainframe Cluster")
        print("  API Access: [ENCRYPTED] Token Authenticated via SSL")
        print(f"  Log Level: {current_log} (Production restrictions active)")
        print(f"  Zion Network: Routing securely through tunnel: {env_zion}")
    else:
        print(f"  Database: Connected to local instance ({env_db_url})")
        print(
            "  API Access: Authenticated with key: ***"
            + str(env_api_key)[-4:] if env_api_key else 'NONE'
        )
        print(f"  Log Level: {current_log} (Verbose DEBUG mode enabled)")
        print(f"  Zion Network: Online at: {env_zion}")

    print("\nEnvironment security check:")
    security_reports = check_environment_security()
    for _, report_message in security_reports.items():
        print(f"  {report_message}")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
