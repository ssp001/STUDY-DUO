import httpx
import asyncio


async def call_async():
    async with httpx.AsyncClient(timeout=90) as client:
        response = await client.post(url="http://127.0.0.1:8000/api/v1/output", json={"messages": "hi who are you"})
        print(response.json())
        return response.json(),


if __name__ == "__main__":
    asyncio.run(call_async())

# uvicorn  backend.api.router.api_endpoint:app --reload
# Run this file in terminal
