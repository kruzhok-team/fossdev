# Оформление кода

Если мы хотим создать полезную библиотеку, мы должны позаботиться об оформлении кода, так чтобы его было удобно читать. Для больших проектах с активным сообществом, справедливо утверждение, что код больше читают чем пишут. И если мы хотим участвовать в таком сообществе нужно не только производить фичи, но и хорошо их оформить. Хорошо - это значит общепринятым способом, чтобы другой разработчик не тратил время на понимание того, что вы почему-то решили назвать переменную так как обычно называют класс. Есть интуитивно понятные правила оформления кода, например с использование отступов. Но существуют не такие понятные, например где мы должны переносить строку [до или после знака оператора](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator):

```python 
#wrong
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

#correct    
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

Можно думать о стиле как о минимально необходимом наборе всех возможностей языка программирования по написанию и оформлению кода: даже если мы можем так написать мы не будем в угоду читаемости. Соблюдение стиля не всегда приводит к меньшему количеству кода. Мы можем обратиться к дзену Python и увидим, что там нет строчки про количество кода, поэтому лучше получить более читаемый, явный и простой код, чем короткий, но сложный и в которым происходит что-то неявное. 

```python
import this 

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Используйте отступы

Одним из основных правил хорошего стиля программирования (code style) заключается в том, что разные уровни вложенности стоит выделять при помощи отступов используя знаки пробелов или табуляции. **Работая с кодом в рамках одного файла стоит использовать что-то одно: или пробелы или табуляцию**. 
Если вы попробуете использовать и то, и другое набирая код программы на Python, то интерпретатор выдаст вам сообщение об ошибке. В других языках программирования такая ситуация не вызовет ошибку синтаксиса, однако читать код с отступами приятнее, он легче и быстрее воспринимается разработчиком. Еще больше информации о стиле программирования можно узнать из документа [pep8](https://peps.python.org/pep-0008/). Этот документ содержит множество рекомендаций по оформлению кода на языке Python.

Код без отступов:

```c++
#include <iostream>

#define DEFINE_NAME true

int main() 
{   
//not indented code    
char* name;
if(DEFINE_NAME) 
{
name = (char*) "Name";
std::cout << "Hello, " << name << "!";    
} 
else 
{
std::cout << "Hello World!";    
}
return 0;   
}
```

Код с отступами:

```c++
#include <iostream>

#define DEFINE_NAME true

int main ()
{
  char *name;
  if (DEFINE_NAME)
    {
      name = (char *) "Name";
      std::cout << "Hello, " << name << "!";
    }
  else
    {
      std::cout << "Hello World!";
    }
  return 0;
}

```

В python так же есть ситуации когда отступы не будут вызывать ошибку, например при вызове функции, название и аргументы, которой не помещаются в максимальную длину строки и должны быть перенесены на следующую строку.

```python 
#buity 
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

#not_so_buity
foo = long_function_name(var_one, var_two,
           var_three, var_four)
```

Оба варианта валидны с точки зрения интерпретатора, но первый более читаем. В [разных](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator) ситуациях отступы используются по-разному. Если чувствуете, что участок кода сложен при оформлении обратитесь к руководству по стию 

### Соблюдайте принятую длину строки

В разных языках программирования и в разных проектах может быть принята разная максимальная длина строки. Когда я работал над проектом на Java мы использовали длину строки 120 символов. В python принято умещать код на каждой строке в [79 символов](https://peps.python.org/pep-0008/#maximum-line-length) и комментарии в 72 символа. Отчасти это историческое ограничение, связанное с тем что раньше были маленькие экраны, но даже с появлением широкоформатных экранов от этого элемента форматирования не стали отказываться, так как человеку проще воспринимать не широкие колонки из текста. Во многих изданиями, принято оформлять текст в виде нескольких колонок на одной странице, хотя ничего не мешает сделать занять всю ширину страница. Так же такое подход позволяется разделить экран ноутбука на две области и быть уверенными что код войдет по ширине в обе, и шрифт не будет слишком мелким. Не заставляйте своих коллег скролить горизонтально, это не круто.

Cуществуют разные способы разбиение длинной строки на несколько коротких. Они будут зависеть от языка программирования и от конкретного участка кода, который нужно перенести на другую строку. 

```python
if super_long_condition_variable == True and another_condition_with_yet_longer_name == False:
    pass
    # do stuff here
```

Просто перенести второе условие на новую строку нельзя будет ошибка:

```python
if super_long_condition_variable == True and 
   another_condition_with_yet_longer_name == False:
    pass
    # do stuff here

...
    if super_long_condition_variable == True and
                                                 ^
SyntaxError: invalid syntax
```

Можно окружить условие скобками. Скобки имеют более высокий приоритет чем перенос поэтому пример внизу выполнится корректно

```python
if (super_long_condition_variable == True and 
    another_condition_with_yet_longer_name == False):
    pass
    # do stuff here
```

Можно использовать явный способ сказать интерпретатору, что строка ниже является продолжением текущей строки:

```python
if super_long_condition_variable == True and \
   another_condition_with_yet_longer_name == False:
    pass
    # do stuff here
```
В математических выражениях удобнее использовать скобки:

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

Так же как и при вызове функции.

```python
long_function_name(var_one, var_two, var_three, var_four,
                   var_six, var_seven, var_eight)
```

### Используйте фигурные скобки правильно

В С++ и в других языках, которые используют фигурные скобки для выделение блоков кода, мы можем не писать фигурные скобки у условного оператора или оператора цикла. 

```C++
int age;
//get age from user
if(age >= 18) 
    allow_18plus_content();
else 
    disable_18plus_content();
```

Но лучше всегда их использовать даже если Вы полностью уверены, что в тело условия больше не будет добавлено ни одной строчки. Опять же использование единого оформления позволит не отвлекать и читать код быстрее. 

```C++
int age;
//get age from user
if(age >= 18) 
{
    allow_18plus_content();
}
else 
{
    disable_18plus_content();
}
```

Есть также альтернативно оформление, которое на мой взгляд выглядит более приятно при условии использования отступов. Уточните какой из эти способов принят в команде к которой вы подключаетесь. Но скобки должны быть всегда.

```C++
int age;
//get age from user
if(age >= 18) {
    allow_18plus_content();
} else {
    disable_18plus_content();
}
```

### Именуйте объекты правильно

Среди начинающих программистов и своих студентов я часто встречаю именование переменных либо одним ничего не значащим символом, любо транслитом. 

```python
def srednee(znacheniya):
    return sum(znacheniya) / len(znacheniya)
```

Как первое так и второе плохо. Именование с использование транслита, не позволит другому разработчику понять, что это за функция и что она делает. Еще одна частая проблема, которая встречается при именовании объектов, это оставление контекста, который использовался при разработке. Например мы работаем с датчиком который предоставляет температуру (`temperature`) и давление (`pressure`). Мы хотим как то обработать данные, например найти среднее значение. Мы начинаем разработку и выбираем использовать температуру, что бы проверять нашу работу. Мы правильно пишем название функции, а аргументом передаем список снятых значений температуры, вроде бы все нормально. 

```python
def average(temperature):
    return sum(temperature) / len(temperature)

vals = measure_temperature()
average_temperature = average(vals)
```

Мы оттестировали функции и довольны ее работой и теперь готовы применить ее к показаниям давления. И все ... работает. Мы счастливы и коммитим свою работу. А разработчик, который будет потом разбираться в нашем коде долго не сможет понять почему температура ведет себя как давление.

```python
vals = measure_pressure()
average_pressure = average(vals)
```

Используйте несколько слов там где это нужно, например мы могли просто назвать функцию `pressure()`.  И что "давление", измерить, прочитать из файла, забрать из базы данных, что я делаю с давлением? Тот вариант, который использовали мы `measure_pressure()` сразу даст нам  понимание что это функция измерения давления и скорее всего она работает с датчиком, а не получает давление, каким-то другим способом. Здесь можно прокомментировать, что непонятно что эта функция дает ряд значений, а не одно. Мы можем согласиться с этим и добавить эту информацию к названию функции или сделать это через обязательные аргументы.
Существуют два основных способа именования переменных и функций через подчеркивания (`measure_pressure`) и CamelCase (`measurePressure`). На мой взгляд через подчеркивание удобнее, так как мы используем название классов через заглавные буквы `PressureSensor` и при беглом чтении разница в одной заглавной (для классов) или строчной (для переменных и функций) менее заметна чем при использовании подчеркиваний.
При выборе имени для переменной используйте существительные, а для функции глагол.

### Придерживаться определенного подхода

Этот пункт, не относится напрямую к стилю кода. И это не является строгим требованием. Код состоит из определенных конструкций, и неплохая идея пользоваться одним подходом для написания, одной и той же функциональности. Например если нам нужно открыть файл мы можем сделать несколькими способами:


```python
with open(filename) as f:
    #do something
```

или

```python 
f = open(filename)
#do something
f.close()
```

Это простой пример, и есть соглашение о том что конструкция с `with` лучше. Но в других ситуациями когда нет устоявшегося способа написать участок кода, вам придется приходить к этому внутри команды. То же самое касается и подходов к программированию. Например, Python позволяет использовать основные парадигмы программирования: объектно-ориентированную, процедурную, функциональную и императивную. Мы можем смешивать их в рамках одной программы и это не будет ошибкой. Есть решения где использования другого подхода оправдано: все так делают и решение более красивое и явное, чем при использовании другого подхода. Однако использование другого подхода только ради того, чтобы его использовать не будет хорошей идеей и ухудшит читаемость кода.

### Избегайте вложенности (Flat is better than nested)

Этот пункт взять из дзена Python и ему можно легко дать количественную оценку - уровни вложенность можно посчитать. Возьмем код ниже: 

```python 
#nested
def foo(a, b, c):
    if a > 5:
        if b > 10:
            if c != 6: 
                return a + b + c
    return None
```

И уберем вложенность:

```python
def foo(a, b, c):
    if a <= 5:
        return None
    if b <= 10:
        return None
    if c != 6: 
        return None
    return a + b + c
```


Задание: попробуйте прогнать код с вложенностью через autopep8 и проверьте, что произойдет. Как думаете почему так?


### Не перегружайте код (Sparse is better than dense.)

Хотя мы должны умещать код в 8 строк. Мы можем написать очень насыщенный код. Код ниже заставить разработчика остановиться и потратить какое-то время, чтобы разобраться в нем, если ему нужно что-то поправить или реализовать подобный функционал у себя.

```python 
capacity = [(j * 8, 256**j-1) for j in (1 << i for i in range(4))]
print("\n".join("%i bits can store number up to %i" % bc for bc in capacity))
```

```
8 bits can store number up to 255
16 bits can store number up to 65535
32 bits can store number up to 4294967295
64 bits can store number up to 18446744073709551615
```

Написав больше кода мы можем уменьшить время, которое разработчик тратит на изучение этого участка.

```python
capacity = list()
for i in range(4):
    j = 1 << i
    bits = j * 8
    max_val = 256**j - 1
    capacity.append((bits , max_val))

for bits, max_val in capacity:
    print("%i bits can store number up to %i" % (bits, max_val))
```

## Выводы

Придерживаться стиля нужно для того, чтобы быть понятным. Хороший стиль помогает быстро сориентироваться в коде и найти, то место за которым вы пришли в этот модуль. Часть работы по оформлению кода, можно делегировать автоматическим средствам, таким как `autopep8`. Про другую часть придется помнить и писать код с учетом этих знаний. Стиль это не про то, чтобы писать меньше кода. Иногда (редко) Вам будет казаться, что придерживаться стиля контр интуитивно, а получивший код может казаться вам не красивым, но если так пишут большинство разработчиков, все равно придерживайтесь рекомендаций, со временем вы привыкните. Вы не сможете начать писать хорошо оформляя код без практики, пишите, а самое главное читайте чужой код, чтобы понять, как пишут ваши коллеги. 

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

Улучшите читаемость кода ниже. Для решения примите, что нам нужно импортировать функции `one_function`, `another_function` из `my_module`. Обратитесь к [этой](https://note.nkmk.me/en/python-import-usage/) статье если, вам нужна помощь в оформлении.

```python
import math, pandas as pd, numpy
from my_module import *
```

**Ответ**

Хорошим стилем считается использование импортов каждого п

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
    * Вокруг арифметических, логических операторов есть пробелы, например (`a * b`, `x = 10` и `y = 5`), что упрощает идентификацию выполняемой операции. Вокруг оператора присваивания пробелы, так же ставятся, кроме случаев использования при объявлении функции.
    * Перед двоеточием в условном операторе пробела нет, что улучшает связность кода.
    * После запятой, которая разделяет аргументы функции мы ставим пробел.
    
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

Улучшите именование переменных, функций и классов. Используйте CamelCase для классов, и разделение подчеркиванием для функций.

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

Мы должны поправить имена переменных, чтобы они не состояли из одной буквы. Имя функции сокращено и не дает понимание того что функция делает, так как `calcrect1` не дает понимание о том, что именно будет рассчитано.

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

Для примера ниже предполагается что база данных хранит данные о покупателе и его карточку.

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

Часто бывает что сокращение приводит к тому, что это становиться другим словом. Так в примере карточка (card) стала машиной (car).

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

Бывает что мы хотим называем объект используя какие-то свои ассоциации или что-то еще, что делает название понятным для нас, но будет сбивать с толку других разработчиков. Поправьте код ниже чтобы, каждый мог понять что мы создали класс Кольцо. Поправьте название методов.

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

Напишите комментарии к функции, чтобы дать понимание о ее работе. Попробуйте описать функцию которая рассчитывает прибыль по инвестициям.

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

Часто бывает, что мы реализуем логику, которая специфична для конкретной ситуации, и может не встречаться за ее пределами. Например поведение функции `sum` для чисел очевидно, она вернет суммы переданных в нее аргументов-чисел. Но давайте представим подсчет очков в настольной игре-ходилке, где количество очко зависит от тех клеток, которые прошла фишка игрока. Давайте представим что клетки и числом кратным трем содержат сундуки, которые увеличивают вклад этой клетки в два раза, а клетки кратные двум содержат разбойников, которые уменьшаю вклад этой клетки в два раза.

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