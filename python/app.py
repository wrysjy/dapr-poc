# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------
import json
import time
import requests
import os
from dapr.clients import DaprClient

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
        print("Sending message with invoke ...", flush=True)
        requests.post(dapr_url, json=message)
        print("Sending message to pubsub ...", flush=True)
        requests.post(pub_sub_url, json=message_pub_sub)
        secret_store = requests.get(secret_store_url)
        print("Secret store: {}".format(secret_store.text), flush=True)

        with DaprClient() as d:
            CONFIG_STORE_NAME = 'configstore'
            keys = ['orderId', 'orderId1']
            # Startup time for dapr
            d.wait(20)
            configuration = d.get_configuration(store_name=CONFIG_STORE_NAME, keys=keys, config_metadata={})
            print(f"Got key={configuration.items[0].key} value={configuration.items[0].value} version={configuration.items[0].version} metadata={configuration.items[0].metadata}", flush=True)
            print(f"Got key={configuration.items[1].key} value={configuration.items[1].value} version={configuration.items[1].version} metadata={configuration.items[1].metadata}", flush=True)

    except Exception as e:
        print(e)

    time.sleep(10)
