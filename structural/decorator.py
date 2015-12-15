"""
    Copy paste
"""


from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    """a decorated hello world"""
    return "hello world"


print('result:{}   name:{}   doc:{}'.format(hello(), hello.__name__, hello.__doc__))