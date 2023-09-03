import discord
from discord.ext import commands
from discord import app_commands
import openai

trigger1 = ["i'm", "im", "i;m", "lm", "l'm", "i am", "i’m"]
trigger2 = ["omg", "omg...", "omg.", "omg..", "christ", "shit", "god", "wtf"]

openai.api_key = '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'

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    # The message the bot will print out when it is logged in and ready
    @client.event
    async def on_ready():
        print('Monke is ready and logged in')
        await tree.sync()

    def gpt(message):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages = [{'role': 'system', 'content': message}],
            max_tokens = 1000
        )

        model_reply = response['choices'][0]['message']['content']        # if response_dict and len(response_dict) > 0:
        #     message_response = response_dict[0]["text"]
        return model_reply

    @tree.command(name = "monke", description = "Chat GPT but monke")
    async def first_command(interaction: discord.Interaction, mess: str):
        prompt = "you are to act like an intelligent monkey and also end every message with OOH OOH AHH AHH. "
         # Get the arguments provided by the user
        response = gpt(prompt + mess)
        await interaction.response.send_message("(" + mess + ")" + "\n" + "```\n" + response + "\n```")
    
    # checks if the message is from the bot itself
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        content = message.content.lower().split()  

        if message.content.lower().strip() == 'dance monke':
            await message.channel.send("https://tenor.com/view/donkey-kong-country-dancing-dance-donkey-kong"
                                       "-boombox-gif-18467530")
            
        if message.content.lower().strip() in  ['goodbye monke','bye monke']:
            await message.channel.send("https://tenor.com/view/i-dont-wanna-go-spider-man-gif-14959755")

        for idx in range(len(content)):
            if content[idx] in trigger2 and (idx == len(content) - 1 or content[idx + 1] == ""):
                await message.channel.send("it's Jason Bourne")
                return
            elif content[idx] in trigger1 and idx != len(content) - 1 and content[idx + 1] != "":
                for word in content:
                    if '@' in word:
                        user = str(message.author)
                
                        prefix, suffix = message.content.split('@')
                        directed = suffix
                            
                        await message.channel.send("@" + directed + ", " + user + " is using me to ping you. OOH OOH AHH AHH")
                        return
                else:
                    # the : after 1 means, everything after, 2:4 would go from idx 2 thru 4, but since its empty after :,
                    # it'll keep joining any words until the end
                    phrase = ' '.join(content[idx + 1:])
                    # await means its asynchronous message.channel gets the channel the message was originally sent from,
                    # then we do .send to send a message back to the same channel
                    await message.channel.send("Hello " + phrase + " , I'm monke bot OOO OOO AHH AHH")
                    return


    client.run('MTA5Nzk3ODQyMDE0ODgzODQyMA.GxE7Dj.K8VMk_60Q9AaWyp834VvaupOfp-QL5GPtxc_rc')