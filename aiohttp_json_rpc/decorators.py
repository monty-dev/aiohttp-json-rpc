def raw_response(function=None):
    def decorator(function):
        function.raw_response = True

        return function

    return decorator(function) if function else decorator


def validate(**kwargs):
    def decorator(function):
        if not hasattr(function, 'validators'):
            function.validators = {}

        function.validators.update(kwargs)

        return function

    return decorator
