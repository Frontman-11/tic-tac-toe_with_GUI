# COMPUTATION PROCESSES
# 1. Ranking of data with the highest value assigned 1
#    and the lowest value assigned the highest list number in {ranking()}
#    The reverse of this process can be done or no sorting at all
# 2. Difference of sorted index values taken by {sum_d2()}
# 3. Square of the difference taken by {sum_d2()}
# 4. Number of terms and evaluation done at {spearman_rs}
#    using the formula 1- (n * sum_d2)/n(n2 - 1)

import math


def ranking(arg, ranked=False):
    """
    Info: Returns list of ranked data set.
    Takes two parameters where arg is the data to be ranked and
    ranked parameter tells whether the data set is already
    ranked. Default value for ranked is boolean False if not given.
    """
    if not ranked:
        ranked_list = []
        in_list = list(arg)
        for _ in range(len(arg)):
            ranked_list.append(None)
        index_incrementer = 1
        for _ in arg:
            max_value = max(in_list)
            max_value_index = in_list.index(max_value)
            ranked_list[max_value_index] = index_incrementer
            in_list[max_value_index] = -1000
            if max_value in in_list:
                continue
            index_incrementer += 1
        return ranked_list
    return list(arg)


def sum_d2(arg1, arg2):
    """
    Info: Returns sum of the square of the difference between the
    two ranked data set.
    """
    d2 = []
    for index in range(len(arg1)):
        d2.append(math.pow((arg1[index] - arg2[index]), 2))
    return sum(d2)


def spearman_rs(arg, ranked=False):
    """
    Info: Spearman's ranking returns the strength of monotonic
    relationship between two variables with range -1 =< rs <= 1
    where -1 denotes strong monotonic decreasing and 1 denotes
    strong monotonic increasing.
    """
    try:
        if type(arg) != dict:
            raise TypeError('Invalid data format: Data must be dict and have only two variables')
        elif len(arg.keys()) != 2:
            raise ValueError('Invalid data format: Data must have only two variables')
        else:
            x, y = arg.keys()
        for variable_values in arg.values():
            for data in variable_values:
                if type(data) != int and type(data) != float:
                    raise TypeError('Check carefully, all data must be a real number!')
        if not iter(arg[x]) or not iter(arg[y]):
            raise TypeError('Not iterable: Data must be of the format {x: iterable, y: iterable}')
        n = len(arg[x])
        if n == len(arg[y]):
            x_ranked_list = ranking(arg[x], ranked)
            y_ranked_list = ranking(arg[y], ranked)
            d2 = sum_d2(x_ranked_list, y_ranked_list)
            numerator = 6 * d2
            denominator = math.pow(n, 3) - n
            return 1 - (numerator / denominator)
        return 'Invalid data pair! Check to confirm each dependent variable has a correspondent independent ' \
               'variable. If you mean none use 0 instead of a missing data.'

    except TypeError as err:
        if __name__ == '__main__':
            print(err)
        return err.args[0]
    except ValueError as err:
        if __name__ == '__main__':
            print(err)
        return err

