# EDA_py

## Importante!

Esta extensión está en desarrollo (última actualización: 28/2/2024). La sintaxis de las funciones y/o los parámetros y valores de retorno pueden cambiar en próximas versiones.

## Instrucciones

1. Descargar el archivo "EDA.py" (descargando manualmente o clonando y actualizando el repo)
2. Abrir el archivo localmente desde Thonny
3. Guardar el archivo en el dispositivo micropython (si ya está, sobreescribirlo)
4. Incorporar al proyecto:
    * (Opción 1: "Transparente"): En el archivo "boot.py" * ya existente * en el dispositivo, añadir la línea `from EDA import *`.
    * (Opción 2: "Explícita"): En el archivo main.py (ya existente o a crear), añadir la línea `from EDA import *` al inicio.

## Funciones

* Fijar_salida_digital(salida, valor)
    * salida: 1-4
    * valor: 0-1 / True-False

* Fijar_salida_analogica(salida, valor)
    * salida: 1-4
    * valor: 0-1023

* Leer_entrada_digital(entrada)
    * entrada: 1-4
    * retorno: 0-1

* Leer_entrada_digital(entrada)
    * entrada: 1-4
    * retorno: 0-65535
