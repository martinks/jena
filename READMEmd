# Jena

This package provides a wrapper for serial communication with Jena piezoelectric controllers. 

Currently, only support for the NV40/1CL(E) controller is implemented.

## Installing

The package can be easily installed with pip:
```
pip install https://github.com/martinks/jena/archive/master.zip
```


## Usage

Set position in microns using the closed loop mode::

    device = jena.NV40('COM3')
    device.set_position(10)
    print(device.get_position())

Recommended use is with a context manager, which restores manual control after executing the statements in the with block. Note that the position will be reset to the position it had before the remote control was switched on::

	setpoint = 100
	print('Setpoint',setpoint)
	with jena.NV40('COM3') as device:
	    print('Initial position',device.get_position())
	    device.set_position(setpoint)
	    position = device.get_position()
	    print('New position',device.get_position())
	print('Final position',device.get_position())

## Finding the right port 

``python -m serial.tools.list_ports`` will print a list of available ports. It is also possible to add a regexp as first argument and the list will only include entries that matched. See https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports for more details.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details