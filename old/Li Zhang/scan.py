from bluepy.btle import Peripheral

p = Peripheral()
p.start_advertising(data = "Hello Arduino!")