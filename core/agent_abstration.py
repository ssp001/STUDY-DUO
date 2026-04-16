from abc import ABC,abstractmethod
from typing import *


class AgentAbstration(ABC):
    @abstractmethod
    def run_query(self,query:str)->AsyncGenerator[Any]:
        pass