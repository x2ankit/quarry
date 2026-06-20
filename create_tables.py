from app.db.database import Base, engine
from app.models.user import User
from app.models.document import Document
from app.models.chunk import Chunk

def main():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    main()
