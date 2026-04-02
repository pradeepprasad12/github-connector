import requests
from app.config import GITHUB_TOKEN, BASE_URL

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def handle_github_error(res):
    if res.status_code == 401:
        raise Exception("Unauthorized: Invalid GitHub Token")
    elif res.status_code == 403:
        raise Exception("Forbidden: You don’t have permission")
    elif res.status_code == 404:
        raise Exception("Not Found: Repo or user does not exist")
    elif res.status_code == 422:
        raise Exception("Validation Failed: Check your input data")
    else:
        raise Exception(f"GitHub Error: {res.text}")


def get_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        handle_github_error(res)

    return res.json()


def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    payload = {
        "title": title,
        "body": body
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 201:
        handle_github_error(res)

    return res.json()


def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        handle_github_error(res)

    return res.json()


def create_pull_request(owner, repo, title, body, head, base):
    url = f"{BASE_URL}/repos/{owner}/{repo}/pulls"

    payload = {
        "title": title,
        "body": body,
        "head": head,
        "base": base
    }

    res = requests.post(url, json=payload, headers=headers)

    if res.status_code != 201:
        handle_github_error(res)

    return res.json()


def get_commits(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        handle_github_error(res)

    data = res.json()

    # Clean response
    return [
        {
            "sha": c["sha"],
            "author": c["commit"]["author"]["name"],
            "message": c["commit"]["message"],
            "date": c["commit"]["author"]["date"]
        }
        for c in data
    ]