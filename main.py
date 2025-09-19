import unittest

def fib(iterations):
    a = 0
    b = 1
    fib = []

    for _ in range(iterations):
        fib.append(a)
        temp = a + b
        a = b
        b = temp
    return fib

def fib2(iterations):
    a = 0
    b = 1
    fib = []

    for _ in range(iterations):
        fib.append(a)
        temp = a + b
        a = b
        b = temp
    return fib


# class TestFib(unittest.TestCase):
#     def test_first_10(self):
#         expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#         self.assertEqual(fib(10), expected)



if __name__ == "__main__":
    unittest.main()
