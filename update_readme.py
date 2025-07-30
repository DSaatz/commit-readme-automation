import requests
import os
import re
from datetime import datetime

USERNAME = "DSaatz"
TOKEN = os.getenv("GH_TOKEN")

PROFILE_REPO = "DSaatz/DSaatz"
README_FILE = "profile-repo/README.md"

EVENTS_API = f"https://api.github.com/users/{USERNAME}/events/public"
START_MARKER = "<!--RECENT_ACTIVITY_START-->"
END_MARKER = "<!--RECENT_ACTIVITY_END-->"

RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BLUE = "\033[94m"
GREY = "\033[90m"

def fetch_recent_commits():
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(EVENTS_API, headers=headers)
    response.raise_for_status()
    events = response.json()

    activities = []
    for event in events:
        if event["type"] == "PushEvent":
            repo_name = event["repo"]["name"]
            branch = event["payload"]["ref"].split("/")[-1]
            for commit in event["payload"]["commits"]:
                commit_id = commit["sha"][:7]
                commit_msg = commit["message"]
                formatted = (
                    f"{GREEN}[{repo_name}]{RESET} "
                    f"{CYAN}<{branch}>{RESET} "
                    f"{YELLOW}`{commit_id}`{RESET} "
                    f"{WHITE}{commit_msg}{RESET}"
                )
                activities.append(formatted)
                if len(activities) == 3:
                    return activities
    return activities

def format_terminal_block(lines):
    plain_lines = [re.sub(r"\033\[[0-9;]*m", "", line) for line in lines]
    content_width = max(len(line) for line in plain_lines)

    top = "┌" + "─" * (content_width + 2) + "┐"

    
    header_text = " Recent GitHub Activities "
    header = "│" + BLUE + header_text.ljust(content_width + 2) + RESET + "│"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    timestamp_line = "│" + GREY + f" Last updated: {timestamp}".ljust(content_width + 2) + RESET + "│"

    separator = "├" + "─" * (content_width + 2) + "┤"

    body = "\n".join(f"│ {line.ljust(content_width)} │" for line in lines)

    bottom = "└" + "─" * (content_width + 2) + "┘"

    return "\n".join([top, header, timestamp_line, separator, body, bottom])

def update_readme(activities):
    terminal_block = format_terminal_block(activities)
    new_section = f"{START_MARKER}\n```ansi\n{terminal_block}\n```\n{END_MARKER}"

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(f"{START_MARKER}[\\s\\S]*{END_MARKER}", new_section, content)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    commits = fetch_recent_commits()
    if commits:
        update_readme(commits)
