from cars_api import models
from cars_api.database import engine


def init_db():
    models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
