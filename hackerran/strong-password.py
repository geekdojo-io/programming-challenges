# Problem: https://www.hackerrank.com/challenges/strong-password/problem

def check_condition(c, condition, lookup, other_chars):
    if c in lookup:
        if condition:
            other_chars = max(0, other_chars - 1)
        else:
            condition = True
    return condition, other_chars

def calculate_minnumber(has_number, has_lower, has_upper, has_special, other_chars):
    res = 0
    if not has_number:
        res += 1
    if not has_lower:
        res += 1
    if not has_upper:
        res += 1
    if not has_special:
        res += 1
    return res + other_chars

def minimumNumber(n, password):
    has_number, has_lower, has_upper, has_special = False, False, False, False
    other_chars = 2
    for c in password:
        has_number, other_chars = check_condition(c, has_number, "0123456789", other_chars)
        has_lower, other_chars = check_condition(c, has_lower, "abcdefghijklmnopqrstuvwxyz", other_chars)
        has_upper, other_chars = check_condition(c, has_upper, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", other_chars)
        has_special, other_chars = check_condition(c, has_special, "!@#$%^&*()-+", other_chars)
    print(has_number, has_lower, has_upper, has_special, other_chars)
    return calculate_minnumber(has_number, has_lower, has_upper, has_special, other_chars)

def test_simple():
    assert minimumNumber(3, 'Ab1') == 3
    assert minimumNumber(11, '#HackerRank') == 1

if __name__ == '__main__':
    test_simple()
