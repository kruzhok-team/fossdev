import logging
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from tempfile import gettempdir

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

DATA_FILE = Path(gettempdir()) / "devices.json"

app = FastAPI()

# In-memory storage for demonstration purposes

devices = {}

def load_devices():
    """Loads registered devices from a file."""
    global devices
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                devices = json.load(f)
            logging.info(f"Loaded {len(devices)} devices from disk.")
        except (json.JSONDecodeError, IOError) as e:
            logging.critical(f"Failed to load devices from disk: {e}")
            devices = {}  # Reset to avoid corrupted data
    else:
        logging.warning("No existing device data found, starting fresh.")

def save_devices():
    """Saves registered devices to a file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(devices, f, indent=4)
        logging.debug("Devices successfully saved to disk.")
    except IOError as e:
        logging.critical(f"Failed to save devices to disk: {e}")

load_devices() 

class Device(BaseModel):
    device_id: str = Field("00:00:00:00:00:00")
    location: str = Field("Bratsk")
    owner: str = Field("Lyceum")
    measurement_type: str = Field("temperature")
    sensor_model: str = Field(..., description="Put particular sensor model name here")


@app.post("/register")
async def register_device(device: Device):
    logging.debug(f"Received registration request for device_id: {device.device_id}")

    if device.device_id in devices:
        logging.warning(f"Device {device.device_id} is already registered.")
        raise HTTPException(status_code=400, detail="Device already registered")

    devices[device.device_id] = device.model_dump()
    save_devices()  # Persist changes
    logging.info(f"Device {device.device_id} registered successfully.")

    return {"message": "Device registered successfully"}

@app.get("/devices")
async def list_devices():
    logging.debug("Fetching list of all registered devices.")
    
    if not devices:
        logging.warning("Device list requested but no devices are registered.")
    
    return devices

@app.get("/device/{device_id}")
async def get_device(device_id: str):
    logging.debug(f"Fetching details for device_id: {device_id}")

    if device_id not in devices:
        logging.error(f"Device {device_id} not found.")
        raise HTTPException(status_code=404, detail="Device not found")

    logging.info(f"Device {device_id} details retrieved.")
    return devices[device_id]
