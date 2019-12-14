def add_two_numbers(n1, n2):
    '''
    This function takes two parameters and
    adds them up using the + operator
    '''
    return n1 + n2

def multiply_two_numbers(n1,n2):
    '''
    This function multiplies two numbers
    using the function add_two_numbers
    '''
    multi=0
    for i in range (n2):
        multi=add_two_numbers(multi,n1)
    return multi

if (__name__ == "__main__"):
    def test_multiply_two_numbers():
        assert multiply_two_numbers (2,3) == 6
        assert multiply_two_numbers (12,10) == 120
        assert multiply_two_numbers (13,13) == 169
        assert multiply_two_numbers (100,100) == 10000

    def test_my_module():
        test_multiply_two_numbers()
    test_my_module()
