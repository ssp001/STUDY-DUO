# Hugging face client use
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
from core.agent_abstration import AgentAbstration

from langgraph.prebuilt import ToolNode

from utils.logger import log
from typing import *

from dotenv import load_dotenv
import sys
import os

load_dotenv()
logger = log(system_handeler=sys.stdout,
             file_handler="monitor/Huggingfaceclient.log")


class HuggingFaceClient(AgentAbstration):
    def __init__(self):
        self.hugging_wrapper = HuggingFaceEndpoint(model=os.getenv(
            "HUGGINGFACE_AI_MODEL"), huggingfacehub_api_token=os.getenv("HUGGING_FACE_API_TOKEN"), streaming=True, verbose=True)
        self.client = ChatHuggingFace(llm=self.hugging_wrapper)

    async def run_query(self, query: str) -> AsyncGenerator[Any]:
        """self run query it is asynce 
        Args: query-> str
        return: List[str]
        """
        try:
            for chunks in self.client.stream(query):
                logger.info("streming respones fetched succesful")
                yield chunks.content
        except Exception as error:
            logger.info(f"an excestion occured:{error}")
            raise RuntimeError(error)
