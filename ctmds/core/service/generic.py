from typing import Generic

from ctmds.core.data_access.interfaces import Entity
from ctmds.core.db.session import SessionStream, get_session
from ctmds.core.service.interfaces import IService


class GenericService(IService, Generic[Entity]):
    def __init__(
        self,
        db: SessionStream = get_session,
    ):
        self.db: SessionStream = db
