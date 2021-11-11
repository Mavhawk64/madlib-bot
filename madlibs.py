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

games.append(Game(1,"MadLib Bot#2264"))
for i in range(0, 23):
	thegame = games[len(games)-1].game
	# print(thegame.params)
	# print(thegame.get_params())
	thegame.params.append("test")
