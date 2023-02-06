class A(object):
    def __init__(self):
        print(self.__dict__)

class B(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        #super().__init__()

class D(A):
   def __init__(self):
        super(self.__class__, self).__init__()
        #super().__init__()

"""
# C is a class which is B that inherits from A
C = type('C', (A,), B.__dict__.copy())
C()
# TypeError: descriptor '__dict__' for 'B' objects doesn't apply to 'C' object
"""
d=D()