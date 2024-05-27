def get(user):
    qa={
        "hello": "Hello! How can I help you today?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm a chatbot, so I'm always good. How can I assist you?",
        "what is your name": "I'm a simple chatbot created to assist you.",
        "what can you do": "I can chat with you and answer your questions!",
        "what is the meaning of life": "The meaning of life is a philosophical question, but some say it's 42!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the weather like": "I don't have access to real-time data, but you can check your local weather forecast online.",
        "how old are you": "I'm as old as the code that created me, which is quite young!",
        "who created you": "I was created by a developer using Python!",
        "what is python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "can you help me": "Of course! Ask me anything, and I'll do my best to assist you.",
        "what is your purpose": "My purpose is to assist and entertain you with responses to your questions.",
        "do you like music": "I'm a chatbot, so I don't have preferences, but I know music is loved by many people!",
        "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"
    }
    if user=="math":
        return ""
    return qa.get(user.lower(), "I'm not sure how to respond to that. Can you ask something else?")

def calculate(user):
    l=['+','-','*','/','%']
    a,b,c=0,'+',0
    for i in range(len(user)):
        if user[i] in l:
            a=int(user[:i])
            b=int(user[i+1:])
            c=user[i]
            break
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        return round(a/b,2)
    elif c=='%':
        return a%b
    else:
        return "Invalid operation. Please enter a valid operation"   

print("Welcome to the simple chatbot! Type 'bye' to exit.")
print("For calculations type 'math'.")
while True:
    user=input("You: ")
    if user.lower()=="math":
        print("Chatbot: Enter an expression to calculate.")
        u=input("You: ").lower()
        r=calculate(u)
        print(f"Chatbot: {r}")
    elif user.lower()=="bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        r=get(user)
        print(f"Chatbot: {r}")