from asyncore import file_wrapper
from google.cloud import pubsub_v1

import requests


class Producer:

    def __init__(self):
        self.project_id = ""
        self.topic_id = ""

    def reading_data_from_api(self):

        payload = {
            "token": "NmqfmelPxPHZfucXRjV1hw",
            "data": {
                "name": "nameFirst",
                "email": "internetEmail",
                "phone": "phoneHome",
                "_repeat": 300
            }
        }

        r = requests.post("https://app.fakejson.com/q", json=payload)

        return r

    def publishing_messages(self,r):

        publisher = pubsub_v1.PublisherClient()

        topic_path = publisher.topic_path(self.project_id, self.topic_id)
        
        data_len = r.len()
        for n in range(0, data_len):
            data_str = f"Message number {n}"
            data = data_str.encode("utf-8")
            future = publisher.publish(topic_path, data)
            print(future.result())

        print(f"Published messages to {topic_path}.")
