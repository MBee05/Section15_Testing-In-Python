import unittest
import main


class TestMain(unittest.TestCase):
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


# unittest.main()



# def test_do_stuff(self):                                   
#         test_param = ''
#         result = main.do_stuff(test_param)                  #if i rename 'main' into script then have to change in every test then have to mention the if part below
#         self.assertEqual(result, 'please enter number')

if __name__ == '__main__':                                   #this is neccessary if we change name of the file
    unittest.main()
