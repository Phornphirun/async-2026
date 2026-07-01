# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time, ctime

async def serve_custumer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Served {name}...")

async def main():
    start_time = time()
    await serve_custumer("A")
    await serve_custumer("B")

    print(f"total time: {time() - start_time:0.2f} secounds")

if __name__ == "main":
    asyncio.run(main())

