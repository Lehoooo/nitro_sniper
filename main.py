import discum
import json


configopen = open("config.json", "r")
config = json.loads(configopen.read())
configopen.close()

bot = discum.Client(token=str(config['token']))


@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        content = m['content']
        if "discord.gift" in content:
            print("Gift Detected")
            print(str(content))



bot.gateway.run(auto_reconnect=True)
