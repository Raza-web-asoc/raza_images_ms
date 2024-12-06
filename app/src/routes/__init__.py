from .user import router as users_router
from .dog import router as dogs_router
from .post import router as posts_router

__all__ = ["dogs_router", "users_router", "posts_router"]