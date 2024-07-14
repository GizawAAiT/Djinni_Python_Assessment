from fastapi import FastAPI
from .routers import auth, posts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = "mysql+pymysql://user:password@localhost/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
app.include_router(auth.router, prefix="/auth")
app.include_router(posts.router, prefix="/posts")

# Cache setup (if necessary)
app.state.cache = {}  # Simple in-memory cache for example purposes
