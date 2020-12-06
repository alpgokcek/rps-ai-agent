import random
from copy import deepcopy
from RPS_Agent import *
class RandomPredictor():

    @staticmethod
    def predict():
        #return random.choices(POSSIBLE_MOVES, weights=[0.4,0.2,0.4])[0]
        return random.choice(POSSIBLE_MOVES)

random_predictor = RandomPredictor()

scores = []
agent=RPS_Agent(0.1)
for q in range(100):
    for i in range(1000):
        random_move = random_predictor.predict()
        #move = input("Enter your move: ")
        agent.play_RPS(random_move)
    #print()
    #agent.print_results()
    #agent.print_transition_matrix()
    scores.append(agent.scores)
    agent.scores = {'agent': 0, 'draw': 0, 'opponent': 0}

win_count, draw_count, loss_count = 0,0,0
for score in scores:
    if score['agent'] > score['opponent']:
        win_count += 1
    elif score['agent'] < score['opponent']:
        loss_count += 1
    else:
        draw_count += 1
    
print("W:{} - D:{} - L:{}".format(win_count,draw_count,loss_count))
