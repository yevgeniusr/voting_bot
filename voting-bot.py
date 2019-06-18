import discord
import creds

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!vote'):
        message_list = message.content.split(' ')
        if len(message_list) < 4:
            err_msg = "{0.author.mention}: Incorrect usage: Not enough arguments. ".format(message)
            err_msg += "Correct usage: `!vote <write-topic-like-this> <option1> <option2>`"
            await message.channel.send(err_msg)
        else:
            topic = message_list[1]
            option1 = message_list[2]
            option2 = message_list[3]
            msg = "{0.author.mention} started a new poll.\n\n".format(message)
            msg += "Topic: " + topic + ". \n\n"
            msg += "Option1: " + option1 + ".\n"
            msg += "Option2: " + option2 + ".\n\n"
            msg += "Use thumbs up for Option 1 and thumbs down for option 2.\n"
            await message.channel.send(msg)
    
    if (message.author.name == 'Voting Bot') and ('Option' in message.content):
        emoji_thumbs_up = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji_thumbs_up)
        emoji_thumbs_down = '\N{THUMBS DOWN SIGN}'
        await message.add_reaction(emoji_thumbs_down)
        await message.pin()
        
@client.event
async def on_ready():
    print("Logged in as: ")
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    
client.run(creds.bot_token)