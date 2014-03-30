from ast_transformers import InvertGenerator, transformAstWith


def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start


def invertibleGenerator(globalEnv):
    """ Add a co method to a generator function, that is the equivalent
    coroutine. """

    def decorator(func):
        func.co = coroutine(
            transformAstWith(globalEnv, [InvertGenerator])(func)
        )
        return func

    return decorator
