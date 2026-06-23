import random
import time

WIDTH = 20
player = WIDTH // 2
score = 0

print("Pixel Dodge")
print("Move with A/D, avoid the falling block. Press Ctrl+C to quit.\n")

try:
    while True:
        block = random.randint(0, WIDTH - 1)

        line = ""
        for i in range(WIDTH):
            if i == player:
                line += "P"
            elif i == block:
                line += "X"
            else:
                line += "."

        print(line)

        if block == player:
            print(f"\nGame over! Score: {score}")
            break

        move = input("Move [a/d/enter]: ").lower()

        if move == "a" and player > 0:
            player -= 1
        elif move == "d" and player < WIDTH - 1:
            player += 1

        score += 1
        time.sleep(0.1)

except KeyboardInterrupt:
    print(f"\nStopped. Score: {score}")
