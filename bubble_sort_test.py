import unittest
import bubblesort as st

class Test_Testvalue(unittest.TestCase):
    def test_smaple(self):
       testList = [4,3,2,1]
       expectedList = testList.copy() 
       expectedList.sort()
       actualList = st.bubblesort(testList)
       self.assertEqual(actualList, expectedList)

    def test_empty(self):
       testList = []
       expectedList = testList.copy() 
       expectedList.sort()
       actualList = st.bubblesort(testList)
       self.assertEqual(actualList, expectedList)

    def test_negative(self):
       testList = [-4,-2,-1]
       expectedList = testList.copy() 
       expectedList.sort()
       actualList = st.bubblesort(testList)
       self.assertEqual(actualList, expectedList)
       