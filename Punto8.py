# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
import time


# Configura los pines
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

# Configuración del correo
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'sergioarias1001@gmail.com'
password = 'qvfe cnit mrme xpet'
receiver_email = 'juliana.zapata9217@uco.net.co'

def enviar_correo(pulsador):
    msg = MIMEText("El pulsador "+pulsador+" ha sido presionado.")
    msg['Subject'] = 'Notificacion de Pulsador'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Inicia la encriptación
            server.login(sender_email, password)  # Inicia sesión
            server.send_message(msg)  # Envía el mensaje
        print("Correo enviado con exito!")
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

try:
    print("Presione el pulsador para enviar un correo...")
    while True:
        if GPIO.input(5) == False:  # Si el pulsador está presionado
            enviar_correo("1")
            time.sleep(1)  # Espera un segundo para evitar múltiples envíos
        elif GPIO.input(7) == False:  # Si el pulsador está presionado
            enviar_correo("2")
            time.sleep(1)  # Espera un segundo para evitar múltiples envíos
        elif GPIO.input(11) == False:  # Si el pulsador está presionado
            enviar_correo("3")
            time.sleep(1)  # Espera un segundo para evitar múltiples envíos




except KeyboardInterrupt:
    print("Programa detenido.")

finally:
    GPIO.cleanup()  # Limpia la configuración de GPIO
