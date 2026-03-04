from abc import abstractmethod, ABC


class MCPAGENTCORE(ABC):
    """abstarion method for Mcp service"""
    @abstractmethod
    def genarate_output(self, querry: str):
        pass
