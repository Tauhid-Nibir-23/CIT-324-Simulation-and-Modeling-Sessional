"""
Monte Carlo Simulation of a Gambling Game (সহজ সংস্করণে লিখিত)
"""

import random


def play_one_game(starting_balance, stake, win_probability, max_rounds):
    balance = starting_balance
    rounds_played = 0

    while balance >= stake and rounds_played < max_rounds:
        rounds_played = rounds_played + 1

        if random.random() < win_probability:
            balance = balance + stake  
        else:
            balance = balance - stake  

    went_bankrupt = (balance < stake)

    return balance, rounds_played, went_bankrupt


def run_simulation(number_of_games, starting_balance, stake, win_probability, max_rounds, seed):
    random.seed(seed)

    total_bankrupt_count = 0
    total_final_balance = 0.0
    total_rounds_played = 0

    for i in range(number_of_games):
        balance, rounds, went_bankrupt = play_one_game(
            starting_balance, stake, win_probability, max_rounds
        )

        if went_bankrupt:
            total_bankrupt_count = total_bankrupt_count + 1

        total_final_balance = total_final_balance + balance
        total_rounds_played = total_rounds_played + rounds

    ruin_rate = total_bankrupt_count / number_of_games
    average_balance = total_final_balance / number_of_games
    average_rounds = total_rounds_played / number_of_games

    return ruin_rate, average_balance, average_rounds


def main():
    print("Gambling Game Monte Carlo Simulation")
    print("Enter the experiment settings below.\n")

    games_input = input("Number of games [10000]: ")
    if games_input == "":
        number_of_games = 10000
    else:
        number_of_games = int(games_input)

    balance_input = input("Starting balance [100]: ")
    if balance_input == "":
        starting_balance = 100.0
    else:
        starting_balance = float(balance_input)

    stake_input = input("Stake per round [10]: ")
    if stake_input == "":
        stake = 10.0
    else:
        stake = float(stake_input)

    prob_input = input("Win probability, 0 to 1 [0.5]: ")
    if prob_input == "":
        win_probability = 0.5
    else:
        win_probability = float(prob_input)

    rounds_input = input("Maximum rounds per game [100]: ")
    if rounds_input == "":
        max_rounds = 100
    else:
        max_rounds = int(rounds_input)

    seed_input = input("Random seed [42]: ")
    if seed_input == "":
        seed = 42
    else:
        seed = int(seed_input)

    ruin_rate, average_balance, average_rounds = run_simulation(
        number_of_games, starting_balance, stake, win_probability, max_rounds, seed
    )

    print("-------------------------------------")
    print(f"Games simulated:       {number_of_games}")
    print(f"Starting balance:      ${starting_balance:.2f}")
    print(f"Stake per round:       ${stake:.2f}")
    print(f"Win probability:       {win_probability * 100:.0f}%")
    print(f"Maximum rounds:        {max_rounds}")
    print(f"Probability of ruin:   {ruin_rate * 100:.2f}%")
    print(f"Average final balance: ${average_balance:.2f}")
    print(f"Average rounds played: {average_rounds:.2f}")


if __name__ == "__main__":
    main()