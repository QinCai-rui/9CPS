EXPRESSION_TO_CALCUATE = input("Enter an expression to calculate **SEPARATE ELEMENTS USING SPACES**: ").split(" ")
print(EXPRESSION_TO_CALCUATE)
OPERATORS = ["+", "-"]

def calculate_expression(expression):
    while len(expression) > 1:
        # Find the first operator in the expression
        for i in range(len(expression)):
            if expression[i] in OPERATORS:
                # Perform the operation
                if expression[i] == "+":
                    result = int(expression[i - 1]) + int(expression[i + 1])
                elif expression[i] == "-":
                    result = int(expression[i - 1]) - int(expression[i + 1])
                
                # replace the operator and operands with the result
                expression = expression[:i - 1] + [str(result)] + expression[i + 2:]
                break
    return int(expression[0])

if __name__ == "__main__":
    result = calculate_expression(EXPRESSION_TO_CALCUATE)
    print(f"Final result: {result}")
