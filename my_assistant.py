# my_assistant.py
# Author: Marie Lessman

HANDOFF_WORDS = ["refund", "complaint", "allergy", "allergic", "custom cake"]
ASK_WORDS = ["what", "when", "where", "how", "do you", "tell me", "is there"]


class FaqAssistant:
    """A mock bakery assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, faq_book):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.faq_book = faq_book
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that one. I'm passing you to a team member."
        for word in ASK_WORDS:
            if word in text:
                return self.faq_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me about hours, parking, wifi, or delivery."
        return "I'm not sure how to help with that. I can answer questions about hours, parking, wifi, or delivery."

    def needs_human(self, text):
        """Return True if the message needs a real person."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def faq_reply(self, user_message):
        """Use the FAQ book to answer a question about a topic."""
        topic = self.faq_book.find_topic(user_message)
        if topic is None:
            return "Which topic? I can check hours, parking, wifi, or delivery."
        answer = self.faq_book.answer_for(topic)
        return f"About {topic}: {answer}"