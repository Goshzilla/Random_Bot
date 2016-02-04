import discord

#email@email.com:password
fp_infos = open("infos.txt", "r")
infos = fp_infos.read().split(':')
fp_infos.close()

client = discord.Client()
client.login(infos[0], infos[1])

if not client.is_logged_in:
	print("Failed to login.")
	exit(1)
	
	
	
@client.event
def on_message(msg):
	if msg.content.startswith("!fun"):
		client.send_message(msg.channel, "No.")
	
	
@client.event
def on_ready():
	print("Bot is running as the user '()'".format(client.user.name))
		
	
	
print("Starting bot...")
client.run()