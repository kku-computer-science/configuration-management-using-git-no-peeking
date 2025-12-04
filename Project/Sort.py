def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    numbers_input = input("ใส่ตัวเลข (คั่นด้วย space): ")
    numbers = list(map(int, numbers_input.split()))

    algo = input("เลือก algorithm (quick / bubble): ")

    if algo == "quick":
        result = quick_sort(numbers)
        print("ผลลัพธ์ (quick sort):", result)

    elif algo == "bubble":
        result = bubble_sort(numbers)
        print("ผลลัพธ์ (bubble sort):", result)

    else:
        print("ไม่รู้จัก algorithm ที่เลือก")


if __name__ == "__main__":
    main()

