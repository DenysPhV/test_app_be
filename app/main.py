from fastapi import FastAPI
from app.controllers import auth, posts, users


app = FastAPI()

# Подключаем роутеры для различных эндпоинтов
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
