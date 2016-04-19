class MethodCallCount(object):
    """
    Creates a proxy class wrapper around a function/method.
    Handy for when wanting to see if or how many times a function/method
    was called.
    
    For example:
    
    class Foo(object):
        def bar():
            print 'foo-bar'
    
    foo = Foo()
    foo.bar = MethodCallCount(foo.bar)
    foo.bar()  # This will print "foo-bar"
    foo.bar()  # This will print "foo-bar"
    print foo.bar.called_count  # This will print "2" because foo.bar was called twice.
    """
    def __init__(self, meth_ref):
        self._ref = meth_ref
        self.called_count = 0

    def __call__(self):
        self.called_count += 1
        self._ref()
