import os
import tempfile
from pydantic import ConfigDict

DATA_FILE = os.path.join(tempfile.gettempdir(), "devices.json")
CONFIG_FILE = os.path.join(tempfile.gettempdir(), "configs.json")
USERS_FILE = os.path.join(tempfile.gettempdir(), "users.json")
USER_DEVICE_LINK_FILE = os.path.join(tempfile.gettempdir(), "user_device_links.json")