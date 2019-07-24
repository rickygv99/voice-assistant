import wolframalpha

WOLFRAM_ALPHA_APP_ID = "" # Put Wolfram Alpha App ID here

fallback_response = "Sorry, I don't understand."

greetings = ["hello", "hi", "howdy", "hey", "hola", "sup", "aloha"]
farewells = ["bye", "goodbye", "adios"]

client = wolframalpha.Client(WOLFRAM_ALPHA_APP_ID)

def execute(input):
    tokens = input.split()
    for token in tokens:
        if token in greetings:
            return "Hello!"
        if token in farewells:
            return "Bye!"

    # Query WolframAlpha
    response = client.query(input)
    if response['@success'] == 'false':
        return fallback_response
    else:
        pod_answer = response['pod'][1]['subpod']
        if isinstance(pod_answer, list):
            return pod_answer[0]['plaintext']
        else:
            return pod_answer['plaintext']
