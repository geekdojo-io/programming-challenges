# Problem: https://www.hackerrank.com/challenges/strong-password/problem

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
                
def find(c, has_c, chars, other):
    if c in chars:
        if has_c:
            other = max(0, other - 1)
        else:
            has_c = True
    return has_c, other

def calculate_minimum(conditions, other):
    res = 0
    for i, val in enumerate(conditions):
        if not val:
            res += 1
    return res + other

def minimumNumber(n, password):
    requirements = [numbers, lower_case, upper_case, special_characters]
    conditions = [False, False, False, False]
    other = 6 - len(requirements) # minimum legnth of 6 minus four required fields is 2.
    for c in password:
        for i, status in enumerate(conditions):
            conditions[i], other = find(c, status, requirements[i], other)
    return calculate_minimum(conditions, other)

def test_simple():
    assert minimumNumber(3, 'Ab1') == 3
    assert minimumNumber(11, '#HackerRank') == 1

if __name__ == '__main__':
    test_simple()
