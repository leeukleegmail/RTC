from utime import localtime


def get_time_json():
    lt = localtime()
    return {
        'year': lt[0],
        'month': lt[1],
        'day': lt[2],
        'hour': lt[3],
        'minutes': lt[4],
        'seconds': lt[5]
    }
