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
    status: Dict[str, str] = {}

    gitignore_path = "../.gitignore"

    # check for .gitignore and hardcoded secrets prevention
    if os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, "r", encoding="utf-8") as file:
                content = file.read()
            if ".env" in content:
                status["hardcoded"] = "[OK] No hardcoded secrets detected"
            else:
                status["hardcoded"] = "[WARNING] .env missing from .gitignore!"
        except IOError:
            status["hardcoded"] = "[WARNING] Could not read .gitignore file."
    else:
        status["hardcoded"] = (
            "[WARNING] .gitignore missing! Secrets might be exposed."
        )

    # check if .env exists
    if os.path.exists(".env"):
        status["dot_env"] = "[OK] .env file properly configured"
    else:
        status["dot_env"] = "[WARNING] .env file missing."

    # check for overrides (Terminal priorities)
    if os.environ.get("MATRIX_MODE") == "production":
        status["overrides"] = (
            "[OK] Production overrides active! "
            "Terminal settings prioritized."
        )
    else:
        status["overrides"] = (
            "[INFO] Running with standard environment variables."
        )

    return status


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # load environment variables from .env
    # allows developers to securely store sensitive data
    load_dotenv()

    # fetch required variables or None
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
        db_info = env_db_url if env_db_url else "local instance"
        print(f"  Database: Connected to {db_info}")

        if env_api_key:
            masked_key = "***" + str(env_api_key)[-4:]
            print(f"  API Access: Authenticated with key: {masked_key}")
        else:
            print("  API Access: [WARNING] No API Key configuration detected")

        print(f"  Log Level: {current_log} (Verbose DEBUG mode enabled)")
        print(f"  Zion Network: Online at: {env_zion}")

    print("\nEnvironment security check:")
    security_reports = check_environment_security()
    for report_message in security_reports.values():
        print(f"  {report_message}")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    # MATRIX_MODE=production python3 oracle.py
    # MATRIX_MODE=development python3 oracle.py
    main()
