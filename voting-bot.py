import discord
import creds

client = discord.Client()
originalmessage=""

@client.event
async def on_message(message):
    if message.content.startswith('!vote'):
        message_list = message.content.split(' ')
        if len(message_list) < 4:
            err_msg = "{0.author.mention}: Incorrect usage: Not enough arguments. ".format(message)
            err_msg += "Correct usage: `!vote <write-topic-like-this> <emoji=option1> <emoji=option2> (For as many as you like)`"
            await message.channel.send(err_msg)
        else:
            topic = message_list[1]
            msg = "{0.author.mention} started a new poll.\n\n".format(message)
            msg += "Topic: " + topic + ". \n\n"
            # We have the topic, now lets run through and get each option
            option_count = len(message_list) #Total options
            i = 2 # To avoid !vote / topic
            while i < option_count:
                msg+="Option " + str(i-1) + " - " + message_list[i].split("=")[1] + " [ " + message_list[i].split("=")[0] + " ]" + "\n\n" 
                i += 1
            await message.channel.send(msg)
    
    if (message.author.name == 'Voting Bot') and ('Option' in message.content):
        # lets get the original message to find all emojis
        async for original_message in message.channel.history(limit=2):
            if original_message.author != message.author and original_message.content != message.content:
                message_list2 = original_message.content.split(' ')
                emoji_count = len(message_list2) #Total emojis
                j = 2 # To avoid !vote / topic
                while j < emoji_count:
                    emoji_current = message_list2[j].split("=")[0]
                    await message.add_reaction(emoji_current)
                    j += 1
                await original_message.delete()
        
@client.event
async def on_ready():
    print("Logged in as: ")
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    
client.run(creds.bot_token)
