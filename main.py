from graph.agent_graph import graph
from typing import *
import asyncio


async def main(query: str) -> dict[str, Any] | Any:
    ans = await graph.ainvoke({"input": query})
    return ans


ans = main("hi who are you")
if __name__ == "__main__":
    asyncio.run(ans)
print(ans)
