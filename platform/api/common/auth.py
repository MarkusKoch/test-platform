from functools import wraps

auth_bp = object()


def protect(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
            # do something

        return func(*args, **kwargs)

    return decorated_view
