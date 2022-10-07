# A PROGRAM TO CALCULATE CORRELATION USING PEARSON'S
# PRODUCT-MOMENT AND SPEARMAN'S RANKING METHODS
import math


def sum_x_sum_y(arg):
    """
    Info: Returns the summation of both x and y
    """
    container = []
    for variable in arg.values():
        container.append(sum(variable))
    return {'summation_x': container[0], 'summation_y': container[1]}


def sum_xy(arg):
    """
    Info: Returns the summation of the product of x and y
    """
    x, y = arg.keys()
    summation_xy = 0
    for index in range(len(arg[x])):
        summation_xy += (arg[x][index] * arg[y][index])
    return summation_xy


def sum_squared_values(arg):
    """
    Info: Returns a 2 length dictionary which contains the
    summation of the square of both x and y respective values
    """
    container = 0
    result = []
    for variable in arg.values():
        for data in variable:
            container += data * data
        result.append(container)
        container = 0
    return {'summation_x2': result[0], 'summation_y2': result[1]}


def pearson_r(arg):
    """
    Info: Measures the strength of the linear relationship between
    two variables with range -1 =< rs <= 1 where -1 denotes strong
    inverse linear relation and 1 denotes strong direct linear
    relation.
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
        if len(arg[x]) == len(arg[y]):
            nth = len(arg[x])
            summation_x, summation_y = sum_x_sum_y(arg).values()
            numerator = nth * sum_xy(arg) - summation_x * summation_y
            sum_squared_x, sum_squared_y = sum_squared_values(arg).values()
            x_denominator_diff = nth * sum_squared_x - math.pow(summation_x, 2)
            y_denominator_diff = nth * sum_squared_y - math.pow(summation_y, 2)
            denominator = math.sqrt(x_denominator_diff * y_denominator_diff)
            return numerator / denominator
        return 'Invalid data pair! Check to confirm each dependent variable has a correspondent independent variable.' \
               ' If you mean none use 0 instead of a missing data.'
    except TypeError as err:
        if __name__ == '__main__':
            print(err)
        return err.args[0]
    except ValueError as err:
        if __name__ == '__main__':
            print(err)
        return err
