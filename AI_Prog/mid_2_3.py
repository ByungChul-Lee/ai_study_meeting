def gcd(a, b):
    tmp = 0
    while(b > 0):
        tmp = a % b
        a = b
        b = tmp
    return a

def lcm(a, b):
    return a*b/gcd(a,b)

a = int(input("첫 번째 수를 입력하시오 "))
b = int(input("두 번째 수를 입력하시오 "))

print("최대공약수 : ",gcd(a, b))
print("최소공배수 : ",lcm(a, b))