from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from model import Question

# question router 정의 Author: 선동환 modify: 2023-10-23
router = APIRouter(
    prefix="/api/question"
)

# question 전체 목록
@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()

    return _question_list
