from app.contants import MeasurementType, UserRole
from typing import BaseModel, Field


class Device(BaseModel):
    measurement_type: str = Field(
        MeasurementType.TEMPERATURE, 
        description=f"Measurements types: {[e.value for e in MeasurementType]}"
    )
    sensor_model: str = Field(..., description="Put particular sensor model name here")
    
class DeviceRegistration(Device):
    mac_address: str = Field("00:00:00:00:00:00")

class ConfigSettings(BaseModel):
    longitude: float = Field(101.7121)
    latitude: float = Field(56.2928)
    height: float = Field(428)
    city: str = Field("Bratsk")
    owner: str = Field("Lyceum")
    data_cadence: int = Field(60, description="Data transmission interval in seconds")
    qos: int = Field(0, description="MQTT Quality of Service level")
    last_updated: str = Field(..., description="Timestamp of last update")

class User(BaseModel):
    username: str = Field(description="User nickname")

class UserRegistration(User):
    chat_id: int = Field(description="User chat id in telegram")

class UserResponse(User):
    user_id: str = Field(description="User ID in service")
    role: str = Field(
        UserRole.MANAGER, 
        description=f"Available roles: {[item.value for item in UserRole]}"
    )