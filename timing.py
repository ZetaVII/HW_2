import time

def calculate_time(func):
    """
    Calculates the amount of time it takes for this decorator to run.

    Parameters
    ----------
    func :  function()
        The calling function of this decorator: it makes the decorator sleep for 2 seconds

    """
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()

        x = t2 - t1

        print(f"Total time {x}")
    return wrapper

@calculate_time
def myfunc():
    time.sleep(2)

if __name__ == '__main__':
    myfunc()
    