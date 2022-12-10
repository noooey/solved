def solutions():
    n = [1]*10001

    for i in range(1, 10001):
        tmp = i
        for j in str(i):
            tmp += int(j)
        if tmp < 10001:
            n[tmp] = 0

    return n

if __name__ == "__main__":
    nums = solutions()

    for idx in range(1, len(nums)):
        if nums[idx]:
            print(idx)
