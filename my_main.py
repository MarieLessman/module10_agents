# my_main.py
# Author: Marie Lessman

from my_assistant import FaqAssistant
from my_tool import FaqBook

ANSWERS = {
    "hours": "We're open 7 am to 3 pm, Tuesday through Sunday.",
    "parking": "There's free street parking on Palm Street and a small lot behind the shop.",
    "wifi": "Yes, it's free. The password is on the chalkboard by the register.",
    "delivery": "We deliver within 5 miles for orders over $25.",
}

faq_book = FaqBook(ANSWERS)
helper = FaqAssistant(
    "Pip",
    "You help customers of Palm Street Bakery with common questions.",
    faq_book,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")