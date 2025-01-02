from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import List, Dict
class Memo(BaseModel):
    id: int
    content: str

app = FastAPI()

memos = []

@app.get("/api/memos")
async def get_memo(sort: str, by: str) :
    arr = []
    if sort == "asc":
        if by == "alphabet": 
            # 'content' 기준 오름차순 정렬
            arr = sorted(memos, key=lambda x: x.content)
            
        elif by == "created":
            # 'id' 기준 오름차순 정렬
            arr = sorted(memos, key=lambda x: x.id)
            

    elif sort == "desc":
        if by == "alphabet":
            # 'content' 기준 내림차순 정렬
            arr = sorted(memos, key=lambda x: x.content, reverse=True)
            
        elif by == "created":
            # 'id' 기준 내림차순 정렬
            arr = sorted(memos, key=lambda x: x.id, reverse=True)
            
    
    return arr


@app.post("/api/memos")
async def create_memo(memo: Memo):
    memos.append(memo)
    return "메모 추가 성공"

@app.put("/api/memos/{memo_id}")
async def update_memo(memo: Memo):
    for m in memos:
        if m.id == memo.id:
            m.content = memo.content
            return "메모 수정 성공"
    return "메모 수정 실패."

@app.delete("/api/memos/{memo_id}")
async def delete_memo(memo_id: int):
    for i, m in enumerate(memos):
        if m.id == memo_id:
            del memos[i]
            return "메모 삭제 성공"
    return "메모 삭제 실패."

app.mount("/", StaticFiles(directory="static", html=True), name="static")

from typing import List
class Me:
    name: str
    age: int
    hooby: List[str]
    
    def introduce(self):
        return f"안녕하세요. 저는 {self.name}입니다. {self.age}살이고, 취미는 {', '.join(self.hobby)}입니다."
    
    
me = Me()
me.name = "chanjoo"
me.age = 34
me.hobby = ["soccer", "game"]
me.introduce()
