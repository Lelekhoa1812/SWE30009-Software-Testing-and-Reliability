class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        # Check if the given sides can form a triangle
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def get_triangle_type(self):
        if not self.is_triangle():
            return "Not a triangle"
        elif self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        elif self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2:
            return "Right-Angled"
        else:
            return "Scalene"

# Define descriptions for types of triangles
longDesc = {
    "RAT": "Right-Angled"
}
