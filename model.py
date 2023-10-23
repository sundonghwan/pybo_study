from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# question 모델 정의 Author: 선동환 modify: 2023-10-23
class Question(Base):
    """
        사용자의 질문시 필요한 값이 정의된 모델
        nullable의 True인 경우 null값을 허용 False 인경우 null을 허용하지 않음

        author: 선동환
        modify: 2023-10-23
    """
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

# Answer 모델 정의 Author: 선동환 modify: 2023-10-23
class Answer(Base):
    """
        사용자 질문에 대한 답변 모델
        question 모델과 관계를 맺음

        author: 선동환
        modify: 2023-10-23
    """
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    # backref는 역참조를 하기위해 사용 Author: 선동환 Modify: 2023-10-23
    question = relationship("Question", backref="answers")

