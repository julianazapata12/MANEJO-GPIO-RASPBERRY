import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led_pins = [7, 11, 13, 15, 31, 33, 35, 37]  
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

def mostrar_binario(num):
      
      if 0 <= num <= 255:
          binario = format(num, '08b')
          for i in range(8):
              GPIO.output(led_pins[i], int(binario[i]))
      else:
          print("El numero debe estar entre 0 y 255.")

try:
    while True:
          print("Seleccione una operacion:")
          print("1. Sumar (+)")
          print("2. Restar (-)")
          print("3. Multiplicar (*)")
          print("4. Dividir (/)")

        opcion = input("Ingrese la opcion (1-4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = int(input("Ingrese el primer numero (0-255): "))
            num2 = int(input("Ingrese el segundo numero (0-255): "))

              if opcion == '1':
                  resultado = num1 + num2
              elif opcion == '2':
                  resultado = num1 - num2
              elif opcion == '3':
                  resultado = num1 * num2
              elif opcion == '4':
                  if num2 != 0:
                      resultado = num1 // num2 
                  else:
                      print("Error: Division por cero.")
                      continue
            
            print(f"Resultado: {resultado}")
            mostrar_binario(resultado)
        else:
            print("Opcion invalida.")

except KeyboardInterrupt:
    print("Programa detenido.")

finally:
    GPIO.cleanup() 
