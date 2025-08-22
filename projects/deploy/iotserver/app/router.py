from fastapi import APIRouter, BackgroundTasks, HTTPException, Depends
from app.schemas import (
    DeviceRegistration, 
    UserRegistration
)
from app.utils import make_id
from app.storage import (
    save_data, 
    storages, 
    devices,
    user_device_links
)

router = APIRouter()

@router.post("/register/", response_model=dict)
def register_device(
    device: DeviceRegistration, 
    tasks: BackgroundTasks, 
    storage = Depends(storages)
):
    device_id = make_id(device.mac_address)
    topic = f"{device.owner}/{device.city}/{device.measurement_type}/{device_id}"
    
    if device_id in devices:
        raise HTTPException(status_code=400, detail="Device already registered")
    
    devices[device_id] = {"device_id": device_id, "topic": topic, **device.model_dump()}
    save_data(storage["devices"], devices)
    user_device_links["devices"][device_id] = []
    save_data(storage["user_device_links"], user_device_links)

    message = (
        f"New device registered!\n"
        f"ID: {device_id}\n"
        f"Location: ({device.longitude}, {device.latitude})\n"
        f"Owner: {device.owner}\n"
        f"Measurement Type: {device.measurement_type}\n"
        f"Sensor Model: {device.sensor_model}"
    )

    #send_telegram_notification(message)
    #tasks.add_task(send_telegram_notification, message)
    return {"device_id": device_id, "topic": topic}

@router.get("/devices", response_model=dict)
def get_all_devices(owner: str):
    result = {}
    for device in devices.values():
        if device["owner"] == owner:
            result[device["device_id"]] = device                

    if not result:
        raise HTTPException(status_code=404, detail="No devices found for owner")
    return result

@router.get("/device/{device_id}", response_model=dict)
def get_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return devices[device_id]

@router.post("/device_by_mac/", response_model=dict)
def get_device_by_mac(device: DeviceRegistration):
    device_id = make_id(device.mac_address)
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return devices[device_id]

@router.delete("/device/{device_id}")
def delete_device(device_id: str, storage = Depends(storages)):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    del devices[device_id]
    save_data(DATA_FILE, devices)
    return {"message": "Device deleted"}

@router.put("/device/{device_id}", response_model=dict)
def update_device(device_id: str, updated_data: DeviceRegistration):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    
    topic = f"{updated_data.owner}/{updated_data.city}/{updated_data.measurement_type}/{device_id}"
    devices[device_id] = {"device_id": device_id, "topic": topic, **updated_data.model_dump()}
    save_data(DATA_FILE, devices)
    return devices[device_id]

@router.get("/topics/{device_id}", response_model=dict)
def get_mqtt_topic(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"topic": devices[device_id]["topic"]}

@router.get("/configs/{device_id}", response_model=ConfigSettings)
def get_device_config(device_id: str):
    if device_id not in configs:
        raise HTTPException(status_code=404, detail="Config not found for device")
    return configs[device_id]

@router.post("/configs/{device_id}", response_model=ConfigSettings)
def set_device_config(device_id: str, config: ConfigSettings):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    configs[device_id] = {"device_id": device_id, **config.model_dump()}
    save_data(CONFIG_FILE, configs)
    return config


@router.post("/configs/{device_id}", response_model=ConfigSettings)
def set_device_config(device_id: str, config: ConfigSettings):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    configs[device_id] = {"device_id": device_id, **config.model_dump()}
    save_data(CONFIG_FILE, configs)
    return config

@router.post("/register_user", response_model=UserResponse)
def register_user(user: UserRegistration):
    """Performes user registration based on Telegram chat ID

    Default role assigned to a User is manager. It could be letter changed via separate 
    endpoint. An empty device list created for a user. That should be filled via
    'link_device' endpoint.

    Returns 400 HTTP code if user already regestered.
    """
    user_id = make_id(str(user.chat_id))
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already registered")
    users[user_id] = {"user_id": user_id, "role": UserRole.MANAGER, **user.model_dump()}
    save_data(USERS_FILE, users)
    user_device_links["users"][user_id] = []
    save_data(USER_DEVICE_LINK_FILE, user_device_links)
    return users[user_id]


@router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@router.post("/identify_user/", response_model=UserResponse)
def identify_user(user: UserRegistration):
    user_id = make_id(str(user.chat_id))
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@router.delete("/remove_user/{user_id}")
def remove_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    save_data(USERS_FILE, users)
    return {"message": "User {user_id} deleted"}

@router.post("/link_device")
def link_device_to_user(
    user_id: str = Query(description="The ID of user as it appears in service"),
    device_id: str = Query(description="The ID of device as it appears in service"),
) -> dict:
    if not user_id in users:
        raise HTTPException(status_code=404, detail="User not found")
    if not device_id in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    
    device_users = user_device_links["devices"][device_id]
    user_devices = user_device_links["users"][user_id]
    if not user_id in device_users:
        device_users.append(user_id)
    if not device_id in user_devices:
        user_devices.append(device_id)

    return {"devices": user_devices}