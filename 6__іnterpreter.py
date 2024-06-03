import re

class Expression:
    def interpret(self, context):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) * self.right.interpret(context)


class Divide(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) / self.right.interpret(context)


class Parser:
    def parse(self, expression):
        tokens = re.findall(r'\d+|[+*/()-]', expression)
        return self._parse_expression(tokens)

    def _parse_expression(self, tokens):
        if not tokens:
            raise ValueError("Порожній вираз")
        
        token = tokens.pop(0)
        
        if token.isdigit():
            left = Number(int(token))
        elif token == '(':
            left = self._parse_expression(tokens)
            tokens.pop(0)  # Видалити ')'
        else:
            raise ValueError(f"Неочікуваний токен: {token}")
        
        if not tokens:
            return left
        
        token = tokens[0]
        
        if token in '+-*/':
            operator = tokens.pop(0)
            right = self._parse_expression(tokens)
            if operator == '+':
                return Add(left, right)
            elif operator == '-':
                return Subtract(left, right)
            elif operator == '*':
                return Multiply(left, right)
            elif operator == '/':
                return Divide(left, right)
        
        return left


expression = "(3 + 5) * 2"
parser = Parser()
parsed_expression = parser.parse(expression)
result = parsed_expression.interpret(None)
print(f"Результат виразу '{expression}' дорівнює {result}")
