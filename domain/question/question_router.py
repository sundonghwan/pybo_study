from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from model import Question
from domain.question import question_schema, question_crud
# question router 정의 Author: 선동환 modify: 2023-10-23
router = APIRouter(
    prefix="/api/question"
)

# question 전체 목록
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)

    return _question_list
