# Your task is to write a function which returns the sum of following series upto nth term(parameter).
#
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
#
# You need to round the answer upto 2 decimal places and return it as String.
# If the given value is 0 then it should return 0.00
# You will only be given Natural Numbers as arguments.
# Examples:
#
# SeriesSum(1) => 1 = "1"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

# 1 = 1
# 2 = 1 / 4
# 3 = 1 / 7

def series_sum(n):
    n = int(n)
    if n == 0:
        return 0.00
    else:
        new_n = 0
        i = 1
        while i <= n:
            new_n = new_n + ( 1.0 / (1 + (i - 1) * 3 ))
            i += 1
        return "%.2f" % new_n
