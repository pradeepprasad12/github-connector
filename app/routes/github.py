from fastapi import APIRouter, HTTPException
from app.models.schemas import Issue, PullRequest

from app.services.github_service import (
    get_repos,
    create_issue,
    list_issues,
    create_pull_request,
    get_commits
)

router = APIRouter()


@router.get("/repos/{username}")
def fetch_repos(username: str):
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")

    try:
        return get_repos(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/issues/{owner}/{repo}")
def fetch_issues(owner: str, repo: str):
    try:
        return list_issues(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-issue")
def make_issue(issue: Issue):
    try:
        return create_issue(
            issue.owner,
            issue.repo,
            issue.title,
            issue.body
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-pr")
def make_pr(pr: PullRequest):
    try:
        return create_pull_request(
            pr.owner,
            pr.repo,
            pr.title,
            pr.body,
            pr.head,
            pr.base
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/commits/{owner}/{repo}")
def fetch_commits(owner: str, repo: str):
    try:
        return get_commits(owner, repo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))