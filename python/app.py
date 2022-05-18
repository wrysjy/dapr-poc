# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------
import json
import time
import requests
import os

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/nodeapp/method/neworder".format(dapr_port)

# pub sub
pub_sub_url = "http://localhost:{}/v1.0/publish/pubsub/deathStarStatus".format(dapr_port)

# secret store
secret_store_url = "http://localhost:{}/v1.0/secrets/localsecretstore/mysql".format(dapr_port)

n = 0
while True:
    n += 1

    message_pub_sub = {"status": "completed"}
    message = {"data": {"orderId": n}}

    try:
        requests.post(dapr_url, json=message)
        requests.post(pub_sub_url, json=message_pub_sub)
        secret_store = requests.get(secret_store_url)
        print("Secret store: {}".format(secret_store.text), flush=True)
    except Exception as e:
        print(e)

    time.sleep(10)
