'''
Created on Jul 28, 2016

@author: Shrinath Thube
'''

from leetCodeProblems import convertExcelColumn

import unittest

class Simple(unittest.TestCase):
   
    pair = (('A',1),('B',2),('C',3),('D',4),('E',5),('F',6),('AA',27),("AABBCCDD",8365457520))
   
    def testColumnLetterToNumber(self):
        for col, num in self.pair:
            result = convertExcelColumn.columnLetterToNumber(col)
            self.assertEqual(num, result, result)
        
    def testColumnNumberToLetter(self):
        for col, num in self.pair:
            result = convertExcelColumn.columnNumberToLetter(num)
            self.assertEqual(col, result, result)
        


if __name__ == "__main__":
    unittest.main()