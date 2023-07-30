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
