import asyncio
from http import client
import httpx

#เปลี่ยน IP ตรงนี้ให้เป็น IP เครื่องพื่อนที่เป็น Server (เช่น 192.168.1.50)
SERVER_IP = "172.20.58.26"
PORT = "8088"
Server_URL = f"http://{SERVER_IP}:{PORT}"

#ระบุรหัส/ชื่อนักเรียนของผู่ส่ง
MY_STUDENT_ID = "6710301020"

async def hunt_coupons():
    async with httpx.AsyncClient() as client:
        print(f"{MY_STUDENT_ID} เริ่มต้นภารกิจล่าคูปอง...")

        #ยิงคูปองต่อเนื่องสูงสุด 5 ครั้ง เพื่อพยายามเก็บให้ได้ครบ 2 คูปอง
        for attempt in range(1, 6):
            try:
                res = await client.post(
                    f"{Server_URL}/claim",
                    json={"student_id": MY_STUDENT_ID},
                    timeout=5.0
                )
                data = res.json()
                status = data.get("status")

                print(f" -- ครั้งที่ {attempt}: [{status}] -> {data.get('message', data.get('claim_coupon'))}")

                #หากได้ครบ 2 ใบ หรือคูปองหมดแล้ว ให้หยุดการยิงทันที
                if status in ["LIMIT_REACHED", "OUT_OF_STOCK"]:
                    break

            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

            #พักก่อนยิงรอบถัดไปเล็กน้อย
            await asyncio.sleep(0.02)

        # ดึงสรุปคูปองส่วนตัว (เฉพาะของ MY_STUDENT_ID)
        print("\nกำลังดึงผลคูปองของตนเอง...")
        try:
            res = await client.get(f"{Server_URL}/my-coupons/{MY_STUDENT_ID}")
            if res.status_code == 200:
                summary = res.json()
                total = summary.get("total_claimed", 0)
                coupons = summary.get("claimed_coupons", [])
                print(f"สรุปผล [{MY_STUDENT_ID}]: ได้รับคูปองรวม {total} ใบ -> {coupons}")
            else:
                print(f"ดึงข้อมูลส่วนตัวไม่สำเร็จ Status Code: {res.status_code}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลส่วนตัว: {e}")

        # เพิ่มการดึงสรุปภาพรวมทั้งหมด (/summary)
        print("\nกำลังดึงสรุปภาพรวมคูปองทั้งหมดจาก Server (/summary)...")
        try:
            res = await client.get(f"{Server_URL}/summary")
            if res.status_code == 200:
                summary_all = res.json()
                rem_stock = summary_all.get("remaining_stock", "N/A")
                claimed = summary_all.get("students_claims", {})

                print(f"จำนวนคูปองคงเหลือใน Server: {rem_stock} ใบ")
                print("รายการคูปองที่นักเรียนแต่ละคนได้รับ:")

                for sid, coupons in claimed.items():
                    print(f" - {sid}: ได้รับ {len(coupons)} ใบ -> {coupons}")
            else:
                print(f"ดึงข้อมูลสรุปภาพรวมไม่สำเร็จ Status Code: {res.status_code}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลสรุปภาพรวม: {e}")

if __name__ == "__main__":
    asyncio.run(hunt_coupons())