import json

from exampleco.models.database import Session
from exampleco.models.database.orders import Order, OrderSchema
from exampleco.models.database.services import Service, ServiceSchema
#### Changes for PR 2 End

# pylint: disable=unused-argument
def get_all_orders(event, context):
    """
    Example function that demonstrates grabbing list or orders from database

    Returns:
        Returns a list of all orders pulled from the database.
    """

    orders_schema = OrderSchema(many=True)
    orders = Session.query(Order).all()
    results = orders_schema.dump(orders)

    response = {"statusCode": 200, "body": json.dumps(results)}

    return response

#### Changes for PR 2 Start
def get_service_by_id(event, context):
    service_id = event.get("pathParameters",{}).get("id", None) 
    service_shema = ServiceSchema(many=False)
    try:
        data = service_shema.get_by_id(service_id)
        return {"statusCode": 200, "body": json.dumps(data)}
    except NoResultFound as e:
        return {"statusCode": 404, "body": json.dumps({data : "Service does not exist"})}

def get_all_services(event, context):
    service_shema = ServiceSchema(many=True)
    data = service_shema.get_all(service_id)
    return {"statusCode": 200, "body": json.dumps(data)}

#### Changes for PR 2 End
