# 将一个ｘ进制的数转换为y进制数
# x 源进制
# y 目标进制
# s 源数字


def transform(x, y, s):
    res = ''
    sum = 0
    for i in s:
        if i == '-':
            continue
        if '0' <= i and i <= '9':
            sum = sum*x + (int(i) - int('0'))
        else:
            sum = sum*x + (int(i) - int('A'))
    # 1. 先转换为10进制

    while sum:
        temp = sum % y
        sum = int(sum / y)
        if temp <= 9:
            temp = temp + int('0')
        else:
            temp = chr(int(temp) - 10 + int('A'))
        res = str(temp) + res

    # 2. 在转换为y进制
    if not len(res):
        res = '0'
    if s[0] == '-':
        res = '-' + res
    return res


if __name__ == '__main__':
    print(transform(2, 7, '1000'))

