from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from typing import Any

from utils.logger import log
import sys
logge = log(system_handeler=sys.stdout, file_handler="monitor/agent_tools.log")


@tool
def search_tool(query: str) -> Any:
    """ this is a search tool in the internet use when it is needed """
    _search_engine = DuckDuckGoSearchResults(verbose=True)
    try:
        ans = _search_engine.invoke({"input": query})
        logge.info("Duck duck go search has inicilized")
        return ans
    except Exception as error:
        logge.exception(f"tools has an exception occured:{str(error)}")
