def reverseString(s: list[str]) -> list[str]:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        
        left += 1
        right -= 1

    return s


test_runs = [["H", "E", "L", "L", "O"], ]

test_run_num = 1
for test_run in test_runs:
    print(f"Run #{test_run_num}: {reverseString(test_run)}")
    test_run_num += 1