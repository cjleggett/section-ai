import random

def elevator_prob(N=10000):
    """
    This function should run N simulations of the elevator problem, and
    return the approximate probability of 3 consecutive floors
    """
    def elevator_sim():
        floors = {random.randrange(2, 11) for _ in range(3)}
        return len(floors) == 3 and max(floors) - min(floors) == 2

    simulations = [elevator_sim() for _ in range(N)]
    return sum(simulations) / N

def birthday_prob(num, N=10000):
    """
    This function should run N simulations of the birthday problem,
    and return the approximate probability of a shared birthday.
    """
    def birthday_sim():
        birthdays = {random.randrange(365) for _ in range(num)}
        return len(birthdays) != num

    simulations = [birthday_sim() for _ in range(N)]
    return sum(simulations) / N

def monty_hall_prob(N=10000):
    """
    This function should run N simulations of the game show problem,
    and return the approximate probability of winning by switching doors.
    """
    def monty_sim():
        doors = ["Goat", "Goat", "Car"]
        random.shuffle(doors)
        initial_choice = random.randrange(3)
        for i in range(3):
            if doors[i] != "Car" and i != initial_choice:
                monty_reveal = i
                break
        final_choice = ({0, 1, 2} - {initial_choice, monty_reveal}).pop()
        return doors[final_choice] == "Car"

    simulations = [monty_sim() for _ in range(N)]
    return sum(simulations) / N


print(f"Elevator probability: {elevator_prob()}")
print(f"Brithday probability with 10 people: {birthday_prob(10)}")
print(f"Brithday probability with 20 people: {birthday_prob(20)}")
print(f"Brithday probability with 30 people: {birthday_prob(30)}")
print(f"Probability of winning when switching: {monty_hall_prob()}")