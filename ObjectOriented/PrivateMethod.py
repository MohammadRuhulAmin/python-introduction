
class PrivateMethod:

    # def __init__(self):pass
    def public_method(self):
        self.__private_method()
    def __private_method(self):
        print('Private Method cannot be  called outside of a class')
        print('It can only be called inside of a class')
        print('##')

pm1 = PrivateMethod()
pm1.public_method()
