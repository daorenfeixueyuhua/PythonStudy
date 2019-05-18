# 被积函数f(x)
def f(x):
    return 2 * x


# 求解积分
# f 被积函数
# a, b 积分上下界
# n 划分份数
def simpson(f, a, b, n):
    h = (b-a)/n
    ans = f(a)+f(b)
    for i in range(1,n,2):
        ans += 4*f(a+i*h)
    for i in range(2, n, 2):
        ans += 2*f(a+i*h)
    return ans*h/3


print(simpson(f, 1 , 2, 100))

