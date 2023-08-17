## Задача

### Задача 1

Используйте код ниже и снабдите его логами уровней SUCCES, DEBUG, INFO. Используйте `loguru`. Сделайте так, чтобы для вызова функций с разными аргументами сообщения отличались, т.е. были информативными с точки зрения того, что по ним можно восстановить детали работы приложения. Сообщения вида `Sum calculated` не являются информативными, так как каждый вызов функции приведет к одному и тому же сообщению, по которым можно восстановить только время вызова, другая информация не сохраняется, что будет неудобно при анализе логов.


```python
def calculate_sum(a, b):
    return a + b

def main():
    num1 = 10
    num2 = 20
    result = calculate_sum(num1, num2)

if __name__ == "__main__":
    main()
```

**Ответ**

([код](/projects/logging/summator_logging.py)):

```python
import loguru

# Configure loguru to write logs to a file named 'app.log' with a maximum size of 1 MB per file
loguru.logger.add("app.log", rotation="1 MB")

def calculate_sum(a, b):
    result = a + b
    loguru.logger.debug(f"Sum calculated: {a} + {b} = {result}")
    return result

def main():
    num1 = 10
    num2 = 20

    # Log the beginning of the calculation
    loguru.logger.info(f"Starting the calculation of {num1} + {num2}")

    result = calculate_sum(num1, num2)

    # Log the result
    loguru.logger.success(f"Calculation successful! The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
```

### Задача 2

Используйте код ниже и снабдите его логами уровней DEBUG, INFO, WARNING и ERROR. Не всегда появление `exception` в программе должно приводить к легированию уровня ERROR. Мы можем использовать другие уровни в зависимости от того, как обрабатываются исключения. Подумайте, какие еще проверки можно внести, например, мы не проверяем, что `data` в `process_data` является строкой, хотя тело функции это подразумевает.

```python

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def process_data(data):
    if not data:
        return

    # Perform some data processing here
    processed_data = data.upper()
    return processed_data

def save_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:

def main():

    file_path = "data.txt"
    data = load_data(file_path)
    if data:
        processed_data = process_data(data)
        if processed_data:
            save_data("processed_data.txt", processed_data)

if __name__ == "__main__":
    main()
```

**Ответ**

([код](/projects/logging/data_processing_logging.py)):

```python
import loguru

loguru.logger.add("app.log", rotation="1 MB")

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            loguru.logger.debug(f"Data loaded from {file_path}")
            return data
    except FileNotFoundError:
        loguru.logger.warning(f"File not found: {file_path}")
        return None
    except Exception as e:
        loguru.logger.error(f"Error loading data from {file_path}: {e}")
        return None

def process_data(data):
    if not data:
        loguru.logger.error("No data to process!")
        return
    processed_data = data.upper()
    data_len = len(data)
    log_size = min(data_len / 2, 20)
    loguru.logger.debug("Data {data[:log_size]} ... {data[log_size:]} processed successfully")
    return processed_data

def save_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            loguru.logger.info(f"Data saved to {file_path}")
    except Exception as e:
        loguru.logger.error(f"Error saving data to {file_path}: {e}")

def main():
    loguru.logger.info("Starting the program")

    file_path = "data.txt"
    data = load_data(file_path)
    if data:
        processed_data = process_data(data)
        if processed_data:
            save_data("processed_data.txt", processed_data)

    loguru.logger.info("Program execution completed")

if __name__ == "__main__":
    main()
```


### Задача 3

Модифицируйте код ниже так, чтобы была информация о пользователе, который сделал запрос, а также `hash` переданных данных. Напишите логирование для полученного кода.


```python
from flask import Flask, request, jsonify

app = Flask(__name__)

def process_request(request_data):
    try:
        # Simulate some request processing
        result = request_data.get('data', 0) * 2
        return result
    except Exception as e:
        return None

@app.route('/api/data', methods=['POST'])
def handle_request():
    try:
        request_data = request.get_json()

        if not request_data or 'data' not in request_data:
            return jsonify({'error': 'Invalid request data'}), 400

        result = process_request(request_data)
        if result is not None:
            return jsonify({'result': result}), 200
        else:
            return jsonify({'error': 'Error processing request'}), 500

    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

**Ответ**

([код](/projects/logging/user_request_logging.py)):

```python
import loguru
import hashlib
from flask import Flask, request, jsonify

# Configure loguru to write logs to a file named 'web_app.log' with a maximum size of 1 MB per file
loguru.logger.add("web_app.log", rotation="1 MB")

app = Flask(__name__)

def compute_data_hash(data):
    data_str = str(data).encode('utf-8')
    return hashlib.sha256(data_str).hexdigest()

def process_request(request_data, user_id, data_hash):
    try:
        # Simulate some request processing
        result = request_data.get('data', 0) * 2
        loguru.logger.debug(f"User ID: {user_id} | Data Hash: {data_hash} | Request processed successfully. Result: {result}")
        return result
    except Exception as e:
        loguru.logger.error(f"User ID: {user_id} | Data Hash: {data_hash} | Error processing request: {e}")
        return None

@app.route('/api/data', methods=['POST'])
def handle_request():
    try:
        request_data = request.get_json()
        user_id = request_data.get('user_id', None)
        loguru.logger.info(f"User ID: {user_id} | Received a request")
        loguru.logger.debug(f"User ID: {user_id} | Request data: {request_data}")

        if not request_data or 'data' not in request_data or not user_id:
            loguru.logger.warning(f"User ID: {user_id} | Data Hash: N/A | Invalid request data received")
            return jsonify({'error': 'Invalid request data'}), 400

        data_hash = compute_data_hash(request_data)
        result = process_request(request_data, user_id, data_hash)

        if result is not None:
            loguru.logger.success(f"User ID: {user_id} | Data Hash: {data_hash} | Request processed successfully")
            return jsonify({'result': result}), 200
        else:
            loguru.logger.error(f"User ID: {user_id} | Data Hash: {data_hash} | Error occurred while processing the request")
            return jsonify({'error': 'Error processing request'}), 500

    except Exception as e:
        loguru.logger.critical(f"User ID: N/A | Data Hash: N/A | Unhandled exception: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    loguru.logger.info("Starting the web application")
    app.run(debug=True)
```