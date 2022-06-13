def readInt(msg: str) -> int:
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = int(number)
            break
        except ValueError:
            print('Input must be a int!')

    return int(number)
