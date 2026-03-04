from abc import ABC, abstractmethod


class ANALAYSISCORE(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def genarate_output(self):
        pass
