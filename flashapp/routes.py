import functools
from flask import render_template, Flask

from flashapp.debug import trace_print, debug_print

trace_print(f"Importing app/routes")


def routes(rule, endpoint, methods=None):
    if not getattr(routes, 'all', None):
        routes.all = list()

    if methods is None:
        methods = ["GET"]

    def decorator(func):
        if not getattr(func, 'orig_func', None):
            func.orig_func = func
        routes.all.append((rule, endpoint, func.orig_func, methods))

        @functools.wraps(func)
        def decorated(*args, **kwargs):
            trace_print(f"Calling decorated function {func}, {args} {kwargs}")
            return func(*args, **kwargs)
        return decorated

    return decorator


@routes('/', 'index')
@routes('/index', 'index')
def _index():
    user = {'username': 'David Christ'}
    return render_template('index.htm', title='Home', user=user)


@routes('/hello', 'hello', methods=["GET", "POST"])
def _hello():
    return f'Hello, World!'


def add_routes(app: Flask):
    for route in routes.all:
        debug_print(f"Adding route: {route}")
        *route, methods = route
        app.add_url_rule(*route, methods=methods)
