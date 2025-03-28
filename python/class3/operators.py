"""
# Operators

    1. Arithmetic operators

        (+, -, *, /, %, **, //)

    2. Assignment operators

        (=, +=, -=, *=, /=, %=, **=, //=)

    3. Comparison operators

        (==, !=, >, <, >=, <=)

    4. Logical operators

        (and, or, not)

    5. Identity operators

        (is, is not)

    6. Membership operators

        (in, not in)

"""

# 1. Arithmetic operators -->  (+, -, *, /, %, **, //)

    # a = 15
    # b = 2

    # result = a + b
    # result = a - b
    # result = a * b
    # result = a / b
    # result = a % b
    # result = a ** b
    # result = a // b    --> floor division

    # print(result)

# 2. Assignment operators --> (=, +=, -=, *=, /=, %=, **=, //=)

    # a = 5

    # a += 2   # a = a + 2
    # a -= 2   # a = a - 2
    # a *= 2   # a = a * 2
    # a /= 2   # a = a / 2
    # a %= 2   # a = a % 2
    # a **= 2  # a = a ** 2
    # a //= 2  # a = a // 2

    # print(a)

# 3. Comparison operators -->  (==, !=, >, <, >=, <=)

    # age = 17

    # # result = (age == 18)
    # result = (age >= 18)

    # print(result)

# 4. Logical operators -->  (and, or, not)

    # and

    # (True)  and (True)   ----> True
    # (True)  and (False)  ----> False
    # (False) and (True)   ----> False
    # (False) and (False)  ----> False

        # age = 22

        # result = (age >= 18) and (age == 18)

        # print(result)

    # or

    # (True)  or (True)   ----> True
    # (True)  or (False)  ----> True
    # (False) or (True)   ----> True
    # (False) or (False)  ----> False

        # age = 18

        # result = not((age >= 18) or (age == 18))

        # print(result)

# 5. Identity operators -->  (is, is not)

        # x = ["apple", "banana"]
        # y = ["apple", "banana"]

        # z = x

        # print(x)
        # print(y)
        # print(z)

        # print(x is y)
        # print(x is not y)

# 6. Membership operators  -->  (in, not in)

        # x = ["apple", "banana"]

        # print("banana" in x)
        # print("banana" not in x)