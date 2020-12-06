def update_transition_matrix(self, opponent_move):
    global POSSIBLE_MOVES
    if len(self.moves) <= len(LAST_POSSIBLE_MOVES[0]):
        return None
    for i in range(len(self.transition_sum_matrix[self.last_moves])):
        self.transition_sum_matrix[self.last_moves][i] *= self.decay
    self.transition_sum_matrix[self.last_moves][POSSIBLE_MOVES.index(opponent_move)] += 1

    transition_matrix_row = deepcopy(self.transition_sum_matrix[self.last_moves])
        
    row_sum = sum(transition_matrix_row)
    transition_matrix_row[:] = [count/row_sum for count in transition_matrix_row]
    self.transition_matrix[self.last_moves] = transition_matrix_row
