from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from db import engine


class OpenSession:
    def __enter__(self):
        self.session = sessionmaker(bind=engine, autoflush=True)()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()

