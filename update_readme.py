import requests
import os
import re
from datetime import datetime

USERNAME = os.getenv("GH_USERNAME")
TOKEN = os.getenv("GH_TOKEN")

PROFILE_REPO = USERNAME + "/" + USERNAME
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
                formatted = f"[{repo_name}] <{branch}> `{commit_id}` {commit_msg}"
                activities.append(formatted)
                if len(activities) == 3:
                    return activities
    return activities

def format_terminal_block(lines):
    content_width = max(len(line) for line in lines)

    top = "┌" + "─" * (content_width + 2) + "┐"
    header_text = " Recent GitHub Activities "
    header = "│" + header_text.ljust(content_width + 2) + "│"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    timestamp_line = "│" + f" Last updated: {timestamp}".ljust(content_width + 2) + "│"

    separator = "├" + "─" * (content_width + 2) + "┤"

    body = "\n".join(f"│ {line.ljust(content_width)} │" for line in lines)

    bottom = "└" + "─" * (content_width + 2) + "┘"

    return "\n".join([top, header, timestamp_line, separator, body, bottom])

def update_readme(activities):
    terminal_block = format_terminal_block(activities)
    new_section = f"{START_MARKER}\n```text\n{terminal_block}\n```\n{END_MARKER}"

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(f"{START_MARKER}[\\s\\S]*{END_MARKER}", new_section, content)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    commits = fetch_recent_commits()
    if commits:
        update_readme(commits)