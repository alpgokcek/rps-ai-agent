def predict(self):
    global POSSIBLE_MOVES, beats
    if len(self.predictions) == 0:
        prediction = random.choices(population=POSSIBLE_MOVES, weights=[0.45, 0.35, 0.20], k=1)
        return prediction[0]
    elif len(self.predictions) in range(1, len(LAST_POSSIBLE_MOVES[0])):
        last_prediction, last_move = beats[self.predictions[-1]], self.moves[-1]
        last_result = self.get_result(last_prediction, last_move)

        if last_result in [0,1]:
            prediction = beats[last_prediction]
        else:
            prediction = beats[last_move]
        return prediction
    else:
        row = self.transition_matrix[self.last_moves]
        if max(row) == min(row):
            return random.choices(POSSIBLE_MOVES, [0.35, 0.30, 0.35], k=1)[0]
        else:
            if min(row) * random.uniform(1.7, 3) <= max(row):
                return random.choices(POSSIBLE_MOVES, weights=[1-prob for prob in row], k=1)[0]
            else:
                return random.choices(POSSIBLE_MOVES, row, k=1)[0]
