# FastAPI Web Application

## Setup

1. Install dependencies:
pip install -r requirements.txt


2. Run the application:
uvicorn app.main

--reload


## Endpoints

- **Signup**: `/auth/signup` - POST request with `email` and `password`.
- **Login**: `/auth/login` - POST request with `email` and `password`.
- **Add Post**: `/posts/addpost` - POST request with `text` and `token`.
- **Get Posts**: `/posts/getposts` - GET request with `token`.
- **Delete Post**: `/posts/deletepost/{post_id}` - DELETE request with `post_id` and `token`.
