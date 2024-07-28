def mul(x):
    def other(y):
        return x * y

    return other


multi_10 = mul(10)
multi_20 = mul(20)


print(multi_10(3))
print(multi_10(5))

print(multi_20(8))
print(multi_20(9))
