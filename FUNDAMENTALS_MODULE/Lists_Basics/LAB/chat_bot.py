# Useless

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],[
        r"(.*) your name ?",
        ["My name is chat_bot.",]
    ],[
        r"quit",
        ["Bye", "F off",]
    ],
]

chat = Chat(pairs, reflections)
chat.converse()
