import sys
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, backtrace=True, diagnose=True)

def func(a, b):
  return (a / b) + func(a, b-1)
    
def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("Division by zero error!")

nested(1)
