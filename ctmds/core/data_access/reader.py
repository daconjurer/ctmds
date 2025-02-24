from typing import Type

from loguru import logger
from sqlalchemy import column, select
from sqlalchemy.orm import Session

from ctmds.core.data_access.interfaces import Entity, IRead
from ctmds.core.utils.filter_sort import BaseFilterParams, SortParams
from ctmds.domain.exceptions import CoreException


class GenericReader(IRead[Entity]):
    model: Type[Entity]

    def get_by(
        self,
        db: Session,
        filter: BaseFilterParams,
    ) -> Entity | None:
        """Read operation.

        Fetches a record by a filter key-value pair.
        """

        logger.debug(f"Getting one {self.model.__name__} by filter {filter}")

        filters = filter.get_filters()

        if len(filters) > 1:
            raise CoreException("Only one filter is allowed for this operation.")

        statement = select(self.model)

        for key, value in filters.items():
            statement = statement.where(column(key) == value)

        entity = db.scalar(statement)
        db.commit()
        db.refresh(entity)

        return entity

    def get_many(
        self,
        db: Session,
        filter: BaseFilterParams | None = None,
        sort: SortParams | None = None,
        limit: int | None = 5,
        page: int | None = 1,
    ) -> list[Entity]:
        """Read operation.

        Fetches a list of records from the database with optional filtering,
         sorting and pagination.
        """

        logger.debug(f"Getting several {self.model.__name__}")

        statement = select(self.model)

        if filter:
            filters = filter.get_filters()

            for key, value in filters.items():
                statement = statement.where(column(key) == value)

        # Apply sorting
        if sort:
            statement = statement.order_by(
                column(sort.sort_by).asc()
                if sort.sort_order == "asc"
                else column(sort.sort_by).desc()
            )

        # Apply pagination
        if page is not None and limit is not None:
            page = 1 if page < 1 else page
            offset = (page - 1) * limit
            statement = statement.offset(offset).limit(limit)

        # Query
        logger.debug(statement.compile(compile_kwargs={"literal_binds": True}))

        result = db.scalars(statement)
        db.flush()
        entities = list(result.all())

        return entities
