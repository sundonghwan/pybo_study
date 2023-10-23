import datetime

from pydantic import BaseModel

# 데이터 검증을 위한 Question 스키마 모델 정의 Author: 선동환 Modify: 2023-10-24
class Question(BaseModel):
    """
        4개 항목 모두 필수 항목이라 따로 추가작업 x
        만약 필수 항목이 아닌경우
        "subject: str | None = None" 와 같은 예제로 선언 가능
        -> subject 항목은 문자열 타입이며 None값이 기본값이고 None을 가질수 있음이란 뜻

    """
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
