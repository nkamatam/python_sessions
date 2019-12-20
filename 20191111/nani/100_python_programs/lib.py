pi = 3.14159265
def area (r):
    """
    This fucntion returns the area of a circle
    You need to pass the radius of the circle
    as the parameter
    """
    return( pi * r * r)

def perimeter(r):
    return(2*pi*r)


def test_module():
    print ("Testing the module")
    if (area(5) != 78.5):
        print ("Something is wrong with the area function, please check")
    if (perimeter(1) != 6.28):
        print ("Something is wrong with the perimeter function, please check")

if (__name__ == "__main__" ):
    test_module()


