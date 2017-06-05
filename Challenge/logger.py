'''
1. define function logger_func(func)
2. to create log file we need to import logging package.
2. create log file name and log data as debugging =INFO
3. use wrapper function to wrap the data
4. return wrapper function

'''

def logger_func(log_func):
    import logging

    # create log file
    logging.basicConfig(filename='{}.log'.format(log_func.__name__),
                        level= logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and keywords: {}'.format(args, kwargs))
        return log_func(*args, **kwargs)

    return wrapper

@logger_func
def addition(name, age):

    print("Name: {}".format(name))
    print("Age: {}".format(age))


addition('Aabid', 25)