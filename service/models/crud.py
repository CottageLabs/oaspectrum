from service.models import Score
from octopus.modules.crud.models import ES_CRUD_Wrapper_Ultra

class ScoreCrud(ES_CRUD_Wrapper_Ultra):
    INNER_TYPE = Score

    @classmethod
    def pull(cls, id):
        # get the inner type, but then we want to omit the admin data
        inner = cls.INNER_TYPE.pull(id)
        if inner is None:
            return None

        # remove the admin data
        inner.remove_admin_data()

        # return the instance
        this = cls()
        this.inner = inner
        return this
