import time

from main import Order
from main import redis

key = "refund_order"
group = "payment_group"
consumer_name = "refund_order_consumer"

last_message_id = {"id": "0-0"}

try:
    redis.xgroup_create(name=key, groupname=group)
except Exception as e:
    print(f"Group already exists: {e}")
    # print("creating a new stream with lenght of 0")
    # redis.xgroup_create(key, group, mkstream=True)

while True:
    try:
        # XREADGROUP is a write command because even if it reads from the stream,
        # the consumer group is modified as a side effect of reading,
        # so it can only be called on master instances.
        # reading messages never delivered to other consumers so far using '>'
        results = redis.xreadgroup(
            groupname=group, consumername=consumer_name, streams={key: ">"}, count=None
        )
        # TODO: redis.xack()
        if results != []:
            print(results)
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj["pk"])
                order.status = "refunded"
                order.save()

    except Exception as e:
        print(f"Error payment consumer xreadgroup: {e}")
    time.sleep(1)
