import requests
import discord
from discord.ext import commands, tasks
import schedule
import time

TOKEN = 'OTAzMTQ1NjI1MzA1MTA4NTQx.YXot6A.GbYZ6K1m5qOrRwKCSs4-qQdl4SA'
client = discord.Client()

	
@tasks.loop(minutes=1)
@client.event
# async def on_message(message):
async def test():
    # general_channel = client.get_channel(int(903145625305108541))
    general_channel = client.get_channel(int(902165383165923422))

    header = {
        'Content-Type': 'application/json'
    }
    # data = requests.get('http://127.0.0.1:8000/api/v1/producturl/', headers=header)
    data = requests.get('http://3.12.241.102/api/v1/producturl/', headers=header)
    print(data)
    product_data = data.json()
    print(len(product_data))
    for product in product_data:
        if product['status'] == True:
            header = {
                'Content-Type': 'application/json'
                }
            id = str(product['id'])
            myEmbed = discord.Embed(
                title = "Title",
                description = product['product_name'],
                colour = discord.Color.blue()
            )
            myEmbed.set_footer(text="This is the footer")
            myEmbed.set_image(url=product['product_image'])
            myEmbed.set_thumbnail(url=product['product_image'])
            myEmbed.set_author(name=client.user, icon_url=client.user.avatar_url)
            myEmbed.add_field(name="**Current Price**", value="$" + product['product_price'], inline=True)
            myEmbed.add_field(name="Resell Price", value="$" + product['resell_price'], inline=True) 
            myEmbed.add_field(name="Profitt", value="$" + product['profit_price'], inline=True)
            myEmbed.add_field(name="Url link:", value="**[CLICK ME](%s)**" % product['product_url'], inline=True)
            myEmbed.add_field(name="Useful link:", value="**[Ebay](%s) | [Cragslist](%s)**" % (product['product_url'], product['product_url']), inline=True)
            myEmbed.add_field(name="Checkout link:", value="**[Checkout](%s)**" % product['product_url'], inline=True)

            prod_data = requests.delete('http://3.12.241.102/prod/delete/'+id, headers=header)
            # prod_data = requests.delete('http://127.0.0.1:8000/prod/delete/'+id, headers=header)
            # await message.channel.send(embed=myEmbed)
            print("Message sending on Discord channel")
            await general_channel.send(embed=myEmbed)
        else:
            print("Status => False")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    test.start()

client.run(TOKEN)
