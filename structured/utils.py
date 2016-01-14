import functools


def pipe(*a):
    """
    Specify several functions which will be
    applied to value one-by-one (in chain).

        result = pipe(a, b, c)(1)

    equal to:

        result = c(b(a(1)))

    """
    funcs = list(a)
    funcs.reverse()

    def wrap(*args):
        result = list(args)
        while funcs:
            func = funcs.pop()
            n_result = []
            result = func(*result)
            if isinstance(result, (list, tuple)):
                for elem in result:
                    n_result.append(pipe(funcs)(elem))
                result = n_result
            else:
                import ipdb; ipdb.set_trace()
                result = [func(*result)]

            #if not isinstance(result, (tuple, list)):
            #    result = [result]

        return result

    return wrap
