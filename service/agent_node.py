from infra.agnet_client import HuggingFaceClient
from langchain.messages import HumanMessage, AIMessage


class HggingfaceAgentNode:
    def __init__(self) -> None:
        self.client = HuggingFaceClient()

    async def run(self, state):
        messages = state["messages"][-1].content
        respones = ""
        async for chunk in self.client.run_query(messages):
            if chunk:
                respones += chunk
            yield {"messages": [{"role": "assistant", "content": respones}]}
