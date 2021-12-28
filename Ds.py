from test_file import tests


def locate_cards(cards, query):
    lo, hi = 0, len(cards)

    while lo <= hi:
        mid = (lo+hi) // 2
        mid_card = cards[mid]

        print("lo:", lo, "hi:", hi, "mid:", mid, "mid_card:", mid_card)

        if mid_card == query:
            return mid
        elif mid_card < query:
            hi = mid - 1
        elif mid_card > query:
            lo = mid + 1

    return -1


lst = []
n = int(input("Enter number of elements:"))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

my_query = int(input("Enter one number from the cards you want to find: "))

my_output = lst.index(my_query)

main_query = ({
    'input': {
        'cards': lst,
        'query': my_query
    },
    'output': my_output
})

if locate_cards(**main_query['input']) == main_query['output']:
    print(main_query['input'])
    print(main_query['output'])
    print('Passed')
elif locate_cards(**main_query['input']) != main_query['output']:
    print(main_query['input'])
    print(main_query['output'])
    print('Failed')

#
# for test in tests:
#     if locate_cards(**test['input']) == test['output']:
#         print(test['input'])
#         print(test['output'])
#         print("Passed")
#     else:
#         print(test['input'])
#         print(test['output'])
#         print("Failed")
