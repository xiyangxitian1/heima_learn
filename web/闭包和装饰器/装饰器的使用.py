class function_wrapper(object):

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)


class User(object):

    # @yanLogin2  # TypeError: 'classmethod' object is not callable
    @function_wrapper
    @classmethod
    def comment2(cls):
        print("发表评论")


if __name__ == '__main__':
    user = User()
    # user.comment = yanLogin(user.comment)
    # user.comment()
    User.comment2()
