from pydantic import BaseModel, Field


class Issue(BaseModel):
    owner: str = Field(..., min_length=1)
    repo: str = Field(..., min_length=1)
    title: str = Field(..., min_length=3)
    body: str = Field(..., min_length=5)


class PullRequest(BaseModel):
    owner: str = Field(..., min_length=1)
    repo: str = Field(..., min_length=1)
    title: str = Field(..., min_length=2)
    body: str = Field(..., min_length=2)
    head: str = Field(..., min_length=1)
    base: str = Field(..., min_length=1)