# 자격증으로 직업 추천받기
# 자격증에 해당되는 직업 목록 -> 직업들의 급여 목록 만들기
# 급여 목록을 퀵 정렬로 정렬한 다음
# 자격증에서 급여가 일치하는 직업을 찝어서 해당 순서대로 추가해서 반환
# 급여 순서대로 정렬했다는 점을 명시

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)


def partition(a, pivot, high):
    i = pivot+1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

print('정렬 전:\t', a)  
qsort(a, 0, len(a)-1)
print('정렬 후:\t', a)
