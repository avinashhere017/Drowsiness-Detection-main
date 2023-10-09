import pyfirmata
comport='COM9'
board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
buzzer=board.get_pin('d:10:o')

def run(flag):
    if(flag==1):
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        buzzer.write(0)
    if(flag==2):
        led_1.write(0)
        led_2.write(2)
        led_3.write(0)
        buzzer.write(0)
    if(flag==3):
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        buzzer.write(1)
    
