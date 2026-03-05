import random
import time

def bubble_sort(arr: list[int]) -> list[int]:
    """버블 정렬 (Bubble Sort)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr: list[int]) -> list[int]:
    """선택 정렬 (Selection Sort)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr: list[int]) -> list[int]:
    """삽입 정렬 (Insertion Sort)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr: list[int]) -> list[int]:
    """병합 정렬 (Merge Sort)"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr, low=0, high=None):
    """퀵 정렬 (Quick Sort)"""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

MIN_MERGE = 32

def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort_for_timsort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_for_timsort(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = arr[l : m + 1]
    right = arr[m + 1 : r + 1]
    
    i = j = 0
    k = l
    
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
        
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timsort(arr):
    """팀소트 파이썬 구현 (Timsort Python)"""
    n = len(arr)
    min_run = calc_min_run(n)
    
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_for_timsort(arr, start, end)
        
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge_for_timsort(arr, left, mid, right)
        size = 2 * size
    return arr

# --- 테스트 코드 ---
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)

    # 성능 비교를 위해 데이터 크기 증가
    DATA_SIZE = 3000
    test_data = [random.randint(1, 10000) for _ in range(DATA_SIZE)]
    print(f"데이터 크기: {DATA_SIZE}개 (1부터 10000 사이의 무작위 숫자)\n")

    algorithms = {
        "버블 정렬 (Bubble Sort)": bubble_sort,
        "선택 정렬 (Selection Sort)": selection_sort,
        "삽입 정렬 (Insertion Sort)": insertion_sort,
        "병합 정렬 (Merge Sort)": merge_sort,
        "퀵 정렬 (Quick Sort)": quick_sort,
        "팀소트 (파이썬 구현)": timsort,
        "파이썬 내장 정렬 (Timsort)": sorted,
    }

    import unicodedata

    def get_display_width(s):
        return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)

    def pad_str(s, width):
        return s + ' ' * max(0, width - get_display_width(s))

    print(f"{pad_str('알고리즘 이름', 28)} | {pad_str('정렬 결과(검증)', 15)} | {'실행 시간(초)'}")
    print("-" * 65)

    for name, func in algorithms.items():
        arr_copy = test_data.copy()
        
        start_time = time.time()
        sorted_arr = func(arr_copy)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        
        # 파이썬 내장 정렬 결과와 비교하여 검증
        is_correct = sorted_arr == sorted(test_data)
        result_str = "성공" if is_correct else "실패"
        
        print(f"{pad_str(name, 28)} | {pad_str(result_str, 15)} | {elapsed_time:.6f}초")

    print("\n✅ 모든 정렬 알고리즘의 성능 비교가 완료되었습니다!")
