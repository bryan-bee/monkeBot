import discord


def run_discord_bot():
    TOKEN = 'MTA5Nzk3ODQyMDE0ODgzODQyMA.Gi3QzM.ZFz337Yp1m0VKiitqTjXnoMsXpTbjKKYvR_p00'
    intents = discord.Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)

    # The message the bot will print out when it is logged in and ready
    @client.event
    async def on_ready():
        print('Monke is ready and logged in')

    # checks if the message is from the bot itself
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        trigger1 = ["i'm", "im", "i;m", "lm", "l'm", "i am", "i’m"]
        trigger2 = ["omg", "omg...", "omg.", "omg..", "christ", "shit", "god", "wtf"]
        content = message.content.lower().split()
        if message.content == 'dance monke':
            await message.channel.send("https://tenor.com/view/donkey-kong-country-dancing-dance-donkey-kong"
                                       "-boombox-gif-18467530")
        # for ( int idx=0; idx<= number of words ; idx++)
        for idx in range(len(content)):
            if content[idx] in trigger2 and (idx == len(content) - 1 or content[idx + 1] == ""):
                await message.channel.send("it's Jason Bourne")
                return
            elif content[idx] in trigger1 and idx != len(content) - 1 and content[idx + 1] != "":
                # the : after 1 means, everything after, 2:4 would go from idx 2 thru 4, but since its empty after :,
                # it'll keep joining any words until the end
                phrase = ' '.join(content[idx + 1:])
                # await means its asynchronous message.channel gets the channel the message was originally sent from,
                # then we do .send to send a message back to the same channel
                await message.channel.send("Hello " + phrase + " , I'm monke bot OOO OOO AHH AHH")
                return

    client.run(TOKEN)
