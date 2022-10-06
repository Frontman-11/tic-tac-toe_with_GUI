# Test Program to test my correlation program
import unittest
import pearson_r


# import spearman_r


class Test(unittest.TestCase):
    def test_okay(self):
        a = [
            {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 8, 9, 10]}, {'x': (1, 2, 3, 4, 5), 'y': (6, 7, 8, 9, 10)},
            {'x': (1, 2, 3, 4, 5), 'y': [6, 7, 8, 9, 10]}
        ]
        for data in a:
            result = pearson_r.pearson_r(data)
            expectation = 1.0
            self.assertEqual(expectation, result)

    def test_for_iterable_data(self):
        a = [{'a': 'a', 'b': 2}, {'a': [2, 3, '1', 4], 'b': [2, 4, 5, 6]}]
        for item in a:
            result = pearson_r.pearson_r(item)
            expectation = 'Check carefully, all data must be a real number!'
            self.assertEqual(expectation, result)

    def test_for_invalid_input(self):
        a = ['gibberish', 23, [23, 45], (23, 78), [{'x': 2, 'y': 3, 'z': 4}, {'x': 2}], None]
        for invalid_input in a:
            result = pearson_r.pearson_r(invalid_input)
            expectation = 'Invalid data format: Data must be dict and have only two variables'
            self.assertEqual(expectation, result)

    def test_unequal_num_of_variable_data(self):
        a = {'a': [2, 3, 4], 'b': [2, 4, 5, 6]}
        result = pearson_r.pearson_r(a)
        expectation = '''
        Invalid data pair! check to confirm each dependent variable
        has a correspondent independent variable. If you mean none 
        use 0 instead of a missing data.
        '''
        self.assertEqual(expectation, result)


if __name__ == '__main__':
    unittest.main()
