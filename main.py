from API_FUNCIONES import PlayTimeGenre
from API_FUNCIONES import UserForGenre
from API_FUNCIONES import UsersRecommend
from API_FUNCIONES import UsersWorstDeveloper
from fastapi import FastAPI
app= FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.get("/PlayTimeGenre/{genre}")
async def user(genre: str):
    try:
        result = PlayTimeGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/UserForGenre/{genre}")
async def user(genre: str):
    try:
        result = UserForGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/UsersRecommend/{year}")
async def user(year: int):
    try: 
        result = UsersRecommend(year)
        return result
    except Exception as e:
        return {"error": str(e)}
    
    
@app.get("/UsersWorstDeveloper/{year}")
async def user(year: int):
    try:
        result = UsersWorstDeveloper(year)
        return result
    except Exception as e:
        return {"error": str(e)}
    
    
    
