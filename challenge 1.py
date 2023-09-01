from fractions import Fraction

# Total number of possible outcomes when rolling two dice
total_outcomes = 6 * 6

# Initialize a variable to count favorable outcomes
favorable_outcomes = 0

# Loop through all possible outcomes of two dice rolls
for die1 in range(1, 7):
    for die2 in range(1, 7):
        # Check if the values rolled are different and their sum is 6
        if die1 != die2 and die1 + die2 == 6:
            favorable_outcomes += 1

# Calculate the probability as a fraction
probability = Fraction(favorable_outcomes, total_outcomes)

# Print the probability as a fraction
print(probability)
