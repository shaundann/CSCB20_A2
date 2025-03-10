from flask import Flask

app = Flask(__name__)


def ifdigit(s) -> bool:
    for char in s:
        if char.isdigit():
            return True
    return False


def NodigitUpper(s) -> str:
    s2 = ''
    for char in s:
        if not char.isdigit():
            char = char.upper()
            s2 += char
    return s2


def name_format(name: str) -> str:
    if name.isupper():
        return name.lower()
    elif name.islower():
        return name.upper()
    elif ifdigit(name):
        name = NodigitUpper(name)
    else:
        return name.title()
    return name


VowelToEmoji = {
    'a': '🔺', 
    'e': '🎗', 
    'i': '👁', 
    'o': '🔵', 
    'u': '🆙'
}


def EmojiFormat(name: str) -> str:
    s = ''
    for char in name:
        if char.lower() in VowelToEmoji:
            char = VowelToEmoji[char.lower()]
        s += char
    return s


@app.route('/')
def home():
    return "Hello! Please type your name as /name so we can greet you!"

@app.route('/<name>')
def name_greeting(name) -> str:
    updated_name = name_format(name)
    if updated_name[::-1].lower() == updated_name.lower():
        return "Welcome, " + name.strip() + ". Your name is a palindrome!"
    return "Welcome, " + updated_name + ", to my CSCB20 website!"


@app.route('/emoji/<name>')
def emoji_greeting(name) -> str:
    processed_name = EmojiFormat(name)
    return "Welcome, " + processed_name + ", to my CSCB20 website!"


if __name__ == '__main__':
    app.run(debug=False)


