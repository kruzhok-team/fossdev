from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
from tempfile import gettempdir
import json

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
        except (json.JSONDecodeError, IOError) as e:
            devices = {}  # Reset to avoid corrupted data
    else:
        raise RuntimeError("Device 'DB' is not found")

def save_devices():
    """Saves registered devices to a file."""
    with open(DATA_FILE, "w") as f:
        json.dump(devices, f, indent=4)

load_devices() 

class Device(BaseModel):
    device_id: str = Field("00:00:00:00:00:00")
    location: str = Field("Bratsk")
    owner: str = Field("Lyceum")
    measurement_type: str = Field("temperature")
    sensor_model: str = Field(..., description="Put particular sensor model name here")

@app.post("/register")
async def register_device(device: Device):
    if device.device_id in devices:
        raise HTTPException(status_code=400, detail="Device already registered")
    
    devices[device.device_id] = device.model_dump()
    save_devices()
    return {"message": "Device registered successfully"}

@app.get("/devices")
async def list_devices():
    return devices

@app.get("/device/{device_id}")
async def get_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return devices[device_id]
