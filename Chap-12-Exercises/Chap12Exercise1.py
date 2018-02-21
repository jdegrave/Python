from Triangle import Triangle


def main():
    side1, side2, side3 = eval(input("Enter the length of all 3 sides of the triangle, separated by commas: "))
    color = input("Enter the color of the triangle: ")
    filled = bool(int(input("Enter 1 if the triangle is filled, or a zero(0) if it's not filled: ")))
    new_triangle = Triangle(color, filled, side1, side2, side3)
    new_triangle.print_triangle()
    print("The Triangle's area is: " + format((new_triangle.get_area()), ".3f"))
    print("The Triangle's perimeter is: " + str(new_triangle.get_perimeter()))


main()