from core.kafka_producer_core import KAFKPRODUCERCORE
from confluent_kafka import Producer
import json
import logging


class KAFKAPRODUCLIENT(KAFKPRODUCERCORE):
    def __init__(self, kafka_config: dict):
        super().__init__()
        self.prod = Producer(kafka_config)

    def kafka_producer(self, data, topic: str):
        try:
            msg = json.dumps(data).encode("utf-8")
            self.prod.produce(value=msg, topic=[topic])
            self.prod.poll(0)
            logging.info("data send to consumer")
        except Exception as error:
            logging.error("can't send data to consumer")
            raise RuntimeError(error)
