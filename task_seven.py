import random
import matplotlib.pyplot as plt

def simulate_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}  
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1  
    
    probabilities = {sum_: count / num_rolls for sum_, count in sum_counts.items()}
    return sum_counts, probabilities

theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

num_rolls = 1000000  
sum_counts, simulated_probabilities = simulate_rolls(num_rolls)

print("Результати симуляції:")
for sum_, count in sum_counts.items():
    sim_prob = simulated_probabilities[sum_]
    theo_prob = theoretical_probabilities[sum_]
    print(f"Сума: {sum_}, Кількість випадків: {count}, Ймовірність (симуляція): {sim_prob:.4f}, "
          f"Ймовірність (теоретична): {theo_prob:.4f}")

sums = list(theoretical_probabilities.keys())
sim_probs = [simulated_probabilities[sum_] for sum_ in sums]
theo_probs = [theoretical_probabilities[sum_] for sum_ in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, sim_probs, alpha=0.6, color='skyblue', label='Симуляція (Монте-Карло)')
plt.plot(sums, theo_probs, marker='o', color='red', linestyle='-', label='Теоретичні значення')
plt.xlabel('Сума значень на двох кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірність кожної суми при киданні двох кубиків')
plt.legend()
plt.show()
