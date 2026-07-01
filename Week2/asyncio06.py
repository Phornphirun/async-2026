# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting cooking for Custumer {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Finished cooking for Custumer {customer}...")

async def main():
    start_time = time()

    task_a = asyncio.create_task(cook_spaghetti("A"))

    await task_a

    print(f"Total Operation Time: {time() - start_time:.2f} secounds")

if __name__ == "__main__":
    asyncio.run(main())