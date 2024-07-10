import collections


def is_palindrome(s):
    string_lower_no_spaces = ''.join(char.lower() for char in s if char.isalnum())

    deq = collections.deque(string_lower_no_spaces)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True


test_strings = [
    "Able was I ere I saw Elba",
    "Madam, in Eden, I'm Adam",
    "Step on no pets",
    "Eva, can I see bees in a cave?",
    "Mr. Owl ate my metal worm",
    "Do geese see God?",
    "A Santa at NASA",
    "Never odd or even",
    "Doc, note I dissent. A fast never prevents a fatness. I diet on cod.",
    "Murder for a jar of red rum",
    "Go hang a salami, I'm a lasagna hog",
    "Yo, Banana Boy!",
    "A Toyota's a Toyota",
    "A Santa lived as a devil at NASA"
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for string in test_strings:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')
