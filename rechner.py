number1 = int(input("Please say yourfirst number:"))
number2 = int(input("Please say your second number:"))
type = input("Please say wich type of invoice it should be. Multiplikation (m) or division (d) or subtraktion (s) ")
if type ==  "m":
    print(number1 * number2)
elif type == "d":
    print(number1 / number2)
elif type == "s":
    print(number1 - number2)

