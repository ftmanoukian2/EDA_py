from machine import Pin, PWM, ADC

idx = [27,14,12,13]
d_outs = []
for pin in idx:
    d_outs.append(Pin(pin, Pin.OUT))

def Fijar_salida_digital(salida : int, estado : bool) -> None :
    if salida >= 1 and salida <= 4:
        d_outs[salida - 1].value(estado)
    else:
        print("Número de salida inválido (1-4)")
       
idx = [32,33,25,26]
pwm_outs = []
for pin in idx:
    pwm_outs.append(PWM(Pin(pin), freq = 50))
    
def Fijar_salida_analogica(salida : int, valor : int) -> None:
    if (salida >= 1 and salida <= 4):
        if(valor >= 0 and valor <= 100):
            pwm_outs[salida - 1].duty(int(valor) * 10.23)
        else:
            print("Valor de salida inválido (0-100)")
    else:
        print("Número de salida inválido (1-4)")
         
idx = [35,34,39,36]        
adc_ins = []
for pin in idx:
    adc_ins.append(ADC(Pin(pin), atten = ADC.ATTN_11DB))
    
def Leer_entrada_analogica(entrada : int) -> int:
    if(entrada >= 1 and entrada <= 4):
        return adc_ins[entrada - 1].read_u16() / 65535
    else:
        print("Número de entrada inválido (1-4)")
        return -1
        
idx = [0,15,2,4]
d_ins = []
for pin in idx:
    d_ins.append(Pin(pin,Pin.IN))
    
def Leer_entrada_digital(entrada : int) -> int:
    if(entrada >= 1 and salida <= 4):
        return d_ins[entrada - 1].value()
    else:
        print("Número de entrada inválido (1-4)")
        return -1
    
del idx