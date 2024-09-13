import pytest
import triangle

# first test
def test_triangle():
    a, b, c = 3, 4, 5 # triangle sides 
    tri = triangle.Triangle(a,b,c)
    expected = True
    actual = tri.is_triangle()
    type = tri.get_triangle_type()
    assert expected == actual # Assert if true test
    print(type)

# test right angled triangle (RAT)
def test_right_triangle():
    a, b, c = 3, 4, 5
    tri = triangle.Triangle(a,b,c)
    expected = triangle.longDesc["RAT"]
    actual = tri.is_triangle()
    assert expected != actual # Assert if true test

# default
if __name__ == "__main__":
    test_triangle()  
    test_right_triangle()