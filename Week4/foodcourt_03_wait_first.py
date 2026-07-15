import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen


async def main():
    MY_STUDENT_ID = "6710301020"

    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED) ---")

    start_time = time()

    t1 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "hainanese_chicken",
            "Chicken Rice Thigh"
        )
    )

    t2 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "noodle",
            "Wonton Noodles"
        )
    )

    t3 = asyncio.create_task(
        send_order_to_kitchen(
            MY_STUDENT_ID,
            "steak",
            "Sizzling Steak"
        )
    )

    done, pending = await asyncio.wait(
        {t1, t2, t3},
        return_when=asyncio.FIRST_COMPLETED
    )

    winner = done.pop().result()

    print(
        f"{ctime()} | Winner served dish! Shop: {winner['shop']} | Menu: {winner['menu']}"
    )

    print(
        f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders..."
    )

    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)

    print(
        f"{ctime()} | Total waiting time for the first dish: {time()-start_time:.2f} seconds."
    )

if __name__ == "__main__":
    asyncio.run(main())