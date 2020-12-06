import random
from copy import deepcopy

ROCK, PAPER, SCISSORS = 'R', 'P', 'S'
POSSIBLE_MOVES= [ROCK, PAPER, SCISSORS]
LAST_POSSIBLE_MOVES = [
    'RRR', 'RRP', 'RRS', 'RPR', 'RPP', 'RPS', 'RSR', 'RSP', 'RSS',
    'PRR', 'PRP', 'PRS', 'PPR', 'PPP', 'PPS', 'PSR', 'PSP', 'PSS',
    'SRR', 'SRP', 'SRS', 'SPR', 'SPP', 'SPS', 'SSR', 'SSP', 'SSS',
    ]
beats = { ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}

class RPS_Agent():
    def __init__(self, decay):
        self.scores = {'agent': 0, 'draw': 0, 'opponent': 0}
        self.last_moves = '   '
        self.transition_matrix = dict()
        self.transition_sum_matrix = dict()
        self.moves = []
        self.predictions = []
        self.decay = decay
        self.create_transition_matrix()

    def create_transition_matrix(self):
        global LAST_POSSIBLE_MOVES, POSSIBLE_MOVES
        for index, dict_key in enumerate(LAST_POSSIBLE_MOVES):
            self.transition_matrix[dict_key] = [1/len(POSSIBLE_MOVES)]*len(POSSIBLE_MOVES)
            self.transition_sum_matrix[dict_key] = [1]*len(POSSIBLE_MOVES)

    def print_transition_matrix(self):
        global POSSIBLE_MOVES
        print('\t  ', '\t  '.join('{}'.format(x) for x in POSSIBLE_MOVES))
        for key in self.transition_matrix.keys(): print('{}\t'.format(key), '\t'.join('{0:.3f}'.format(x) for x in self.transition_matrix[key]))

    def print_results(self):
        print("Results:")
        print("Agent:\t", self.scores['agent'])
        print("Draw:\t", self.scores['draw'])
        print("Opponent:\t", self.scores['opponent'])
        if self.scores['agent'] > self.scores['opponent']:
            print("Agent won!")  
        elif self.scores['agent'] == self.scores['opponent']:
            print("Draw!")
        else:
            print("Opponent won!")
    def train(self, opponent_move):
        self.moves.append(opponent_move)
        self.update_transition_matrix(opponent_move)
        self.last_moves = self.last_moves[1:] + opponent_move


    def update_transition_matrix(self, opponent_move):
        global POSSIBLE_MOVES
        if len(self.moves) <= 3:
            return None
        for i in range(len(self.transition_sum_matrix[self.last_moves])):
            self.transition_sum_matrix[self.last_moves][i] = self.decay * self.transition_sum_matrix[self.last_moves][i]
        self.transition_sum_matrix[self.last_moves][POSSIBLE_MOVES.index(opponent_move)] += 1

        transition_matrix_row = deepcopy(self.transition_sum_matrix[self.last_moves])
        
        row_sum = sum(transition_matrix_row)
        transition_matrix_row[:] = [count/row_sum for count in transition_matrix_row]

        self.transition_matrix[self.last_moves] = transition_matrix_row


    def predict(self):
        global POSSIBLE_MOVES, beats
        if len(self.predictions) == 0:
            prediction = random.choices(population=POSSIBLE_MOVES, weights=[0.45, 0.35, 0.20], k=1)
            return prediction[0]
        elif len(self.predictions) in [1,2]:
            last_prediction, last_move = beats[self.predictions[-1]], self.moves[-1]
            last_result = self.get_result(last_prediction, last_move)

            if last_result in [0,1]:
                prediction = beats[last_prediction]
            else:
                prediction = beats[last_move]
            return prediction
        else:
            #predict from model
            row = self.transition_matrix[self.last_moves]
            if max(row) == min(row):
                return random.choices(POSSIBLE_MOVES, [0.35, 0.30, 0.35], k=1)[0]
            else:
                return POSSIBLE_MOVES[row.index(max(row))]

    def make_move(self):
        global beats
        prediction = self.predict()
        self.predictions.append(prediction)
        return beats[prediction]
    
    def update_results(self, move, opponent):
        result = self.get_result(move, opponent)
        if result == 1: self.scores['agent'] += 1
        elif result == -1: self.scores['opponent'] += 1
        else: self.scores['draw'] += 1
    
    def get_result(self, move, opponent):
        '''
        # takes prediction and compares with opponent's move
        # @param turn (str)         prediction of our model
        # @param opponent (str)     opponent's move
        # @returns (int)            1, if prediction beats opponent
        #                           0, if prediction is same with opponent
        #                           -1, if opponent beats prediction
        '''
        global beats
        if beats[move] == opponent:
            return 1
        elif beats[opponent] == move:
            return -1
        else:
            return 0
    def play_RPS(self, opponent_move):
        global beats
        agent_move = self.make_move()
        self.update_results(agent_move, opponent_move)
        self.train(opponent_move)
        #print("Agent {} - {} Opponent".format(beats[self.predictions[-1]], opponent_move))
