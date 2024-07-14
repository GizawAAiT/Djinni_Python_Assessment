from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from .. import schemas, services, utils
from ..database import get_db

router = APIRouter()

def token_authentication(token: str = Depends(utils.decode_jwt_token)):
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return token

@router.post("/addpost")
async def add_post(post: schemas.PostCreate, request: Request, db: Session = Depends(get_db), token: dict = Depends(token_authentication)):
    if len(post.text) > 1_000_000:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Payload too large")
    user_id = token.get("sub")  # extract user_id from token
    db_post = services.create_post(db, post, user_id)
    return {"postID": db_post.id}

@router.get("/getposts")
def get_posts(request: Request, db: Session = Depends(get_db), token: dict = Depends(token_authentication)):
    user_id = token.get("sub")  # extract user_id from token
    cache_key = f"posts_{user_id}"
    cached_data = request.app.state.cache.get(cache_key)
    if cached_data:
        return cached_data
    posts = services.get_user_posts(db, user_id)
    response = {"posts": posts}
    request.app.state.cache.set(cache_key, response, timeout=300)
    return response

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), token: dict = Depends(token_authentication)):
    services.delete_post(db, post_id)
    return {"detail": "Post deleted"}
