import logging

logging.basicConfig(
    level=logging.WARNING,
    filename="logs.log",
    filemode="w",
    format="We have some error: %(asctime)s : %(levelname)s : %(message)s",
)

class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            logging.error(f"add({a}, {b}) failed: {e}")
            raise

    def subtract(self, a, b):
        try:
            return a - b
        except Exception as e:
            logging.error(f"subtract({a}, {b}) failed: {e}")
            raise

    def multiply(self, a, b):
        try:
            return a * b
        except Exception as e:
            logging.error(f"multiply({a}, {b}) failed: {e}")
            raise

    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a / b
        except Exception as e:
            logging.error(f"divide({a}, {b}) failed: {e}")
            raise

    def maximum(self, a, b):
        try:
            return a if a >= b else b
        except Exception as e:
            logging.error(f"maximum({a}, {b}) failed: {e}")
            raise

    def minimum(self, a, b):
        try:
            return a if a <= b else b
        except Exception as e:
            logging.error(f"minimum({a}, {b}) failed: {e}")
            raise

    def percent(self, number, percent):
        """Повертає percent% від number"""
        try:
            return number * percent / 100
        except Exception as e:
            logging.error(f"percent(number={number}, percent={percent}) failed: {e}")
            raise

    def power(self, number, degree):
        try:
            return number ** degree
        except Exception as e:
            logging.error(f"power(number={number}, degree={degree}) failed: {e}")
            raise