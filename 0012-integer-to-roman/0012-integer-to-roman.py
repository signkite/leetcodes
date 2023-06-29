def calc_roman_num(answer, digit, ninth, fifth, one):
    if digit == 9:
        answer += ninth
        digit = 0
    elif digit == 4:
        answer += one + fifth
        digit = 0
    elif digit >= 5:
        answer += fifth
        digit -= 5
    
    for _ in range(digit):
        answer += one

    return answer


class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        num = str(num)

        # 1000의 자리
        if len(num) == 4:
            digit = int(num[0])
            answer += 'M' * digit
            num = num[1:]
        
        # 100의 자리
        if len(num) == 3:
            answer = calc_roman_num(answer, int(num[0]), 'CM', 'D', 'C')
            num = num[1:]
        
        if len(num) == 2:
            answer = calc_roman_num(answer, int(num[0]), 'XC', 'L', 'X')
            num = num[1:]

        answer = calc_roman_num(answer, int(num), 'IX', 'V', 'I')
        return answer
