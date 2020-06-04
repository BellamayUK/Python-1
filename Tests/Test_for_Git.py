<<<<<<< Updated upstream
import pytest

def temperature_oven():
    return 220

def cake_temperature():
    return 200

def test_temperature_oven():
    assert temperature_oven() == 220

def test_cake_temperature():
    assert cake_temperature() == 200
=======
import pytest

def temperature_oven(num):
    return num + 5


def test_temperature_oven():
    assert temperature_oven(7) == 12
    assert temperature_oven(0) == 5
>>>>>>> Stashed changes
