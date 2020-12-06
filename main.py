import random
from copy import deepcopy
from RPS_Agent import *
class RandomPredictor():

    @staticmethod
    def predict():
        return random.choice(POSSIBLE_MOVES)
    
random_predictor = RandomPredictor()

scores = []
for q in range(100):
    agent=RPS_Agent(0.1)
    for i in range(1000):
        random_move = random_predictor.predict()
        agent.play_RPS(random_move)
    scores.append(agent.scores)

win_count, draw_count, loss_count = 0,0,0
for score in scores:
    if score['agent'] > score['opponent']:
        win_count += 1
    elif score['agent'] < score['opponent']:
        loss_count += 1
    else:
        draw_count += 1
    
print("W:{} - D:{} - L:{}".format(win_count,draw_count,loss_count))
