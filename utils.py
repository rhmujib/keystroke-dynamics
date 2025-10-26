"""
Utility Functions
"""

import os
import json

def ensure_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def load_config(config_path):
    """Load configuration from JSON file"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Config file not found: {config_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in config file: {config_path}")
        exit(1)

def print_banner():
    """Print application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║        ⌨️  KEYSTROKE DYNAMICS ANALYZER  ⌨️           ║
    ║                                                      ║
    ║     Privacy-Respecting | Ethical Use Only           ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)