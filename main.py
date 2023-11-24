from fastapi import Form, File, UploadFile, Depends, FastAPI
from models import Login, User
from buisness_logic import pasting, login, photo_upl, main_page, user_page
from jwt_op import verify_token
from init.settings import session

app = FastAPI()


@app.post("/user/login")
async def logn(log: Login):
    return login((log.login, log.password))


@app.post("/user/register")
async def register(log: str = Form(...), email: str = Form(...),
                   password: str = Form(...), classroom: str = Form(...)):
    return pasting((log, email, password, classroom))


@app.post("/user/update")
async def update(decoded_token: dict = Depends(verify_token),
                 p1: UploadFile = File(None),
                 p2: UploadFile = File(None),
                 password: str = Form(None)):
    return photo_upl((p1, p2, {"cookie": decoded_token}, password))


@app.post("/user")
async def main(num: int):
    return main_page(num)


@app.get("/user/{user_id}")
async def user_by_id(user_id: int):
    return user_page(user_id)
