from email import header
from multiprocessing.connection import Client
from pydoc import cli


from discord.ext import commands, tasks

import discord
import random
import schedule
import time






Token="OTYxNDk5MTg4OTA5MjA3NjIy.Yk535g.GUqwpA8YKKGApHOgwe6xUrDo55g"








client= discord.Client()





@tasks.loop(minutes=1)
@client.event
# async def on_message(message):
async def test():
    # general_channel = client.get_channel(int(903145625305108541))
    general_channel = client.get_channel(int(961895973393682453))

   
    print("Message sending on Discord channel")
    await general_channel.send("HELLO")
       


@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    test.start()

client.run(Token)
    



@client.event
async def on_message(message):
    
    username = str().split("#")[0]
    user_message = str()
    channel = str(channel.name)
    print(f'{username} : {user_message} : ({channel})' )
    
   

  



# # automated messages
   
    if message.channel.name == "testing-channel":
              
        
    
    
  
        if user_message.lower()=="hello":
            await message.channel.send('see you later !')
            return


 
    
#         # elif user_message.lower()=="bye":
#         #     await message.channel.send(f'see you later {username}!')
#         #     return
        
#         # elif user_message.lower()=="!random":
#         #     response=f'this is your random number : {random.randrange(10000000)}'
#         #     await message.channel.send(response)
           
       
    

#     if user_message.lower()=="!anywhere":
#         await channel.send('This can be used anywhere')
#         return
    





