from pymodbus.client.sync import ModbusSerialClient as ModbusClient
 
client = ModbusClient(method = 'rtu', port = '/dev/ttyAMA0', stopbits = 1, bytesize = 8, parity = 'E', baudrate = 19200)
client.connect()
 
result = client.read_input_registers(0x3100,6,unit=1)
solarVoltage = float(result.registers[0] / 100.0)
solarCurrent = float(result.registers[1] / 100.0)
batteryVoltage = float(result.registers[4] / 100.0)
chargeCurrent = float(result.registers[5] / 100.0)
 
# Do something with the data
 
client.close()
