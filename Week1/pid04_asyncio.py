from time import ctime, time
import asyncio
import os
import threading

# ฟังก์ชันของการทำงานแบบ Asynchronous
async def make_coffee(customer_name):
    # 1. Process ID และ Thread ID (จะแสดงงานเดียวกันทุกตัว)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    # 2. ข้อมูล Task ปัจจุบัน ของ asyncio
    current_task = asyncio.current_task()
    task_name = current_task.get_name()  # ชื่อ Task

    # ใน Python 3.12+ สามารถใช้ Unique ID ของ Task ได้ง่าย โดยใช้ id(current_task)
    task_id = id(current_task)

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    # จำลองงาน (Non-blocking wait)
    await asyncio.sleep(5)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] ลูกค้า {customer_name} ได้รับกาแฟแล้วค่ะ!")

async def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองร้านกาแฟแบบ asyncio ===")
    start_time = time()

    tasks = []
    for customer in queue:
        # สร้าง Coroutine
        coro = make_coffee(customer)

        # แปลง Coroutine ให้เป็น Task แล้วให้ Event Loop บริหาร และตั้งชื่อได้
        task = asyncio.create_task(coro, name=f"Task-{customer}")
        tasks.append(task)

    # ให้ทำงานพร้อมกัน
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลาทั้งหมดประมาณ: {duration:0.2f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())