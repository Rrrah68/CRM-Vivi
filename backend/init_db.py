from app.database.database import engine

from app.models.base import Base

import app.models.buyer
import app.models.conversation
import app.models.message

Base.metadata.create_all(bind=engine)

print("Database initialized.")
