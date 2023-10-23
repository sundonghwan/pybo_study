from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router
app = FastAPI()

# cors 설정 Author: 선동환 modify: 2023-10-23
origins = ["http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# question router 추가 Author: 선동환 modify: 2023-10-23
app.include_router(question_router.router)
