import random
from copy import deepcopy
from RPS_Agent import *
class RandomPredictor():

    @staticmethod
    def predict():
        return random.choices(POSSIBLE_MOVES, weights=[0.4,0.2,0.4])[0]
        #return random.choice(POSSIBLE_MOVES)


def get_move(agent, is_random=False):
    if not is_random:
        last_prediction, last_move = beats[agent.predictions[-1]], agent.moves[-1]
        last_result = agent.get_result(last_prediction, last_move)
        if last_result in [0,1]:
            prediction = beats[last_prediction]
        else:
            prediction = beats[last_move]
    else:
        random_move = random_predictor.predict()
    return prediction

        

random_predictor = RandomPredictor()

scores = []
agent=RPS_Agent(0.5)
for j in range(1):
    agent.print_transition_matrix()
    for i in range(10):
        if i == 0:
            random_move = random_predictor.predict()
        else:
            random_move = get_move(agent)
        #move = input("Enter your move: ")
        agent.play_RPS(random_move)
    #print()
    agent.print_results()
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
