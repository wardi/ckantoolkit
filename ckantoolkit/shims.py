
class HelpersNoMagic(object):
    """
    Access helper.functions as attributes, but raise AttributeError
    for missing functions instead of returning null_function

    adapted from ckan/config/environment.py:_HelpersNoMagic
    """
    def __getattr__(self, name):
        import pylons
        h = pylons.config['pylons.h']

        fn = getattr(h, name)
        if fn == h.null_function:
            raise AttributeError("No helper found named '%s'" % name)
        return fn
