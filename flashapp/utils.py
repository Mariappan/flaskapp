import functools

from flashapp import trace_print


def routes(rule, endpoint, methods=None):
    if not getattr(routes, "all", None):
        routes.all = list()

    if methods is None:
        methods = ["GET"]

    def decorator(func):
        print(f"Routes called for {func}")
        if not getattr(func, "orig_func", None):
            func.orig_func = func
        routes.all.append((rule, endpoint, func.orig_func, methods))

        @functools.wraps(func)
        def decorated(*args, **kwargs):
            trace_print(f"Calling decorated function {func}, {args} {kwargs}")
            return func(*args, **kwargs)

        return decorated

    return decorator
