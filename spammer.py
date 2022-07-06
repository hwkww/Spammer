import pyautogui as spam
import time

limite_msg = input("Número de msgs que serão enviadas: ")
msg = input("Mensagem que será enviada: ")

i = 0

time.sleep(2)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

    i+=1
