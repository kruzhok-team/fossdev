## Задачи 

### Задача 1 

Уберите вложенность из кода ниже без изменения условий:

```python 
#nested
def foo(a, b, c):
    if a > 5:
        if b > 10:
            if c != 6: 
                return a + b + c
    return None
```

### Задача 2

Улучшите читаемость кода ниже. Для решения примите, что нам нужно импортировать функции `one_function`, `another_function` из `my_module`. Обратитесь к [этой](https://note.nkmk.me/en/python-import-usage/) статье, если вам нужна помощь в оформлении.

```python
import math, pandas as pd, numpy
from my_module import *
```

**Ответ**

Хорошим стилем считается использование импортов каждой сущности отдельно.

```python
import math
import pandas as pd
import numpy
from my_module import (one_function, 
                       another_function)
```

### Задача 3

Улучшите читаемость кода ниже, убрав лишние пробелы и добавив нужные там, где это необходимо. 

```python

def multiply_numbers(a,b, factor= 2):
    """Multiply two numbers with factor."""
    return a*b

x =10
y =5

result = multiply_numbers(x,y)

if result>10 :
    print("Result is greater than 10.")
```

**Ответ**

Мы должны поправить несколько моментов.
    * Вокруг арифметических, логических операторов есть пробелы, например, (`a * b`, `x = 10` и `y = 5`), что упрощает идентификацию выполняемой операции. Вокруг оператора присваивания пробелы также ставятся, кроме случаев использования при объявлении функции.
    * Перед двоеточием в условном операторе пробела нет, что улучшает связность кода.
    * После запятой, которая разделяет аргументы функции, мы ставим пробел.
    
```python
def multiply_numbers(a, b, factor=2):
    """Multiply two numbers."""
    return a * b

x = 10
y = 5

result = multiply_numbers(x, y)

if result > 10:
    print("Result is greater than 10.")
```

### Задача 4

Улучшите именование переменных, функций и классов. Используйте CamelCase для классов и разделение подчеркиванием для функций.

**Фрагмент 1**

```python
# Bad style
def calcrect1(l, w):
    """Calculate the perimeter of a rectangle."""
    return (l + w) * 2

def calcrect2(l, w):
    """Calculate the area of a rectangle."""
    return l * w


class my_class:
    def __init__(self, n):
        self.n = n
    
    def pn(self):
        print(f"My name is {self.n}.")
```

**Ответ 1**

Мы должны поправить имена переменных, чтобы они не состояли из одной буквы. Имя функции сокращено и не дает понимания того, что функция делает: `calcrect1` не дает понимания, что именно будет рассчитано.

```python
def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return (length + width) * 2


class MyClass:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(f"My name is {self.name}.")
```

**Фрагмент 2**

Для примера ниже предполагается, что база данных хранит данные о покупателе и его карточку.

```python
# Bad style
maxAttempts = 5

def circleArea(r):
    """Calculate the area of a circle."""
    return 3.14 * r ** 2

class customer_db:
    def __init__(self):
        self.cust = []
        self.cars = {}
    
    def add_cust(self, c):
        self.cust.append(c)
    
    def get_cust_count(self):
        return len(self.cust)

    def add_cust_car(self, c, cc):
        self.cars[c] = cc
```

**Ответ 2**

Часто бывает, что сокращение начинает читаться как другое слово. Так в примере карточка (card) стала машиной (car).

```python
MAX_RETRY_ATTEMPTS = 5

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return 3.14 * radius ** 2

class CustomerDatabase:
    def __init__(self):
        self.customers = []
        self.cards = {}
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def get_customer_count(self):
        return len(self.customers)

    def add_customer_card(self, customer, card):
        self.cards[customer] = card
```

**Фрагмент 3**

Бывает, что мы называем объект, используя какие-то свои ассоциации или что-то еще, что делает название понятным для нас, но будет сбивать с толку других разработчиков. Поправьте код ниже чтобы, каждый мог понять, что мы создали класс Кольцо. Поправьте название методов.

```python
# Bad style (objects named improperly)
class Donut:
    def __init__(self, material, size):
        self.material = material
        self.size = size
    
    def get_ingredient(self):
        return self.material
    
    def get_circle(self):
        return self.size

new_donut = Donut("gold", "medium")
print(new_donut.get_ingredient())  # Output: gold
print(new_donut.get_circle()) 
```

**Ответ**

```python
class Ring:
    def __init__(self, material, size):
        self.material = material
        self.size = size
    
    def get_material(self):
        return self.material
    
    def get_size(self):
        return self.size

new_ring = Ring("gold", "medium")
print(new_ring.get_material())  # Output: gold
print(new_ring.get_size())    
```

### Задача 5 

Напишите комментарии к функции, чтобы дать понимание о ее работе. Попробуйте описать функцию, которая рассчитывает прибыль по инвестициям.

**Фрагмент 1**

```python
def calculate_interest(principal, rate, time):
    n = 1
    final_amount = principal * (1 + rate / n) ** (n * time)
    return final_amount


# Example usage
principal_amount = 1000.0
annual_interest_rate = 0.05  
investment_time = 5  
final_amount = calculate_interest(principal_amount, annual_interest_rate, investment_time)
print(f"The final amount after {investment_time} years is: ${final_amount:.2f}")
```


**Ответ**

```python
# Less obvious code that benefits from comments

def calculate_interest(principal, rate, time):
    """Calculate compound interest for the given parameters.

    Args:
        principal (float): The principal amount (initial investment).
        rate (float): The annual interest rate in decimal form (e.g., 0.05 for 5%).
        time (int): The time period in years.

    Returns:
        float: The final amount after compounding the interest.
    """
    # Formula for compound interest: A = P(1 + r/n)^(nt)
    # A: Final amount after compounding the interest
    # P: Principal amount
    # r: Annual interest rate
    # t: Time period in years

    # In this implementation, we'll assume interest is compounded annually (n=1)
    n = 1

    # Calculate the final amount after compounding interest
    final_amount = principal * (1 + rate / n) ** (n * time)

    return final_amount

# Example usage
principal_amount = 1000.0
annual_interest_rate = 0.05  # 5% interest rate
investment_time = 5  # 5 years
final_amount = calculate_interest(principal_amount, annual_interest_rate, investment_time)
print(f"The final amount after {investment_time} years is: ${final_amount:.2f}")

```

**Фрагмент 2**

Часто бывает, что мы реализуем логику, которая специфична для конкретной ситуации и может не встречаться за ее пределами. Например, поведение функции `sum` для чисел очевидно, она вернет суммы переданных в нее аргументов-чисел. Но давайте представим подсчет очков в настольной игре-ходилке, где количество очко зависит от тех клеток, которые прошла фишка игрока. Допустим, клетки с номером, кратным трем, содержат сундуки, которые увеличивают вклад на этой клетке в два раза. А на клетках с номером, кратным двум, находятся разбойники, которые уменьшают вклад на этой клетке в два раза.

```python
def calculate_player_total(data):
    total = 0

    for item in data:
        if item % 3 == 0:
            total += item * 2
        elif item % 2 == 0:
            total += item / 2
        else:
            total += item

    return total
```

**Ответ**

```python
def calculate_player_total(data):
    """Process the given list of integers, that presents cells ID. 
    
    Contribution of the cell to the total is based on divisibility of cell ID.

    Args:
        data (list): A list of integers.

    Returns:
        int: The total value after processing the list.
    """
    total = 0

    for item in data:
        if item % 3 == 0:
            # if cell id is divisible by 3, it is chest, double the value and add to 'total'
            total += item * 2
        elif item % 2 == 0:
            # if cell id is divisible by 2, it is robber, halve the value and add to 'total'
            total += item / 2
        else:
            # For other numbers, add the number to 'total'
            total += item

    return total
```