tmp = int(input())
#สร้างตัวนับจำนวนซ้ำ กับ เก็บค่าที่มันซ้ำ ติดต่อกันโดยไม่มีอะไรกั้น
last_tmp = 0
count = 1 #นับไปละ 1จาก input 
max_count = -9999 # ซ้ำกี่รอบ
res = 0 #ค่าที่ซ้ำบ่อย

while tmp != 0 :
  if tmp == last_tmp:
    count += 1
  else :
      count = 1  # นับใหม่เลย
  if count > max_count : # ถ้าขึ้นเลขใหม่ count จะไม่เข้า เงื่อนไขทำให้ ค่า count ยังตัวแปรเดิม
    max_count = count  # เพิ่มขึ้นเป็นจำนวนที่เท่ากับ count
    res = tmp # ถ้าไม่เข้าเงื่อนไข res ก็เปลี่ยนแปลงไม่ได้
  last_tmp = tmp # เก็บค่าตัวแปร tmp ล่าสุด
  tmp = int(input())
print(max_count)
print(res)