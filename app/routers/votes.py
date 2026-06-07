from fastapi import FastAPI,status,Response,HTTPException,Depends,APIRouter
from app import models,schemas,oauth2,database
from sqlalchemy.orm import Session

router = APIRouter(prefix = "/vote", tags = ["Vote"])

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote : schemas.Vote, db:Session=Depends(database.get_db), current_user: int=Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    query_vote = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.user_id==current_user.id)
    found_vote = query_vote.first()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'post number {vote.post_id} is already voted by user {current_user.id}')
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message : voted successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="voted does not exist")
        query_vote.delete(synchronize_session=False)
        db.commit()
        return {"message : vote deleted successfully"}
    



