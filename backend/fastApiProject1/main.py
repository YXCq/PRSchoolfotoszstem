from fastapi import FastAPI, Form, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from App.models import Login
from App.buisness_logic import pasting, login, photo_upl, main_page, user_page, profile_connect
from Logic.jwt_op import verify_token

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # Adjust with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["Content-Type"],
)

@app.post("/user/login")
async def user_login(log: Login):
    return login((log.login, log.password))

@app.post("/user/register")
async def user_register(log: str = Form(...), email: str = Form(...), classroom: str = Form(...)):
    return pasting((log, email, classroom))

@app.post("/user/update")
async def user_update(
    decoded_token: dict = Depends(verify_token),
    p1: UploadFile = File(None),
    p2: UploadFile = File(None),
    password: str = Form(None)
):
    return photo_upl((p1, p2, {"cookie": decoded_token}, password))

@app.post("/user")
async def users_main(num: int):
    return main_page(skip=num)

@app.get("/user/{user_id}")
async def users_by_id(user_id: int):
    return user_page(user_id)

@app.put("/user/register/confirm/{text}")
async def confirm_registration(text: str, password: str):
    return profile_connect(text, password)
