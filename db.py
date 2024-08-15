from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DB_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_table(columns):
    metadata = MetaData()
    columns_dict = {col: None for col in columns}
    columns_dict['Technology Company'] = None  # Additional column

    # Create table definition
    from sqlalchemy import Table, Column, String
    table = Table(
        'companies',
        metadata,
        *[Column(col, String) for col in columns_dict],
    )

    # Create table in the database
    metadata.create_all(bind=engine)
