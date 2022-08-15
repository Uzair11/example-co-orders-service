import json
from sqlalchemy.orm.exc import NoResultFound

#### Changes for PR 2 Start
from exampleco.models.database import Session
from exampleco.models.database.orders import Order, OrderSchema


#### Changes for PR 3 Start
def get_all_orders(event, context):
    orders_schema = OrderSchema(many=True)
    data = orders_schema.get_all()
    return {"statusCode": 200, "body": json.dumps(data)}

def get_order_by_id(event, context):
    order_id = event.get("pathParameters",{}).get("id", None) 
    orders_schema = OrderSchema(many=False)
    try:
        data = orders_schema.get_by_id(order_id)
        return {"statusCode": 200, "body": json.dumps(data)}
    except NoResultFound as e:
        return {"statusCode": 404, "body": json.dumps({data : "Orders does not exist"})}

def delete_order_by_id(event, context):
    orders_schema = OrderSchema(many=False)
    try:
        orders_schema.delete_by_id(event.get("pathParameters",{}).get("id", None))
    except Exception as e:
        return {"statusCode": 404, "body": json.dumps({data : "Orders does not exist"})}
