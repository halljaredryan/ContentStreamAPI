# FastAPI Media Feed

A FastAPI-based REST API for uploading and managing media posts (images and videos). The application integrates with ImageKit for media hosting and uses SQLite with async SQLAlchemy for data persistence.

## Features

- **Media Upload**: Upload images and videos with optional captions
- **Feed Endpoint**: Retrieve all posts in reverse chronological order
- **Post Management**: Delete posts by ID
- **ImageKit Integration**: Automatic media hosting and CDN delivery

## Tech Stack

- FastAPI
- SQLAlchemy (async) with SQLite
- ImageKit.io for media hosting
- Uvicorn ASGI server

## API Endpoints

- `POST /upload` - Upload a media file with an optional caption
- `GET /feed` - Get all posts ordered by creation date (newest first)
- `DELETE /posts/{post_id}` - Delete a post by ID


