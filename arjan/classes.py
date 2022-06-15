import random
import string
from datetime import datetime
from enum import Enum, auto


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""
    digit_part = ""
