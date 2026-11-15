"""Monte Carlo simulation of a simple gambling game.

Each player starts with a fixed amount of money and bets the same amount on
each fair coin toss. A win earns the stake and a loss removes it. The
simulation estimates the probability of going bankrupt before the time limit.
"""

from dataclasses import dataclass
import random


@dataclass
class GameResult:
	"""Outcome of one gambling game."""

	final_balance: float
	rounds_played: int
	went_bankrupt: bool


def play_game(
	starting_balance: float,
	stake: float,
	win_probability: float,
	max_rounds: int,
	rng: random.Random,
) -> GameResult:
	"""Play one game and return its result."""
	balance = starting_balance
	rounds_played = 0

	while balance >= stake and rounds_played < max_rounds:
		rounds_played += 1
		if rng.random() < win_probability:
			balance += stake
		else:
			balance -= stake

	return GameResult(
		final_balance=balance,
		rounds_played=rounds_played,
		went_bankrupt=balance < stake,
	)


def run_simulation(
	number_of_games: int = 10_000,
	starting_balance: float = 100.0,
	stake: float = 10.0,
	win_probability: float = 0.5,
	max_rounds: int = 100,
	seed: int = 42,
) -> tuple[float, float, float]:
	"""Run many games and return ruin rate, average balance, and average rounds."""
	if number_of_games <= 0:
		raise ValueError("number_of_games must be greater than zero")
	if starting_balance <= 0 or stake <= 0:
		raise ValueError("starting_balance and stake must be greater than zero")
	if stake > starting_balance:
		raise ValueError("stake cannot be greater than starting_balance")
	if not 0 < win_probability < 1:
		raise ValueError("win_probability must be between 0 and 1")
	if max_rounds <= 0:
		raise ValueError("max_rounds must be greater than zero")

	rng = random.Random(seed)
	results = [
		play_game(starting_balance, stake, win_probability, max_rounds, rng)
		for _ in range(number_of_games)
	]
	ruin_rate = sum(result.went_bankrupt for result in results) / number_of_games
	average_balance = sum(result.final_balance for result in results) / number_of_games
	average_rounds = sum(result.rounds_played for result in results) / number_of_games
	return ruin_rate, average_balance, average_rounds


def main() -> None:
	"""Read experiment settings from the user and display the results."""
	print("Gambling Game Monte Carlo Simulation")
	print("Enter the experiment settings below.")

	try:
		settings = {
			"number_of_games": int(input("Number of games [10000]: ") or 10_000),
			"starting_balance": float(input("Starting balance [100]: ") or 100),
			"stake": float(input("Stake per round [10]: ") or 10),
			"win_probability": float(input("Win probability, 0 to 1 [0.5]: ") or 0.5),
			"max_rounds": int(input("Maximum rounds per game [100]: ") or 100),
			"seed": int(input("Random seed [42]: ") or 42),
		}
		ruin_rate, average_balance, average_rounds = run_simulation(**settings)
	except ValueError as error:
		print(f"\nInput error: {error}")
		return

	print("-------------------------------------")
	print(f"Games simulated:       {settings['number_of_games']:,}")
	print(f"Starting balance:      ${settings['starting_balance']:.2f}")
	print(f"Stake per round:       ${settings['stake']:.2f}")
	print(f"Win probability:       {settings['win_probability']:.0%}")
	print(f"Maximum rounds:        {settings['max_rounds']}")
	print(f"Probability of ruin:   {ruin_rate:.2%}")
	print(f"Average final balance: ${average_balance:.2f}")
	print(f"Average rounds played: {average_rounds:.2f}")


if __name__ == "__main__":
	main()