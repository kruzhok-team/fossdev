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
