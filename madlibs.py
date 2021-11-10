class MadLibs(object):
    story_zero = ["an adjective","an adjective","a verb ending in 'ing'","a place","an adjective","a plural noun","a plural noun","a verb","an adjective","a part of the body (plural)","a verb","a part of the body","a silly word","an adjective","a plural noun"]
    param_count = [story_zero]
    params = []
    story = 0
    def __init__(self,user,story):
        print("Madlib started for: " + str(user))
        self.params = []
        self.story = story
    def create_story(self):
        return "Putting on a newscast might look easy, but it takes a lot of " + self.params[0] + " work. Go behind the scenes, and you'll see dozens of " + self.params[1] + " workers " + self.params[2] + " in every direction! Reporters run back and forth between the studio and locations all around (the) " + self.params[3] + " to cover " + self.params[4] + " stories and interview " + self.params[5] + ". They are joined by videographers who operate handheld " + self.params[6] + " to capture all the action. The anchors are the people who " + self.params[7] + " behind the news deck and read the stories during the newscast. They have to look " + self.params[8] + " on air, so they can often be found getting makeup applied to their " + self.params[9] + ". The director tells everyone where and when to " + self.params[10] + ". It's easy to spot a director because he wears a headset on his " + self.params[11] + " and yells things like \"Camera two!\" and \"Cut to commercial!\" and \"" + self.params[12] + "!\" A newscast is live television, so if you make a/an " + self.params[13] + " mistake, everyone watching at home on their " + self.params[14] + " will know!"
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



games = []

games.append(Game(0,"MadLib Bot#2264"))

for i in range(0,15):
	games[len(games)-1].game.params.append("test")
	# print(thegame.get_params())
	# thegame.params.append("test")

games.append(Game(0,"Testing#1234"))
for i in range(0,15):
	games[len(games)-1].game.params.append("testing")

print(games[0].game.params)
print(games[1].game.params)

print(games)
# print(games[0].game.create_story())
games.pop(0)

print(games)

games.append(Game(0,"MadLib Bot#2264"))
for i in range(0, 15):
	thegame = games[len(games)-1].game
	print(thegame.params)
	exit()
	# print(thegame.get_params())
	thegame.params.append("test")
