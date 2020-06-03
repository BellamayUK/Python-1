import pytest

def temperature_oven(num):
    return num + 5


def test_temperature_oven_smallnumbers():
    assert temperature_oven(7) == 12
    assert temperature_oven(0) == 5

