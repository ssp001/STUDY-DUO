"""MCPAGENT as a context manager"""
from ..core.analaysis_core import ANALAYSISCORE
from mcp_use import MCPAgent, MCPClient
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
import logging
import os
import sys
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,  # 👈 VERY IMPORTANT
)
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["MCP_USE_ANONYMIZED_TELEMETRY"] = "false"


class STUDENTANALAYSISINFRA(ANALAYSISCORE):
    """MCPAGENT class can ve use as a context manager
    - value: verbose:Literral[True,false]

    """

    def __init__(self, verbose: bool):
        try:
            self.endpoint = HuggingFaceEndpoint(
                model="mistralai/Mistral-7B-Instruct-v0.2", huggingfacehub_api_token=os.getenv("HUGGINGFACE_ENDPOINT"))
            self.model = ChatHuggingFace(llm=self.endpoint)

            self.verbose = verbose
            logging.info("MCPAGENT incilaization started")
            TOOL_PATH = os.getenv("MCP_TOOLS_PATH")
            try:
                prompt = """You are Study-Duo, an AI student performance analyzer.

                    Student Message:
                    {student_message}

                    Task:
                    1. Analyze the student's message and determine:
                    - Topics discussed
                    - Strengths and weaknesses
                    - Performance metrics (score, improvement)
                    - Recommendations for improvement
                    - Make a visual representation usig tool
                    2. Output **JSON only** in the following format:

                    {
                    "ai_message": "A concise response or feedback to the student",
                    "analysis": [
                        {
                        "topic": "Topic Name",
                        "current_score": 0-100,
                        "previous_score": 0-100,
                        "improvement": 0-100,
                        "recommendation": "Actionable advice for the student"
                        }
                    ],
                    "overall": {
                        "average_score": 0-100,
                        "progress_trend": "improving/steady/declining"
                    }
                    }"""

                if TOOL_PATH is not TypeError:
                    self.mcp_client = MCPClient(
                        config=TOOL_PATH)
                    self.agent = MCPAgent(
                        llm=self.model, client=self.mcp_client, memory_enabled=True, verbose=self.verbose, retry_on_error=True, system_prompt=prompt)
                    logging.info("your tools are configured suucess fully")
                else:
                    raise TypeError("can't configure MCP_TOOLS_PATH")
            except Exception as error:
                logging.exception(error)
                raise Exception(f"there is a error in:{error}")
        except Exception as error:
            logging.error(f"MCPAGENT incilaization failed{error}")
            raise RuntimeError(f"MCPAGENT incilaization failed{error}")

    async def genarate_output(self, querry):
        from langchain.messages import HumanMessage
        result = ""
        async for chunk in self.agent.stream(HumanMessage(content=querry)):
            result += chunk
        return result
