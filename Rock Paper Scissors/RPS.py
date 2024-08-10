# This function tracks the opponent's moves and responds based on past patterns. It has different strategies to handle various cases.

move_history = []
initial_move = previous_move = 'S'
detected_patterns = [False, False, False, False]
move_mapping = {'P': 'R', 'R': 'S', 'S': 'P'}
pattern_counter = -1
move_counts = [{
    "RR": 0, 
    "RP": 0, 
    "RS": 0, 
    "PR": 0, 
    "PP": 0, 
    "PS": 0, 
    "SR": 0, 
    "SP": 0, 
    "SS": 0, 
    }]

def play_response(last_opponent_move, opponent_moves = []):
    global move_history, previous_move, detected_patterns, move_mapping, pattern_counter, move_counts
    opponent_moves.append(last_opponent_move)
    move_history.append(previous_move)

    # Quincy Pattern
    if len(set(detected_patterns)) == 1 and opponent_moves[-5:] == ['R', 'P', 'P', 'S', 'R']:
        detected_patterns[0] = True

    if detected_patterns[0]:
        if len(opponent_moves) % 1000 == 0:
            detected_patterns = [False, False, False, False]
            opponent_moves.clear()
            
        quincy_sequence = ['P', 'S', 'S', 'R', 'P']
        pattern_counter = (pattern_counter + 1) % 5
        return quincy_sequence[pattern_counter]
    
    # Abbey Pattern
    if len(set(detected_patterns)) == 1 and opponent_moves[-5:] == ['P', 'P', 'R', 'R', 'R']:
        detected_patterns[1] = True

    if detected_patterns[1]: 
        last_moves = ''.join(move_history[-2:])
        if len(last_moves) == 2:
            move_counts[0][last_moves] += 1
        possible_responses = [
            previous_move + 'R', 
            previous_move + 'P', 
            previous_move + 'S', 
            ]
        response_counts = {
            k: move_counts[0][k]
            for k in possible_responses if k in move_counts[0]
            }
        predicted_move = max(response_counts, key = response_counts.get)[-1:]
        
        if len(opponent_moves) % 1000 == 0:
            detected_patterns = [False, False, False, False]
            opponent_moves.clear()
            move_counts = [{
              "RR": 0, 
              "RP": 0, 
              "RS": 0, 
              "PR": 0, 
              "PP": 0, 
              "PS": 0, 
              "SR": 0, 
              "SP": 0, 
              "SS": 0, 
              }]

        previous_move = move_mapping[predicted_move]
        return previous_move

    # Kris Pattern
    if len(set(detected_patterns)) == 1 and opponent_moves[-5:] == ['P', 'R', 'R', 'R', 'R']:
        detected_patterns[2] = True

    if detected_patterns[2]:
        if len(opponent_moves) % 1000 == 0:
            detected_patterns = [False, False, False, False]
            opponent_moves.clear()
            
        previous_move = move_mapping[previous_move]
        return previous_move

    # Mrugesh Pattern
    if len(set(detected_patterns)) == 1 and opponent_moves[-5:] == ['R', 'R', 'R', 'R', 'R']:
        detected_patterns[3] = True
    
    if detected_patterns[3]:  
        if len(opponent_moves) == 1000:
            detected_patterns = [False, False, False, False]
            opponent_moves.clear()
            
        recent_moves = move_history[-10:]
        most_common = max(set(recent_moves), key = recent_moves.count)
        previous_move = move_mapping[most_common]
        return previous_move
    
    previous_move = initial_move
    return previous_move
