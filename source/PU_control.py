from source.PhoneControl import *

leidian = PhoneControl('127.0.0.1')

print(leidian.get_phone())
leidian.input_tap([100,100])
