import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sum_counts = {k: 0 for k in range(2, 13)}  # Від 2 до 12 (включно)

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_dice = die1 + die2
        sum_counts[sum_dice] += 1

    return sum_counts


def calculate_probabilities(sum_counts, num_rolls):
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    return probabilities


def plot_probabilities(probabilities):
    lists = sorted(probabilities.items())  # Відсортовані ключі і значення для плавного графіка
    x, y = zip(*lists)
    plt.bar(x, y, color='blue')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probability of Dice Rolls Sums')
    plt.xticks(range(2, 13))  # Відображення всіх можливих сум на осі X
    plt.show()


num_rolls = 1000000

sum_counts = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sum_counts, num_rolls)

plot_probabilities(probabilities)

print("Sum Probabilities:")
for sum_val, prob in probabilities.items():
    print(f"Sum {sum_val}: {prob:.4f}")