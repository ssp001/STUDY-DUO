"""MCPAGENT as a context manager"""
from ..core.mcp_agent_core import MCPAGENTCORE
from mcp_use import MCPAgent, MCPClient
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.chat_models import ChatHuggingFace
import logging
import os
import sys
logger = logging.getLogger(__name__)
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,  # 👈 VERY IMPORTANT
)
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["MCP_USE_ANONYMIZED_TELEMETRY"] = "false"


class MCPAGENTCLIENT(MCPAGENTCORE):
    """MCPAGENT class can ve use as a context manager
    - value: verbose:Literral[True,false]

    """

    def __init__(self, verbose: bool):
        try:
            self.endpoint = HuggingFaceEndpoint(
                model="mistralai/Mistral-7B-Instruct-v0.2", huggingfacehub_api_token=os.getenv("HUGGINGFACE_ENDPOINT"))
            self.model = ChatHuggingFace(llm=self.endpoint)

            self.verbose = verbose
            logger.info("MCPAGENT incilaization started")
            TOOL_PATH = os.getenv("MCP_TOOLS_PATH")
            try:
                prompt = """You are an intelligent AI Teacher your name is Study-Duo. Your tasks are:
                        1. Assess the student's current knowledge based on their messages.
                        2. Provide study material tailored to their current level.
                        3. Create a timetable suggesting what topics to study, how long to spend on each, and in what order.
                        4. Track student performance as the conversation progresses:
                        - Note topics the student struggles with.
                        - Track responses, mistakes, and engagement.
                        - Suggest improvements for weaker areas.
                        5. At the end of the session, generate a clear **text summary document** that includes:
                        - Topics covered
                        - Performance metrics
                        - Weak and strong areas
                        - Recommended next steps
                        - Optimized timetable for future study
                        6. Format this summary so it can be sent to another AI for further analysis or recommendations.

                        Your goal is to act like a tutor and a study coach in one session. Make your feedback actionable and concise, while ensuring the summary document is structured and easy to understand."""
                additional_prompt = """You are an intelligent AI Teacher. Your tasks are:

                        1. Assess the student's current knowledge based on their messages.
                        2. Provide study material tailored to their current level.
                        3. Create a timetable suggesting what topics to study, how long to spend on each, and in what order.
                        4. Track student performance as the conversation progresses **secretly**:
                        - Note topics the student struggles with.
                        - Track responses, mistakes, and engagement.
                        - Suggest improvements for weaker areas.
                        - **At no point should you reveal that you are tracking the student's performance.**
                        5. At the end of the session, generate a clear **text summary document** that includes:
                        - Topics covered
                        - Performance metrics (kept internal)
                        - Weak and strong areas
                        - Recommended next steps
                        - Optimized timetable for future study
                        6. Format this summary so it can be sent to another AI for further analysis or recommendations.

                        **Additional Instructions:**  
                        - Under no circumstances mention or expose that you are tracking the student.  
                        - Only provide study material, guidance, and actionable tips.  
                        - Make your feedback actionable and concise.  
                        - Ensure the summary document is structured, professional, and easy for another AI to analyze."""
                if TOOL_PATH is not TypeError:
                    self.mcp_client = MCPClient(
                        config=TOOL_PATH)
                    self.agent = MCPAgent(
                        llm=self.model, client=self.mcp_client, memory_enabled=True, verbose=self.verbose, retry_on_error=True, system_prompt=prompt, additional_instructions=additional_prompt)
                    logger.info("your tools are configured suucess fully")
                else:
                    raise TypeError("can't configure MCP_TOOLS_PATH")
            except Exception as error:
                logger.exception(error)
                raise Exception(f"there is a error in{logger}:{error}")
        except Exception as error:
            logger.error(f"MCPAGENT incilaization failed{error}")
            raise RuntimeError(f"MCPAGENT incilaization failed{error}")

    async def genarate_output(self, querry):
        from langchain.messages import HumanMessage
        result = ""
        async for chunk in self.agent.stream(HumanMessage(content=querry)):
            result += chunk
        return result
