import numpy as np
from ddqn_agent import DDQNTrainer
from environment import HaliteEnvironment
import time

game_name = "Halite"
INPUT_SHAPE = (5,5,3)
ACTION_SPACE_SIZE = 5

total_run_limit = 200000
max_ep_steps = 100

run = 0
total_step = 0
total_step_limit = total_run_limit * max_ep_steps

game_model = DDQNTrainer(game_name, INPUT_SHAPE, ACTION_SPACE_SIZE)
env = HaliteEnvironment()

while True:
    if total_run_limit is not None and run >= total_run_limit:
        print("Reached total run limit of: " + str(total_run_limit))
        exit(0)

    run += 1
    current_state = env.reset()
    step = 0
    score = 0

    #print('')
    #print('Episode:', run)
    start = time.time()
    while step < max_ep_steps:
        if total_step >= total_step_limit:
            print("Reached total step limit of: " + str(total_step_limit))
            exit(0)

        total_step += 1
        step += 1

        #if render:
        #    env.render()

        if step == 1:
            action = 5
        elif step == 2:
            action = -1 # need to manually capture the yard action here, not a ship action
        else:
            action = game_model.move(current_state)

        # what is action type?
        # assume its an int - need to adjust environemnt
        next_state, reward, terminal, info = env.step(action)
        # reward will be the current halite at that time
        # score - wants to sum these up, but shouldn't really do that
        # could make reward the delta halite...

        #if clip:
        #    np.sign(reward)

        #score += reward
        if action not in [-1, 5]:
            game_model.remember(current_state, action, reward, next_state, terminal)
        #else:
        #    print("Skipping intro actions")

        current_state = next_state

        game_model.step_update(total_step)


    if run % 10 == 0:
        end = time.time()
        ep_duration = end - start
        print(ep_duration)
    score = env.board.observation['players'][0][0]
    #if terminal:
    #print(score)
    game_model.save_run(score, step, run)
    #break
