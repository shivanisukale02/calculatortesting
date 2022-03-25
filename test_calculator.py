import calculator
import unittest

class Calculator(unittest.TestCase):
    def test_add1(self):
        x=5
        y=3
        result=add(x,y)
        self.assertEqual(result,x+y)

    def test_sub1(self):
        x=5
        y=3
        result=sub(x,y)
        self.assertEqual(result,x-y)

    def test_mul1(self):
        x=5
        y=3
        result=mul(x,y)
        self.assertEqual(result,x*y)

    def test_div1(self):
        x=5
        y=3
        result=div(x,y)
        self.assertEqual(result,x/y)

if __name__=="__main__":
    unittest.main()
