def sequential_search(n, target, array):
            for i in range(n):
                if array[i] == target:
                    return i + 1

array = ["정보보안전문가", "자산운용가", "건축석공", "공무원", "제빵사", "회계사"]
print(sequential_search(len(array), "회계사", array))