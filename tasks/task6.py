def greedy_algorithm(items, budget):
    items_list = [(name, item['calories'], item['cost']) for name, item in items.items()]
    
    items_list.sort(key=lambda x: x[1] / x[2], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item in items_list:
        if budget - item[2] >= 0:
            chosen_items.append(item[0])
            total_calories += item[1]
            budget -= item[2]
    
    return chosen_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    items_list = list(items.items())

    for i in range(1, len(items_list) + 1):
        item_name, item_info = items_list[i-1]
        calories = item_info['calories']
        cost = item_info['cost']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    w = budget
    chosen_items = []
    for i in range(len(items_list), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name, item_info = items_list[i-1]
            chosen_items.append(item_name)
            w -= item_info['cost']
    
    return chosen_items[::-1], dp[-1][budget]


# Приклад
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print(f"\nЖадібний алгоритм: Продукти {greedy_result[0]} => {greedy_result[1]} каллорій при вартості {budget}")
print(f"Алгоритм динамічного програмування: Продукти {dp_result[0]} => {dp_result[1]} каллорій при вартості {budget}\n")