from fastapi import APIRouter
from ..services.mcp_agent_service import MCPAGENTSERVICE
from ..infra.mcp_agent_client import MCPAGENTCLIENT
from ..config.userclass import UserClass
from ..services.kafka_producer_service import KAFKAPRODUCERSERVICE
from ..infra.kafka_producer_client import KAFKAPRODUCLIENT
client = MCPAGENTCLIENT(verbose=True)
service = MCPAGENTSERVICE(agent_provicer=client)
kafka_client = KAFKAPRODUCLIENT({"bootstrap.servers": "localhost:9092"})
kafka_service = KAFKAPRODUCERSERVICE(client)
router = APIRouter()


@router.post("/output")
async def end_point(q: UserClass):
    output = await service.run_as_agent(querry=q.messages)
    kafka_service.produce_data(data=output, topic="message_tracker")
    return output
