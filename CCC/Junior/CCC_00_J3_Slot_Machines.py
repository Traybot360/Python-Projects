coins = int(input())
current = [int(input()) for _ in range(3)]
pays = [30, 60, 9]
played = [35, 100, 10]

rounds = 0
machine = 0

while coins >= 1:  
    
    coins -= 1
    rounds += 1
    current[machine] += 1
    
    if played[machine] == current[machine]:
        coins += pays[machine]
        current[machine] = 0
    
    if coins == 0:
        break
    
    machine += 1
    machine = machine % 3   
        
print("Martha plays ? times before going broke.".replace("?",str(rounds)))
