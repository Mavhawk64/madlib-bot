import discord
import os
from dotenv import load_dotenv
import requests
class MadLibs(object):
    adj = "an adjective"
    n = "a noun"
    v = "a verb"
    ving = "a verb ending in 'ing'"
    plv = "a plural verb"
    p = "a place"
    pln = "a plural noun"
    bdy = "a body part"
    silly = "a silly word"
    adv = "an adverb (typically ends in -ly)"
    story_zero = [adj,adj,ving,p,adj,pln,pln,v,adj,bdy + " (plural)",v,bdy,silly,adj,pln]
    story_star = [adj,n,adj,p,adj,adj,pln+" (vehicle)",adj,adj,pln,adj,pln,pln,adj,n,v+" (singular - ends in s)",adj,v,pln,pln+" (type of job)",adj,plv,adj]
    param_count = [story_zero,story_star]
    params = []
    story = 0
    def __init__(self,user,story):
        print("Madlib started for: " + str(user))
        self.params = []
        self.story = story
    def create_story(self):
        if self.story == 0:
            return "Putting on a newscast might look easy, but it takes a lot of " + self.params[0] + " work. Go behind the scenes, and you'll see dozens of " + self.params[1] + " workers " + self.params[2] + " in every direction! Reporters run back and forth between the studio and locations all around (the) " + self.params[3] + " to cover " + self.params[4] + " stories and interview " + self.params[5] + ". They are joined by videographers who operate handheld " + self.params[6] + " to capture all the action. The anchors are the people who " + self.params[7] + " behind the news deck and read the stories during the newscast. They have to look " + self.params[8] + " on air, so they can often be found getting makeup applied to their " + self.params[9] + ". The director tells everyone where and when to " + self.params[10] + ". It's easy to spot a director because he wears a headset on his " + self.params[11] + " and yells things like \"Camera two!\" and \"Cut to commercial!\" and \"" + self.params[12] + "!\" A newscast is live television, so if you make a/an " + self.params[13] + " mistake, everyone watching at home on their " + self.params[14] + " will know!"
        elif self.story == 1:
            return "Star Wars is a " + self.params[0] + " " + self.params[1] + " of " + self.params[2] + " versus evil in a " + self.params[3] + " far far away. There are " + self.params[4] + " battles between " + self.params[5] + " " + self.params[6] + " in " + self.params[7] + " space and " + self.params[8] + " duels with " + self.params[9] + " called  " + self.params[10] + "-sabers. " + self.params[11] + " called 'droids' are helpers and " + self.params[12] + " to the heroes. A " + self.params[13] + " power called The " + self.params[14] + " " + self.params[15] + " people to do " + self.params[16] + " things, like " + self.params[17] + " " + self.params[18] + ". The Jedi " + self.params[19] + " use The Force for the " + self.params[20] + " side, and the Sith " + self.params[21] + " it for the " + self.params[22] + " side."
        else:
            return ""
    def get_params(self):
        return "Enter " + self.param_count[self.story][len(self.params)]

class Game(object):
    story = 0
    user = None
    game = None
    def __init__(self,story,user):
        self.story = story
        self.user = user
        self.game = MadLibs(self.user,self.story)



command_key = '&'
reactor = 'Which of these stories would you like?\nReact to respond.'
games = []

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=command_key+"help"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_reaction_add(reaction,user):
    for a in games:
            if a.user == user:
                await reaction.message.channel.send('You already have a MadLib game going!')
                return
    if reaction.message.content == reactor and reaction.message.author == client.user and user != client.user:
        if reaction.emoji == u"\U0001F3A5":
            await reaction.message.channel.send('Starting News MadLib!')
            games.append(Game(0,user))
        elif reaction.emoji == u"\U0001F680":
            await reaction.message.channel.send('Starting Star Wars MadLib!')
            games.append(Game(1,user))
        else:
            await reaction.message.channel.send('I don\'t recognize that emoji.')
            return
        await reaction.message.channel.send(games[len(games)-1].game.get_params())

@client.event
async def on_message(message):
    gamer = message.author
    if gamer == client.user:
        return

    if message.content.startswith(command_key+'madlib'):
        for a in games:
            if a.user == gamer:
                await message.channel.send('You already have a MadLib game going!')
                return
        await message.channel.send('Starting MadLib Simulation!')
        react = await message.channel.send(reactor)
        await react.add_reaction(u"\U0001F3A5")
        await react.add_reaction(u"\U0001F680")
        return
    if message.content.startswith(command_key):
        userid = -1
        for i in range(0,len(games)):
            if games[i].user == gamer:
                userid = i
                break
        if userid != -1:
            thegame = games[userid].game
            thegame.params.append(message.content[len(command_key):])
            if len(thegame.param_count[thegame.story]) > len(thegame.params):
                await message.channel.send(thegame.get_params())
                return
            else:
                await message.channel.send(thegame.create_story())
                games.pop(userid)
                return
        await message.channel.send('You don\'t have an active MadLibs game going!\nType ' + command_key + 'madlib to start!')


        
client.run(os.getenv('TOKEN'))