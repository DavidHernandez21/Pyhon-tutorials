import time

from main import Product
from main import redis

key = "order_completed"
group = "inventory_group"
consumer_name = "order_completed_consumer"

try:
    redis.xgroup_create(name=key, groupname=group)
except Exception as e:
    print(f"Group already exists: {e}")
    # print("creating a new stream with lenght of 0")
    # redis.xgroup_create(key, group, mkstream=True)

while True:
    try:
        results = redis.xreadgroup(
            groupname=group, consumername=consumer_name, streams={key: ">"}, count=None
        )
        # redis.xack()
        if results != []:
            print(results)
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj["product_id"])
                    product.quantity = product.quantity - int(obj["quantity"])
                    product.save()
                except Exception as e:
                    print(f"Error inventory consumer: {e}")
                    redis.xadd(name="refund_order", fields=obj, id="*", maxlen=100)

    except Exception as e:
        print(f"Error inventory consumer xreadgroup: {e}")
    time.sleep(1)
