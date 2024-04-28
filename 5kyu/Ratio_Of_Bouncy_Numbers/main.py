#!/usr/bin/python3

# Ratio of Bouncy Numbers
# https://www.codewars.com/kata/562b099becfe844f3800000a/

import codewars_test as test

def is_bouncy(n):
    inc = all([int(n[i]) <= int(n[i+1]) for i in range(0, len(n)-1)])
    dec = all([int(n[i]) >= int(n[i+1]) for i in range(0, len(n)-1)])
    return not inc and not dec

def bouncy_ratio(ratio):
    rat, bouncy, total = 0.0, 0, 0

    while rat < ratio:
        total += 1
        if is_bouncy(str(total)): bouncy += 1
        rat = bouncy / total
        
    return total

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(bouncy_ratio(0.1), 132, 'A 10% bouncy ratio should be reached by 132')
        test.assert_equals(bouncy_ratio(0.15), 160, 'A 15% bouncy ratio should be reached by 160')
        test.assert_equals(bouncy_ratio(0.5), 538, 'A 50% bouncy ratio should be reached by 538')
        test.assert_equals(bouncy_ratio(0.75), 3088, 'A 75% bouncy ratio should be reached by 3088')
        test.assert_equals(bouncy_ratio(0.9), 21780, 'A 90% bouncy ratio should be reached by 21780')
