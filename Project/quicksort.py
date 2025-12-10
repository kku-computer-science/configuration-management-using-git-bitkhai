def quicksort(arr):
    # Base Case: ถ้าลิสต์ว่างหรือมีสมาชิกแค่ 1 ตัว ถือว่าเรียงเสร็จแล้ว
    if len(arr) <= 1:
        return arr
    
    # เลือก Pivot (ในที่นี้เลือกตัวตรงกลาง)
    pivot = arr[len(arr) // 2]
    
    # แบ่งกลุ่มข้อมูล
    left = [x for x in arr if x < pivot]    # ค่าน้อยกว่า pivot
    middle = [x for x in arr if x == pivot] # ค่าเท่ากับ pivot
    right = [x for x in arr if x > pivot]   # ค่ามากกว่า pivot
    
    # ส่งค่ากลับโดยเรียกฟังก์ชันซ้ำ (Recursion) กับฝั่งซ้ายและขวา
    return quicksort(left) + middle + quicksort(right)