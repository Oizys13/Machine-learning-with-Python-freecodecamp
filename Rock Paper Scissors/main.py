from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import play_response
from unittest import main

# Uncomment to play against Quincy:
# play(play_response, quincy, 1000)

# Uncomment to play against Abbey:
# play(play_response, abbey, 1000)

# Uncomment to play against Kris:
# play(play_response, kris, 1000)

# Uncomment to play against Mrugesh:
# play(play_response, mrugesh, 1000)

# Uncomment to play interactively against Abbey:
# play(human, abbey, 20, verbose=True)

# Uncomment to play against a random strategy bot:
# play(human, random_player, 1000)

# Uncomment to run unit tests automatically
main(module='test_module', exit=False)
