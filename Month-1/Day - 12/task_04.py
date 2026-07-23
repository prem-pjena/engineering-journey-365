# Task 4: Git Workflow Simulation (Conceptual)

"""
This script demonstrates the Git workflow learned:
1. git init — creates a hidden .git folder
2. git status — shows current repository state
3. git add — stages files for commit
4. git commit — creates a checkpoint
5. git log — shows commit history
6. HEAD — pointer to latest commit

Note: This is a simulation. Run actual commands in terminal.
"""

import os
import subprocess

def run_git_command(command: str) -> str:
    """Run a git command and return output."""
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        return result.stdout or result.stderr
    except FileNotFoundError:
        return "Git not installed. Install git to run this."


if __name__ == "__main__":
    print("=== Git Status Demo ===")
    print(run_git_command("git status"))
    print("\n=== Git Log ===")
    print(run_git_command("git log --oneline -5"))
