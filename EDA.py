from machine import Pin, PWM, ADC

idx = [27,14,12,13]
d_outs = []
for pin in idx:
    d_outs.append(Pin(pin, Pin.OUT))

def Fijar_salida_digital(salida : int, estado : bool) -> None :
    if salida >= 1 and salida <= 4:
        d_outs[salida - 1].value(estado)
       
idx = [32,33,25,26]
pwm_outs = []
for pin in idx:
    pwm_outs.append(PWM(Pin(pin), freq = 50))
    
def Fijar_salida_analogica(salida : int, valor : int) -> None:
    if (salida >= 1 and salida <= 4) and (valor >= 0 and valor <= 1023):
        pwm_outs[salida - 1].duty(int(valor))
         
idx = [36,39,34,35]        
adc_ins = []
for pin in idx:
    adc_ins.append(ADC(Pin(pin), atten = ADC.ATTN_11DB))
    
def Leer_entrada_analogica(entrada : int) -> int:
    if(entrada >= 1 and entrada <= 4):
        return adc_ins[entrada - 1].read_u16()
    else:
        return -1
        
idx = [0,15,2,4]
d_ins = []
for pin in idx:
    d_ins.append(Pin(pin,Pin.IN))
    
def Leer_entrada_digital(entrada : int) -> int:
    if(entrada >= 1 and salida <= 4):
        return d_ins[entrada - 1].value()
    else:
        return -1
    
del idx