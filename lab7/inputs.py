def read_query():
    print("Pass query inputs. Names separated by by commas: ")
    while True:
        try:
            query = input()
            query = query.split(",")
            break
        except ValueError:
            print("Names must be separated by commas!")
    query = [q.strip() for q in query]
    return query


def read_evidence():
    evidence = {}

    while True:
        try:
            print("Pass the name of the node, or leave empty to stop writing evidence:")
            name = input()
            if len(name) == 0:
                return evidence

        except ValueError:
            print("Input must be a string!")
        while True:
            number = read_scalar("Pass 1 for True, 0 for False: ")
            if number == 0:
                evidence[name] = False
                break
            elif number == 1:
                evidence[name] = True
                break
            else:
                print("Incorrect number passed!")


def read_scalar(message):
    while True:
        try:
            number = input(message)
            number = int(number)
            break
        except ValueError:
            print('Input must be a number!')
    return number


def read_params():
    print("STEP 1: Enter the evidence:")
    evidence = read_evidence()

    print("STEP 2: Enter the query:")
    query = read_query()

    print("STEP 3: Enter the number of steps:")
    nr_steps = read_scalar('')

    return evidence, query, nr_steps
