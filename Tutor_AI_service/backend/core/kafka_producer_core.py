from abc import ABC, abstractmethod


class KAFKPRODUCERCORE(ABC):
    @abstractmethod
    def kafka_producer(self, data, topic):
        pass
