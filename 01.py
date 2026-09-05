import asyncio
import time
import aiohttp
from loguru import logger




async def send_request(client, url):
    response = await client.get(url)
    logger.info(response.status)
    return response.status


async def main():
    urls = ["https://www.baidu.com" for _ in range(10)]

    async with aiohttp.ClientSession() as session:
        tasks = (send_request(session, url) for url in urls)
        # 使用 gather 并发发起所有请求
        results = await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"总耗时: {time.time() - start:.2f} 秒")