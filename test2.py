import unittest
import main


class TestMain(unittest.TestCase):
    def setup(self):
        print('about to test a function')   #**
    
    
    def test_do_stuff1(self):                                    #test1
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):                                   #test2
        test_param = 'jsfjfsj'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


    def test_do_stuff3(self):                                   #test3
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


    def test_do_stuff4(self):                                   #test4
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    
    def tearDown(self):
        print('cleaning up')    #**

if __name__ == '__main__':   
    unittest.main()


#** these are useful when setting up or tearup test

#Recheck how to do unittest for all the files, it should show 8 tests instead of


# output
# Ran 4 tests in 0.001s

# OK