# Task 6: Virtual Environment Setup Script

"""
This script demonstrates why virtual environments matter for AI projects.

Purpose:
- Each project gets isolated dependencies
- Prevents version conflicts between projects
- Essential for AI/ML projects with different library versions

Commands to run in terminal (not in Python):
    python3 -m venv venv          # Create virtual environment
    source venv/bin/activate      # Activate it (macOS/Linux)
    pip install requests          # Install packages in isolation
    pip freeze > requirements.txt # Save dependencies
    deactivate                    # Exit virtual environment
"""

import subprocess
import sys


def check_pip_packages() -> list[str]:
    """List currently installed packages."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=columns"],
        capture_output=True, text=True
    )
    return result.stdout.split('\n')[2:]  # Skip header lines


if __name__ == "__main__":
    print("=== Installed Python Packages ===")
    packages = check_pip_packages()
    for pkg in packages:
        if pkg.strip():
            print(pkg)
    print(f"\nTotal: {len([p for p in packages if p.strip()])} packages")
    
    print("\n--- How to create a virtual environment ---")
    print("python3 -m venv venv")
    print("source venv/bin/activate")
    print("pip install fastapi uvicorn")
    print("pip freeze > requirements.txt")
