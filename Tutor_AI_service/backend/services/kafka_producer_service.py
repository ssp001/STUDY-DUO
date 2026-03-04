from core.kafka_producer_core import KAFKPRODUCERCORE


class KAFKAPRODUCERSERVICE:
    def __init__(self, producer: KAFKPRODUCERCORE):
        self.producer = producer

    async def produce_data(self, data, topic):
        output = self.producer.kafka_producer(data=data, topic=topic)
        return output
