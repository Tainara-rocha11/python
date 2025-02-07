import pywhatkit as kit
import time 
phone_number = '+5571991223730'


message = 'Hello! This message is from Tainara Rocha. How are you?'

kit.sendwhatmsg_instantly(phone_number, message, 16,24)
time.sleep(5)
print ('Mensagem enviada com Sucesso!')