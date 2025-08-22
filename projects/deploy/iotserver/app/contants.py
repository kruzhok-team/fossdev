from enum import Enum

class MeasurementType(str, Enum):
    TEMPERATURE = "temperature"
    LUMINOCITY = "luminocity"

class UserRole(str, Enum):
    MANAGER = "manager"
    ADMINISTRATOR = "administrator"