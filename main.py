from fastapi import Form, File, UploadFile, Depends, FastAPI
from models import Login
from buisness_logic import pasting, login, photo_upl, main_page
from jwt_op import verify_token

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
                 p2: UploadFile = File(None)):
    return photo_upl((p1, p2, {"cookie": decoded_token}))


@app.post("/user")
async def main(num: int):
    return main_page(num)
