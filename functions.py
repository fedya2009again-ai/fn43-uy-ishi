def hello():
    return "Hello"


def kvadrat(a):
    return a * a


def kub(a):
    return a * a * a


def yigindi(a, b):
    return a + b


def ayirma(a, b):
    return a - b


def kopaytma(a, b):
    return a * b


def bolish(a, b):
    return a / b


def max_son(a, b):
    return max(a, b)


def min_son(a, b):
    return min(a, b)


def juftmi(a):
    return a % 2 == 0


def toqmi(a):
    return a % 2 != 0

def katta_harf(matn):
    return matn.upper()


def kichik_harf(matn):
    return matn.lower()


def teskari(matn):
    return matn[::-1]


def uzunligi(matn):
    return len(matn)




def yigindi_list(lst):
    return sum(lst)


def eng_katta(lst):
    return max(lst)


def eng_kichik(lst):
    return min(lst)


def uzunligi_list(lst):
    return len(lst)


def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija


def daraja(a, b):
    return a ** b


def abs_son(a):
    return abs(a)


print(hello())
print(kvadrat(5))
print(kub(3))
print(yigindi(5, 7))
print(ayirma(10, 2))
print(kopaytma(3, 4))
print(bolish(20, 5))
print(max_son(4, 8))
print(min_son(4, 8))
print(juftmi(12))
print(toqmi(7))
print(katta_harf("python"))
print(kichik_harf("PYTHON"))
print(teskari("GitHub"))
print(uzunligi("Python"))
print(yigindi_list([1,2,3,4]))
print(eng_katta([5,7,1,9]))
print(eng_kichik([5,7,1,9]))
print(uzunligi_list([1,2,3]))
print(faktorial(5))
print(daraja(2,5))
print(abs_son(-15))