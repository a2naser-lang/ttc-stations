def increment(fred):
    return fred + 1

def main():
    fred = 5
    bob = 10
    bob = increment(bob)   
    print("fred =",fred,"bob =",bob)

if __name__ == '__main__':
    main()