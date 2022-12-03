# https://realpython.com/python-testing/#testing-your-code
# MO5 Programming Assignment - Testing Your Code
# Nate Orona

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"
    
def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"
    
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print('Everything passed')