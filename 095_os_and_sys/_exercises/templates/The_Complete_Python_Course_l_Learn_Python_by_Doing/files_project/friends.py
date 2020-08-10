# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = o..('people.txt', 'r')
people_nearby = [line.strip() ___ line __ people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = o..('nearby_friends.txt', 'w')

___ friend __ friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
