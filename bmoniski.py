import config
import amino
import random
import time
import os
import requests
import subprocess
from io import BytesIO
from getpass import getpass


client = amino.Client()

print("""
     ("`-/")_.-'"``-._
      . . `; -._    )-;-,_`)
     (v_,)'  _  )`-.\  ``-'
    _.- _..-_/ / ((.'
  ((,.-'   ((,/   By- Serval.
""")

client.login(
  input('email: '),
  getpass('password: ')
)

#Puedes cambiar el getpass por input, pero getpass es mas seguro! 

acced = amino.SubClient(
    comId = 67,
    profile=client.profile
)



os.system ("clear")


print("""
      ,/|         _.--''^``-...___.._.,;
     /, \'.     _-'          ,--,,,--'''
    { \    `_-''       '    /}
     `;;'            ;   ; ;
 ._.--''     ._,,, _..'  .;.'
  (,_....----'''     (,..--''
       ¡Bienvenido mortal, puedes probar de este maravilloso bot! Pero recuerda, es una prueba, ¿Te gusto? ¡Compralo y estara 24/7!
""")


HELP = """
[C] )\_/(
[C] 'o.o'
[C]=(_ _)=
[C]⠀

[CB]¡Bienvenido usuario! Me llamo JapariBot, ¿Mi creador? Serval >w<

[C] Comandos de GUION (-):

[B][kiss] [kill] [id] [help] [hug] [comment] [audio] [img]

[C] Comandos de VIRGULILLA (~):

[B][kiss] [ban] [meter] [invite]

Para tener informacion de un comando use [-help comando] donde dice [comando] cambiarlo por los comandos que se dijeron, por ejemplo, -help -kiss o -help ~kiss. :)

"""
join = """ [BC]BIENVENID@༊

[C]Esperamos que tu estadía
[C]sea b u e n a, al igual que tu
[C]actitud o actividad en el chat,
[C]puedes socializar, participar en
[C]actividades, ganar premios y
[C]divertirte con 𝐧 𝐨 𝐬 𝐨 𝐭 𝐫 𝐨 𝐬

[C]Cualquier duda o reporte,
[C]puedes consultar c o n
[C]algún coan o la anfitrióna

"""

leave = """[BC]Adios@༊ :(

[C]¡Te deseamos suerte en tu viaje!
[C]Pero recuerda siempre eres muy...
[C]Bienvenido al chat >w<
"""

name_pr = lambda l: ' '.join(l)

def socketDelay():
    j = 0
    while True:
        if j >= 300: # = 5 min
            print("Actualizándose...")
            client.socket.close()
            client.socket.start()
            print("Actualización completa")
            j = 0
        j += 1
        time.sleep(1)




@client.callbacks.event('on_group_member_join')
def on_group_member_join(data):
    if data.comId == acced.comId:
        acced.send_message(
            chatId=data.message.chatId,
            message=f"{join} <$@{data.message.author.nickname}$> todos los del chat te decimos ¡Welcome user!", mentionUserIds=[str(data.message.author.userId)], replyTo=data.message.messageId)

@client.callbacks.event('on_group_member_leave')
def on_group_member_join(data):
    if data.comId == acced.comId:
        acced.send_message(
            chatId=data.message.chatId,
            message=f"{leave} <$@{data.message.author.nickname}$> ", mentionUserIds=[str(data.message.author.userId)], replyTo=data.message.messageId)


@client.callbacks.event("on_text_message")
def on_text_message(data):

    #parametros
    command = data.message.content.split(' ')
    print(command)
    pr_t = command[1:]
    command = command[0] 

    #help:
    if command == "-help":
       acced.send_message(chatId=data.message.chatId, message = HELP)       
       if name_pr(pr_t) == "-id":
          acced.send_message(chatId=data.message.chatId, message = """[CB]id:
          
          Esto es para tener el ID de dicho chat.""") 
       if name_pr(pr_t) == "-kiss":
          acced.send_message(chatId=data.message.chatId, message = """[CB]kiss:
          
          Es un comando para besar apasionadamente aun usuario. :3 """)
       if name_pr(pr_t) == "-kill":
          acced.send_message(chatId=data.message.chatId, message = """[CB]kill:
          
          ¡Este comando le da O'K a su oponente enseguida! D': """)
       if name_pr(pr_t) == "-hug":
          acced.send_message(chatId=data.message.chatId, message = """[CB]hug:
          
          Este comando le dara un gran abrazo. >w< """)
       if name_pr(pr_t) == "-help":
          acced.send_message(chatId=data.message.chatId, message = """[CB]help:
          
          ¿Qué? ¿Estas viendo para que sirve el help mientras usas el help? OMG. """)
       if name_pr(pr_t) == "-comment":
          acced.send_message(chatId=data.message.chatId, message = """[CB]comment:
          
          Te dare el comentario que quieras, ¡Pero ten cuidado! Un gran poder lleva una gran responsabilidad """ ) 

       if name_pr(pr_t) == "~kiss":
          acced.send_message(chatId=data.message.chatId, message = """[CB]kiss:
          
          Beso fantasma >w<""")
       if name_pr(pr_t) == "~meter":
          acced.send_message(chatId=data.message.chatId, message = """[CB]kiss:
          
          E-esto... Es para meter cosas..""")
       if name_pr(pr_t) == "~ban":
          acced.send_message(chatId=data.message.chatId, message = """[CB]ban:
          
          ban fantasma :3""")
       if name_pr(pr_t) == "-audio":
          acced.send_message(chatId=data.message.chatId, message = """[CB]audio:
          
          ¿Quieres escuchar mi voz? owo
          Para eso debes poner -audio """)

       if name_pr(pr_t) == "-img":
          acced.send_message(chatId=data.message.chatId, message = """[CB]audio:
          
          ¿Quieres ver mi pack... De imagenes? owo
          Para eso debes poner -img """)
          
    #comandos de guion: 

    if data.message.content.lower() == "-id": 
        acced.send_message(chatId=data.message.chatId, message = f"- comunidad = {acced.comId} \n- chat = {data.message.chatId}") 

    if command == "-id?":
       id = client.get_from_code(name_pr(pr_t)).objectId
       acced.send_message(chatId=data.message.chatId, message = f"-El id de este chat/comunidad es {id}") 

    if command == "-kill":
       user = acced.search_users(name_pr(pr_t))
       Search_users = user.json[0]["uid"]
       acced.send_message(chatId=data.message.chatId, message = f"<$@{data.message.author.nickname}$>, mató a <${name_pr(pr_t)}$>", mentionUserIds=[str(data.message.author.userId), str(Search_users)], replyTo=data.message.messageId)

    if command == "-hug":
        user = acced.search_users(name_pr(pr_t))
        Search_users = user.json[0]["uid"]
        acced.send_message(chatId=data.message.chatId, message = f"<$@{data.message.author.nickname}$> abraza con mucho amor a <${name_pr(pr_t)}$>... >w<", mentionUserIds=[str(data.message.author.userId), str(Search_users)], replyTo=data.message.messageId)  
    
    if command == "-comment":
        acced.comment(name_pr(pr_t),(data.message.author.userId))     
    if command == "-audio":
        os.chdir("Audio")
        audio = os.listdir()
        with open(str(random.choice(audio)), "rb") as file:
         acced.send_message(chatId=data.message.chatId, file=file, fileType="audio")
         os.chdir("..")

    if command == "-img":
        
        os.chdir("img")
        img = os.listdir()
        with open(str(random.choice(img)), "rb") as file: 
         acced.send_message(chatId=data.message.chatId,file=file, fileType="image")
         os.chdir("..")

    #Comando exclusivo


    if command == "-invite":
        id = client.get_from_code(name_pr(pr_t)).objectId
        acced.join_chat(id)
   
    if command == "-like_blog":
        id = client.get_from_code(name_pr(pr_t)).objectId
        for x in range(20):
          acced.like_blog(id)
          print(x)

    #Comandos con virgulilla:

    if command == "~kiss":
        acced.send_message(chatId=data.message.chatId, message = f"<$@{data.message.author.nickname}$> besó apasionadamente a  <${name_pr(pr_t)}$>...", messageType=100) 
        os.system("clear")

    if command == "~ban":
        acced.send_message(chatId=data.message.chatId, message = f"<$@{data.message.author.nickname}$> baneó del chat a  <${name_pr(pr_t)}$>...", messageType=100) 
        os.system("clear") 

    if command == "~meter":
        acced.send_message(chatId=data.message.chatId, message = f"el Dios todo poderoso <$@{data.message.author.nickname}$> va a desactivarme metiendome un <${name_pr(pr_t)}$>...", messageType=100) 
        os.system("clear")

    if command == "-terminal":
        acced.send_message(chatId=data.message.chatId, message = f"<$@{data.message.author.nickname}$> Esta procesando el comando: <${name_pr(pr_t)}$>...") 
        output = subprocess.check_output(f"{name_pr(pr_t)}", shell=True)
        acced.send_message(chatId=data.message.chatId, message = f"{output.decode('utf-8')}\n\n") 
    #comandos para admin

    #ESTE BOT NO ES PARTE DEL STAFF.
    
socketDelay()

#Standby