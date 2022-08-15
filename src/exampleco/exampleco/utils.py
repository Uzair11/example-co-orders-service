from sqlalchemy.orm.exc import NoResultFound

#### Changes for PR 2 Start
class ModelManager:
    
    @property
    def queryset(self):
        return self.Meta.session.query(self.Meta.model)

    @property
    def session(self):
        return self.Meta.session

    def get_by_id(self, obj_id: int):
        obj = self.queryset.get(obj_id)
        if obj == None:
            raise NoResultFound("Obj not found")
        return self.dump(obj)

    def get_all(self):
        return self.dump(self.Meta.model.queryset.all())

    def filter(self, **filter):
        return self.dump(self.Meta.model.queryset.filter(**filter))
    
    def delete_by_id(id):
        self.queryset.filter_by(id=id).delete()


#### Changes for PR 2 End
