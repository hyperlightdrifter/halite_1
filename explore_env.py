from environment import HaliteEnvironment

game_name = "Halite"
INPUT_SHAPE = 12
ACTION_SPACE_SIZE = 5

max_ep_steps = 30

run = 0
total_step = 0

#game_model = DDQNTrainer(game_name, INPUT_SHAPE, ACTION_SPACE_SIZE)
env = HaliteEnvironment()

print(env.board)

env.step(5)
print(env.board)
z = env.board_to_obs(env.board)

print("")
print("")

env.step(-1)
print(env.board)
z = env.board_to_obs(env.board)

print("")
print("")

env.step(1)
z = env.board_to_obs(env.board)
env.step(1)
z = env.board_to_obs(env.board)
env.step(1)
print(env.board)
z = env.board_to_obs(env.board)
