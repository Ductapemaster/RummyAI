import humanAgent
import dumbAI
import gameRunner


agents = []
for i in range(2):
	#agents.append(humanAgent.HumanAgent())
	agents.append(dumbAI.DumbAI())
	

gr = gameRunner.GameRunner() 

wins = [0,0]
score = [0]*len(agents)

for i in range(100):
	g = gameRunner.GamePackage(agents)
	gr.playGame(g)
	print("Game %d: player %d went out! p0 score: %d, p1 score: %d" % (i, g.winner, g.score[0], g.score[1]))
	if(g.winner == -1):
		print (g.game)
		break

	wins[g.winner] += 1
	for i in range(len(agents)):
		score[i] += g.score[i]

	print("Totals: p0 score: %d, p1 score: %d, p0 hands won %d, p1 hands won %d" % (score[0], score[1], wins[0], wins[1]))
	
