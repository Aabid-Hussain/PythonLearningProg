# Write a Python program to convert an integer to a roman numeral.

class py_solution:
    def int_to_Roman(self, num):

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        romanNum = ''
        count = 0
        while num > 0:
            for _ in range(num // val[count]):
                romanNum += syb[count]
                num -= val[count]
            count += 1
        return romanNum


print(py_solution().int_to_Roman(77))
print(py_solution().int_to_Roman(21))
