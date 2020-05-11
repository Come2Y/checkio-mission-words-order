"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['hi world im here', ['world', 'here']],
            "answer": True,
        },
        {
            "input": ['hi world im here', ['here', 'world']],
            "answer": False,
        },
        {
            "input": ['hi world im here', ['world']],
            "answer": True,
        },
        {
            "input": ['hi world im here', ['world', 'here', 'hi']],
            "answer": False,
        },
        {
            "input": ['hi world im here', ['world', 'im', 'here']],
            "answer": True,
        },
        {
            "input": ['hi world im here', ['world', 'hi', 'here']],
            "answer": False,
        },
        {
            "input": ['hi world im here', ['world', 'world']],
            "answer": False,
        },
        {
            "input": ['hi world im here', ['country', 'world']],
            "answer": False,
        },
        {
            "input": ['hi world im here', ['wo', 'rld']],
            "answer": False,
        },
        {
            "input": ['', ['world', 'here']],
            "answer": False,
        },
        {
            "input": ['hi world world im here', ['world', 'world']],
            "answer": False,
        },
    ],
    "Extra": [
        {
            "input": ['london in the capital of great britain', ['London', ]],
            "answer": False,
        },
        {
            "input": ['london in the capital of great britain', ['london', ]],
            "answer": True,
        },
        {
            "input": ['london in the capital of great britain', ['london', 'great']],
            "answer": True,
        },
        {
            "input": ['london in the capital of great britain', ['london', 'of', 'great']],
            "answer": True,
        },
        {
            "input": ['london in the capital of great britain', ['britain', 'great']],
            "answer": False,
        },
    ]
}
