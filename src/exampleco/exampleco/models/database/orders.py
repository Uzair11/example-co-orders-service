#### Changes for PR 3 Start
from sqlalchemy import (
    Column,
    Float,
    Integer,
    String,
    text,
    TEXT,
    TIMESTAMP,
    ForeignKey,
    Boolean,
)
from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemySchema
from exampleco.models.database import Session
from exampleco.models.database.services import Service, ServiceSchema
from sqlalchemy.orm import relationship
import enum

from . import Base
from exampleco.utils import ModelManager


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    created_on = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    modified_on = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
    )
    status = Column(Boolean, unique=False, default=True)


class OrderItems(Base):
    __tablename__ = "ordersItem"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    order = relationship("orders", backref="ordersItems")
    service = relationship("services", backref="orderItemsService")


class OrderItem(SQLAlchemySchema):
    class Meta:
        model = OrderItems
        load_instance = True

    name = fields.String(required=True)


class OrderSchema(SQLAlchemySchema, ModelManager):
    class Meta:
        model = Order
        load_instance = True
        session = Session

    id = fields.Integer()
    name = fields.String(required=True)
    status = fields.Boolean(required=False)
    created_on = fields.DateTime()
    modified_on = fields.DateTime()
    order_items = fields.List(fields.Nested(OrderItem))

    def get_all(self):
        return self.dump(self.Meta.model.query.filter(status=True))


#### Chnages for PR 3 end
