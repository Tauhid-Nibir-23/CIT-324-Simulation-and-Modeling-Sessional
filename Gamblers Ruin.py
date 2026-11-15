"""
Monte Carlo Simulation of a Gambling Game 
"""

import random


# ১. একটি একক গেম খেলার ফাংশন (Play one game)
def play_one_game(starting_balance, stake, win_probability, max_rounds):
    balance = starting_balance
    rounds_played = 0

    # যতক্ষণ টাকা বাজির সমান/বেশি থাকবে এবং সর্বোচ্চ রাউন্ড পার না হবে
    while balance >= stake and rounds_played < max_rounds:
        rounds_played = rounds_played + 1

        # ০ থেকে ১ এর মধ্যে র‍্যান্ডম সংখ্যা আসবে
        if random.random() < win_probability:
            balance = balance + stake   # জিতলে টাকা যোগ হবে
        else:
            balance = balance - stake   # হারলে টাকা বিয়োগ হবে

    # প্লেয়ার ব্যাংকরাপ্ট বা নিঃস্ব হয়েছে কিনা চেক করা
    went_bankrupt = (balance < stake)

    # রেজাল্ট ফেরত দেওয়া
    return balance, rounds_played, went_bankrupt


# ২. পুরো সিমুলেশন চালানোর ফাংশন (Run simulation)
def run_simulation(number_of_games, starting_balance, stake, win_probability, max_rounds, seed):
    # র‍্যান্ডম সীড সেট করা (যাতে প্রতিবার একই রেজাল্ট পাওয়া যায়)
    random.seed(seed)

    # মোট হিসাব রাখার জন্য ভ্যারিয়েবল
    total_bankrupt_count = 0
    total_final_balance = 0.0
    total_rounds_played = 0

    # সব খেলা এক এক করে চালানো
    for i in range(number_of_games):
        balance, rounds, went_bankrupt = play_one_game(
            starting_balance, stake, win_probability, max_rounds
        )

        if went_bankrupt:
            total_bankrupt_count = total_bankrupt_count + 1

        total_final_balance = total_final_balance + balance
        total_rounds_played = total_rounds_played + rounds

    # গড় বা Average হিসাব করা
    ruin_rate = total_bankrupt_count / number_of_games
    average_balance = total_final_balance / number_of_games
    average_rounds = total_rounds_played / number_of_games

    return ruin_rate, average_balance, average_rounds


# ৩. প্রধান ফাংশন (Main Function)
def main():
    print("Gambling Game Monte Carlo Simulation")
    print("Enter the experiment settings below.\n")

    # ইউজার ইনপুট নেওয়া এবং খালি রাখলে ডিফল্ট মান বসানো
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

    # সিমুলেশন চালানো
    ruin_rate, average_balance, average_rounds = run_simulation(
        number_of_games, starting_balance, stake, win_probability, max_rounds, seed
    )

    # ফলাফল সুন্দরভাবে প্রিন্ট করা
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