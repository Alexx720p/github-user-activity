import requests
import sys

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for user {username}")
        return None

def display_activity(activity):
    if activity:
        for event in activity:
            event_type = event.get("type")
            repo_name = event.get("repo", {}).get("name")
            print(f"{event_type} in {repo_name}")
    else:
        print("No activity found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github_activity_tracker.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    activity = fetch_github_activity(username)
    display_activity(activity)
