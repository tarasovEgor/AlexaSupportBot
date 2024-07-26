from openai import AsyncOpenAI
from config import OPEN_AI_TOKEN, PROXY_URL


client = AsyncOpenAI(
    api_key=OPEN_AI_TOKEN,
    base_url=PROXY_URL,
)

async def gpt4(question):
    response = await client.chat.completions.create(
        messages=[{"role": "user",
                   "content": str(question)}],
        model="gpt-3.5-turbo"
    )
    return response



# client = AsyncOpenAI(api_key=OPEN_AI_TOKEN,
#                      http_client=httpx.AsyncClient(
#                          proxies=PROXY,
#                          transport=httpx.HTTPTransport(local_address="0.0.0.0")
#                         )
#                     )