import random

def elevator_prob(N=10000):
    """
    This function should run N simulations of the elevator problem, and
    return the approximate probability of 3 consecutive floors
    """
    successes = 0
    for i in range(N):
        floors = {random.randint(2, 10) for _ in range(3)}
        success = len(floors) == 3 and max(floors) - min(floors) == 2
        successes += int(success)
    return successes / N

print(elevator_prob())



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

print(birthday_prob(int(input("N: "))))

def monty_hall_prob(N=10000):
    """
    This function should run N simulations of the game show problem,
    and return the approximate probability of winning by switching doors.
    """
    return 0