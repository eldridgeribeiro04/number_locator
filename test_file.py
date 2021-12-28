tests = []


test = ({
    'input': {
        'cards': [13, 11, 10, 0, 4, 3, 1, 7],
        'query': 7
    },
    'output': 7
})

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, -4, 0, 1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [6, 8, 5, 21],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [6, 6, 7, 7, 7, 7, 7, 3, 8, 8, 5, 21, 29],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [6, 6, 7, 7, 7, 7, 7, 3, 4, 4, 4, 4, 4, 4, 8, 8, 5, 21, 29],
        'query': 4
    },
    'output': 8
})
