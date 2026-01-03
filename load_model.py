import numpy as np
from config import *

def generate_base_load():
    hours = np.arange(HOURS_PER_DAY)

    lighting = np.array([
        LIGHTING_NIGHT if LIGHTING_START <= h <= LIGHTING_END else LIGHTING_DAY
        for h in hours
    ])

    fridge = np.full(HOURS_PER_DAY, FRIDGE_POWER)

    washing_machine = np.array([
        WASHING_MACHINE_POWER if h == WASHING_MACHINE_HOUR else 0
        for h in hours
    ])

    computer = np.array([
        COMPUTER_POWER if COMPUTER_START <= h <= COMPUTER_END else 0
        for h in hours
    ])

    return lighting + fridge + washing_machine + computer
