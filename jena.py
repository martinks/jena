"""Provides a wrapper for serial commands to control Jena piezo stages
"""

import serial

class DeviceError(Exception):
    """Error to throw when the device returns an error
    """
    pass

class jena:
    """Provides control of Jena piezo stages

    Args:
        port (str): serial port
        timeout (float, optional): serial timeout in seconds
        closed_loop (bool, optional): Operation mode. True for closed loop, False for open loop.

    Example use::

        device = jena.jena('COM3', closed_loop = True)
        device.set_position(10)
        print(device.get_position())


    Notes:
        ``python -m serial.tools.list_ports`` will print a list of available ports. It is also possible to add a regexp as first argument and the list will only include entries that matched. See https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports for more details.
    """
    def __init__(self, port, timeout=0.5, closed_loop=True):
        self.__port = port
        self.__timeout = timeout
        self.__baudrate = 9600
        self.__bytesize = serial.EIGHTBITS
        self.__stopbits = serial.STOPBITS_ONE
        self.__parity = serial.PARITY_NONE
        self.__errors = {'err,1':'Unknown command',
                      'err,2':'Too many characters in the command',
                      'err,3':'Too many characters in the parameter',
                      'err,4':'Too many parameters',
                      'err,5':'Wrong character in parameter',
                      'err,6':'Wrong separator',
                      'err,7':'Overload'}
        self.set_closed_loop(closed_loop)
        
    def __execute(self, command):
        """Execute a device command and check if the device returned an error
        
        Args:
            command (str): Device command
        
        Returns:
            str: Response from the device
        
        Raises:
            DeviceError
        """
        with serial.Serial(port=self.__port, baudrate=self.__baudrate, bytesize=self.__bytesize, 
            parity=self.__parity, timeout=self.__timeout) as ser:
            command += '\r'
            ser.write(command.encode())
            answer = ser.read(100).decode("utf-8").rstrip()
            if answer in self.__errors:
                raise DeviceError(self.__errors[answer])
            return answer
        
    def set_position(self, value):
        """Set position 

        Setting the position will enable remote control, which disables manual control
        You can return to manual control using the set_remote_control(False) method.
        
        Args:
            value (float): Position in urad/um (closed loop) or volts (open loop)
        """
        self.set_remote_control(True)
        self.__execute('wr, %.2f' % value)
        
    def get_position(self):
        """Get current position
        
        Returns:
            float: Current position in urad or um (closed loop) or in volts (open loop)
        """
        return float(self.__execute('rd').split(',')[1])
        
    def set_closed_loop(self,is_enabled):
        """Switch between open and closed loop mode
        
        Args:
            is_enabled (bool): closed loop (True) or open loop (False) 
        """
        if is_enabled:
            self.__execute('cl')  
        else:
            self.__execute('ol')
        
    def set_remote_control(self,is_enabled):
        """Switch between remote and manual control
        
        Args:
            is_enabled (bool): remote control (True) or manual control (False)
        """
        if is_enabled:
            self.__execute('i1')  
        else:
            self.__execute('i0')