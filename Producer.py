from asyncore import file_wrapper
from google.cloud import pubsub_v1


class Producer:

    def __init__(self):
        self.project_id = ""
        self.topic_id = ""

    def publishing_messages(self):

        publisher = pubsub_v1.PublisherClient()

        topic_path = publisher.topic_path(self.project_id, self.topic_id)

        for n in range(1, 10):
            data_str = f"Message number {n}"
            data = data_str.encode("utf-8")
            future = publisher.publish(topic_path, data)
            print(future.result())

        print(f"Published messages to {topic_path}.")
