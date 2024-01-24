from App.buisness_logic import pasting, login, photo_upl, main_page, user_page, profile_connect
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Form, File, UploadFile, Depends, FastAPI
from Logic.jwt_op import verify_token
from App.models import Login

app = FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/user/login")
async def logn(log: Login):
    return login((log.login, log.password))


@app.post("/user/register")
async def register(log: str = Form(...), email: str = Form(...),
                   classroom: str = Form(...), decoded_token: dict = Depends(verify_token),
                   status: int = Form(...)):
    return pasting((log, email, classroom, decoded_token, status))


@app.post("/user/update")
async def update(decoded_token: dict = Depends(verify_token),
                 p1: UploadFile = File(None),
                 p2: UploadFile = File(None),
                 password: str = Form(None)):
    return photo_upl((p1, p2, {"cookie": decoded_token}, password))


@app.post("/user")
async def main(num: int, decoded_token: dict = Depends(verify_token)):
    return main_page(skip=num, user=decoded_token)


@app.get("/user/{user_id}")
async def user_by_id(user_id: int):
    return user_page(user_id)


@app.put("/user/register/confirm/{text}")
async def conf(text: str, password):
    return profile_connect(text, password)
