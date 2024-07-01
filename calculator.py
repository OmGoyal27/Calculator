def identifySymbol(symbol: str, num_1: int, num_2: int):
    if symbol == "+":
        return Perform.add(num_1, num_2)
    if symbol == "-":
        return Perform.subtract(num_1, num_2)
    if symbol == "*":
        return Perform.multiply(num_1, num_2)
    if symbol == "/":
        return Perform.divide(num_1, num_2)


class Perform():

    def add(num_1: int, num_2: int) -> int:
        return num_1 + num_2

    def subtract(num_1: int, num_2: int) -> int:
        return num_1 - num_2

    def multiply(num_1: int, num_2: int) -> int:
        return num_1 * num_2

    def divide(num_1: int, num_2: int) -> int:
        return num_1 / num_2

    def ask(question):
        return input(question)

def main():
    question = Perform.ask("Enter your calculation to perform: ")
    responses = question.split()
    number_1 = float(responses[0])
    symbol = responses[1]
    number_2 = float(responses[2])
    print(identifySymbol(symbol, number_1, number_2))
    helper()


def helper():
    try:
        main()
    except Exception as e:
        exit("It is not a valid input. Please enter a valid input.\nAn example of a valid input is like 23(First number) *(symbol) 3(second number)")
        
if __name__ == '__main__':
    helper()