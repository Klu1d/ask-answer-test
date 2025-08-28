from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from app.infrastructure.persistence.config import PostgresConfig


def get_sessionmaker(psql_config: PostgresConfig) -> sessionmaker[Session]:
    engine = create_engine(
        psql_config.uri,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return sessionmaker(
        engine, 
        class_=Session, 
        autoflush=False, 
        expire_on_commit=False
    )