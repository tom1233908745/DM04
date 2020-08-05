import random
def main():

    heads = 0
    tails = 0

    print("Tossing a coin...");

    for i in range(3):
        num = random.random()
        print(num)
        if num*10 >= 5:
            print("Round " + str(i + 1) + ": Head")
            heads += 1
        else:

            print("Round " + str(i + 1) + ": Tail")
            tails += 1

    print("Heads: " + str(heads) + " Tails:" + str(tails))

    return

if __name__ == "__main__":
    main()
