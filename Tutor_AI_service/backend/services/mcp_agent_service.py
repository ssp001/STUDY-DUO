from ..core.mcp_agent_core import MCPAGENTCORE


class MCPAGENTSERVICE:
    def __init__(self, agent_provicer: MCPAGENTCORE):
        self.agent_provider = agent_provicer

    async def run_as_agent(self, querry: str) -> str:
        output = await self.agent_provider.genarate_output(querry=querry)
        return output
