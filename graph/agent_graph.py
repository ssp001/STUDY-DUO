from langgraph.prebuilt import ToolNode
from agent_utils.tools.ai_tools import search_tool

from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, MessagesState, START, END

from infra.agnet_client import HuggingFaceClient
from service.agent_node import HggingfaceAgentNode

# incilizing tools for graph
tools = [search_tool]
service = HggingfaceAgentNode()

# make the graph
builder = StateGraph(MessagesState)
builder.add_node("llm", service.run)
builder.add_node("tools", ToolNode(tools, handle_tool_errors=True))

builder.add_edge(START, "llm")
builder.add_conditional_edges(
    "llm", tools_condition)  # Routes to "tools" or END
builder.add_edge("tools", "llm")


# compile graph bulider
graph = builder.compile()
