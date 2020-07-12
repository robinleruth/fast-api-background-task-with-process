from app.infrastructure.db.some_table import SomeTable
from app.infrastructure.db.db_session import transaction_context

from app.domain.services.some_db_service.util import memoize


class SomeDbService:
    # @memoize
    def get_info_from_table(self, _id: int):
        with transaction_context() as session:
            entry = session.query(SomeTable).filter_by(id=_id).first()
        return entry.info

    def update(self, _id, info):
        with transaction_context() as session:
            entry = session.query(SomeTable).filter_by(id=_id).first()
            entry.info = info
        return entry.info
