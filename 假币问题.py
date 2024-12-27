def check_assumption(weighings, counterfeit, is_heavy):
    for left, right, result in weighings:
        left_set = set(left)
        right_set = set(right)
        if counterfeit in left_set and counterfeit not in right_set:
            expected_result = 'up' if is_heavy else 'down'
        elif counterfeit not in left_set and counterfeit in right_set:
            expected_result = 'down' if is_heavy else 'up'
        else:
            expected_result = 'even'
        if expected_result != result:
            return False
    return True
def find_counterfeit(weighings):
    all_coins = set('ABCDEFGHIJKL')
    for coin in all_coins:
        if check_assumption(weighings, coin, False):
            return coin, 'light'
        if check_assumption(weighings, coin, True):
            return coin, 'heavy'
n = int(input())
for _ in range(n):
    weighings = []
    for _ in range(3):
        weighings.append(input().split())
    coin, state = find_counterfeit(weighings)
    print(f'{coin} is the counterfeit coin and it is {state}.')