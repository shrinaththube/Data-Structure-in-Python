'''
Created on Jul 28, 2016

@author: Shrinath Thube
'''
from leetCodeProblems import maxHistrogramArea # THis code is under test
import unittest


class HistoTest(unittest.TestCase):
    pair = (  ([1,2,1,3,2,4],6),  ([1,2,3,2],6) , ([1,1,1,1],4) )

    def testMaxRecatangleArea(self):
        #print "testMaxRecatangleArea"
        for histo, area in self.pair:
            result = maxHistrogramArea.maxRecatangleArea(histo)
            self.assertEqual(area, result, result)

class BadInputHistoTest(unittest.TestCase):
    
    def testMaxRectangleAreaEmpty(self):
        #print "testMaxRectangleAreaEmpty"
        result = maxHistrogramArea.maxRecatangleArea([])
        self.assertEqual(None, result, result)
        
    def testMaxRectangleAreaZero(self):
        result = maxHistrogramArea.maxRecatangleArea([0,0,0,0,0])
        self.assertEqual(0, result, result)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()