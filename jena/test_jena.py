"""pytest file for jena

Run ``pytest`` to execute tests.

Attributes:
    port (str): serial port
"""
import jena
import pytest
import numpy as np

port = 'COM3'
def test_overload():
    """Check if the device throws an error when an out of bounds value is given 
    """
    with pytest.raises(ValueError):
        piezo = jena.NV40(port)
        piezo.set_position(1000)

def test_value():
     """Check if values are set okay
     """
     piezo = jena.NV40(port)
     for setpoint in [0,100,200,300]
         piezo.set_position(setpoint)
         achieved = piezo.get_position()
         assert(np.isclose(achieved, setpoint,rtol=0,atol=1))