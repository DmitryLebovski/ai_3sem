a = float(input())

if float("-inf") < a < -5:
    print(a, "принадлежит интервалу: (-infinity, -5)")
elif -5 <= a <= 5:
    print(a, "принадлежит интервалу: [-5, 5]")
else:
    print(a, "принадлежит интервалу: (5, +infinity)")