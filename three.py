# import os
import datetime
# import flat_generator2


def logger(path):

    with open(path, 'a') as f:
        f.write(str(datetime.datetime.now()) + '\n')


    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a') as f:
                f.write(old_function.__name__ + '\n')
                for item in args:
                    f.write(str(item) + '\n')
                for key, value in kwargs.items():
                    f.write(str(value) + '\n')
                    f.write(str(result) + '\n')

            return result

        return new_function

    return __logger


if __name__ == '__main__':

    pass