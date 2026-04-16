from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from graph.agent_graph import graph

from infra.redish_abstraction import RedishAbstration

from utils.logger import log
import sys

logger = log(system_handeler=sys.stdout, file_handler="monitor/agent_api.log")
db_service = RedishAbstration()
router = APIRouter()


async def genarator(query: str):
    try:
        async for chunk in graph.astream({"messages": [{"role": "user", "content": query}]}):
            logger.info("agnet anwer fetched sucessfully")
            db_service.post_data(user_data=query, ai_data=chunk)
            yield str(chunk)
    except Exception as error:
        logger.exception(f"exception occured{error}")
        raise RuntimeError(error)


@router.post("/ai_answer")
async def ai_answer(query: str):
    return StreamingResponse(genarator(query), media_type="text/plain")
