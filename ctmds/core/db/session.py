from typing import Iterator, Protocol

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ctmds.core.db.base import Base


class SessionStream(Protocol):
    """Protocol for a session stream."""

    def __call__(
        self,
    ) -> Iterator[Session]: ...


# Create SQLite engine
engine = create_engine(
    "sqlite:///ctmds.db",
    echo=False,
)

# Create sessionmaker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_session() -> Iterator[Session]:
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Initialize database tables."""
    Base.metadata.create_all(bind=engine)


def teardown_db() -> None:
    """Teardown database tables."""
    Base.metadata.drop_all(bind=engine)
