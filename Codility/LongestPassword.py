
def solution(S):
    words = S.split()
    valid = ''

    for word in words:
        letter = 0
        digit = 0
        kiho = False
        for chr in word.lower():
            if not ((122 >= ord(chr) and ord(chr) >= 97) or (57 >= ord(chr) and ord(chr) >= 48)):
                kiho = True
                continue
            if (122 >= ord(chr) and ord(chr) >= 97):
                letter += 1
            if (57 >= ord(chr) and ord(chr) >= 48):
                digit += 1
        if kiho:
            continue
        if letter % 2 != 0:
            continue
        if digit % 2 == 0:
            continue
        if letter == 0 and digit == 0:
            continue

        if len(word) > len(valid):
            valid = word

    if valid == '':
        return -1

    return len(valid)
