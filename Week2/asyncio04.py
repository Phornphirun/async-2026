# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import time, ctime

async def main():
    print(f"{ctime()} | -> Task Started")
    await asyncio.sleep(1)

    print(f"{ctime()} | -> Task finished")

if __name__ == "main":
    asyncio.run(main())
