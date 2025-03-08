from typing import Protocol, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from ctmds.core.utils.filter_sort import BaseFilterParams, SortParams

Entity = TypeVar("Entity")


class IRead(Protocol[Entity]):
    """Interface for operations that read from the database."""

    def get_by(
        self,
        db: Session,
        filter: BaseFilterParams,
    ) -> Entity | None:
        """Get an entity using a key-value filter."""
        ...

    def get_many(
        self,
        db: Session,
        filter: BaseFilterParams | None = None,
        sort: SortParams | None = None,
        limit: int | None = 5,
        page: int | None = 1,
    ) -> list[Entity]:
        """Get multiple entities using a filter, sort, limit, and page."""
        ...


class Schema(BaseModel): ...
