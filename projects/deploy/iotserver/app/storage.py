import os
import tempfile
import json

DEVICE_FILE = os.path.join(tempfile.gettempdir(), "devices.json")
CONFIG_FILE = os.path.join(tempfile.gettempdir(), "configs.json")
USER_FILE = os.path.join(tempfile.gettempdir(), "users.json")
USER_DEVICE_LINK_FILE = os.path.join(tempfile.gettempdir(), "user_device_links.json")

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

def load_user_device_links(file_path):
    data = load_data(file_path)
    if not data:
        data = {"devices": {}, "users": {}}
    return data

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def device_file():
    return DEVICE_FILE

def config_file():
    return CONFIG_FILE

def user_file():
    return USER_FILE

def user_device_file():
    return USER_DEVICE_LINK_FILE

def storages():
    return {
        "users": USER_FILE,
        "devices": DEVICE_FILE,
        "configs": CONFIG_FILE,
        "user_device_links": USER_DEVICE_LINK_FILE
    }

devices = load_data(DEVICE_FILE)
configs = load_data(CONFIG_FILE)
users = load_data(USER_FILE)
user_device_links = load_user_device_links(USER_DEVICE_LINK_FILE)