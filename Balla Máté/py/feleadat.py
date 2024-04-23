import random

def generate_random_list():
    tarolo = [[random.randint(0, 25) for _ in range(3)] for _ in range(4)]
    return tarolo

generate_random_list()

