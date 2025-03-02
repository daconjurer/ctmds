from typing import Protocol, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from ctmds.core.utils.filter_sort import BaseFilterParams

Entity = TypeVar("Entity", covariant=True)


class IRead(Protocol[Entity]):
    """Interface for operations that read from the database."""

    def get_by(
        self,
        db: Session,
        filter: BaseFilterParams,
    ) -> Entity | None:
        """Get an entity using a key-value filter."""
        ...


class Schema(BaseModel): ...
