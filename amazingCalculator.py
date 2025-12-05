class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(result)
        return result

    def previous_result(self):
        if self.history:
            return self.history[-1]
        return None

    def multiply(self, a, b):
        result = a * b
        self.history.append(result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


## This is a not related Commit, remenber how to just fetch one commit without all the others.

## If you feel lost just see this video it will help you: https://www.youtube.com/watch?v=dQw4w9WgXcQ
