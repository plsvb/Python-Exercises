import random

def monty_hall_simulation(num_experiments):
    switch_success = 0
    no_switch_success = 0

    for _ in range(num_experiments):
        # Doors setup: one car (1) and two goats (0)
        doors = [0, 0, 1]
        random.shuffle(doors)

        # Contestant makes an initial choice
        initial_choice = random.randint(0, 2)

        # Host opens a door that has a goat and is not the initial choice
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] == 0]
        door_opened_by_host = random.choice(remaining_doors)

        # Determine the remaining closed door that was not initially chosen or opened by the host
        remaining_closed_doors = [i for i in range(3) if i != initial_choice and i != door_opened_by_host]

        # If the player switches, they switch to the remaining closed door
        switch_choice = remaining_closed_doors[0]

        # Check if switching results in a win
        if doors[switch_choice] == 1:
            switch_success += 1

        # Check if not switching results in a win
        if doors[initial_choice] == 1:
            no_switch_success += 1

    return switch_success, no_switch_success

# Run the simulation 100 times
num_experiments = 100
switch_success, no_switch_success = monty_hall_simulation(num_experiments)

print(f"Success times if you switch: {switch_success} out of {num_experiments}")
print(f"Success times if you do not switch: {no_switch_success} out of {num_experiments}")
