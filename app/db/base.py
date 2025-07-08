# Import all the models, so that Base has them before being imported by Alembic
from app.db.base_class import Base
from app.models.flashcard import Flashcard  # noqa

# Make sure all SQL Alchemy models are imported before initializing DB
# Otherwise, SQL Alchemy might fail to initialize relationships properly
# For more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28 