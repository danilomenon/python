import time

print('Hello World')

cont = 1

while cont <= 15:
    print(f'\rtempo {cont}', end="")
    #print(cont)
    cont += 1
    time.sleep(1)