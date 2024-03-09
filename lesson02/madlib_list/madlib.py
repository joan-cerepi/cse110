def madlib_1() -> None:
    adjective = input('adjective: ').lower().strip()
    animal = input('animal: ').lower().strip()
    verb_1 = input('verb: ').lower().strip()
    exclamation = input('exclamation: ').capitalize().strip()
    verb_2 = input('verb: ').lower().strip()
    verb_3 = input('verb: ').lower().strip()

    print('Your story is: ')
    print()

    print('The other day, I was really in trouble. It all started when I saw')
    print(f'a very {adjective} {animal} {verb_1} down the hallway.')
    print(f'"{exclamation}!" I yelled. But all I could think to do was to')
    print(f'{verb_2} over and over. Miraculously, that caused it to stop,')
    print(f'but not before it tried to {verb_3} right in front of my family.')



def madlib_2() -> None:
    noun_1 = input('noun: ').lower().strip()
    adjective_1 = input('adjective: ').lower().strip()
    adjective_2 = input('adjective: ').lower().strip()
    verb_1 = input('verb (past tense): ').lower().strip()
    verb_2 = input('verb (present tense): ').lower().strip()
    noun_2 = input('noun: ').lower().strip()
    verb_3 = input('verb (past tense): ').lower().strip()
    verb_4 = input('verb (present tense): ').lower().strip()
    verb_5 = input('verb (past tense): ').lower().strip()

    print('Your story is: ')
    print()

    print(f'One day, a {noun_1} wanted to cross a bridge over a pond.')
    print(f'Under that bridge lived a {adjective_1} and {adjective_2} troll.')
    print(f'Stamp, stomp, stamp. He {verb_1} over the bridge.')
    print(f'"Who tramps over my bridge?" yelled the troll. "Stop or I will')
    print(f'{verb_2} you!" But he had already crossed the bridge.')
    print(f'On the next day, a sleepy {noun_2} wanted to cross the bridge.')
    print(f'Stamp, stomp, stamp. He {verb_3} over the bridge. "Who tramps')
    print(f'over my bridge?" yelled the troll. "Stop or I will {verb_4} you!')
    print(f'Oh, never mind. Nobody listens to me anyway!" And with that,')
    print(f'the troll {verb_5} away.')