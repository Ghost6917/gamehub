from typing import NewType, Literal, TypedDict, List

PostID = NewType("PostID", str)

class Comment(TypedDict):
    author: str
    likes: List[str]
    content: str
    epoch: float
    id: PostID

Argon2Hash = NewType("Argon2Hash", str)
AccountType = Literal["user", "admin", "owner", "developer"]