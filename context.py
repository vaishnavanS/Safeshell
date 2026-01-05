import os
import subprocess
import getpass

def get_context():
    """
    Gathers system context info for command validation.
    """
    context = {
        "cwd": os.getcwd(),
        "user": getpass.getuser(),
        "git_branch": None,
        "is_git_repo": False,
        "platform": os.name, # 'nt' for Windows, 'posix' for Linux/Mac
    }

    # Check for Git info
    try:
        # Check if it's a git repo
        is_repo = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, check=False
        )
        if is_repo.returncode == 0:
            context["is_git_repo"] = True
            # Get current branch
            branch = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True, text=True, check=False
            )
            context["git_branch"] = branch.stdout.strip()
    except Exception:
        pass

    return context

if __name__ == "__main__":
    import json
    print(json.dumps(get_context(), indent=2))
