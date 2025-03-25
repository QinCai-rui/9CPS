EXPRESSION_TO_CALCUATE = input("Enter an expression to calculate **SEPARATE ELEMENTS USING SPACES**: ").split(" ")
print(EXPRESSION_TO_CALCUATE)
OPERATORS = ["+", "-", "*", "/"]

def calculate_expression(expression):
    def perform_operation(op, left, right):
        """Perform the operation based on the operator."""
        if op == "*":
            return float(left) * float(right)
        elif op == "/":
            return float(left) / float(right)
        elif op == "+":
            return float(left) + float(right)
        elif op == "-":
            return float(left) - float(right)

    for op in ["*", "/"]:
        while op in expression:
            i = expression.index(op)
            result = perform_operation(op, expression[i - 1], expression[i + 1])
            expression = expression[:i - 1] + [str(result)] + expression[i + 2:]

    for op in ["+", "-"]:
        while op in expression:
            i = expression.index(op)
            result = perform_operation(op, expression[i - 1], expression[i + 1])
            expression = expression[:i - 1] + [str(result)] + expression[i + 2:]

    return float(expression[0])  # Return the final result as a float

if __name__ == "__main__":
    result = calculate_expression(EXPRESSION_TO_CALCUATE)
    print(f"Final result: {result}")
