from quicksort import quicksort
from bubblesort import bubblesort

def get_numbers():
    raw = input("กรอกตัวเลขคั่นด้วย space: ")
    return list(map(int, raw.split()))

numbers = get_numbers()

print("\nเลือกวิธีการเรียงลำดับ:")
print("1. Quick Sort")
print("2. Bubble Sort")
choice = input("พิมพ์ 1 หรือ 2: ")

if choice == "1":
    result = quicksort(numbers)
    print("\nผลลัพธ์จาก Quick Sort:", result)
elif choice == "2":
    result = bubblesort(numbers)
    print("\nผลลัพธ์จาก Bubble Sort:", result)
else:
    print("\nตัวเลือกไม่ถูกต้อง")