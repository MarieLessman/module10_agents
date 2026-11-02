# my_tool.py
# Author: Marie Lessman


class FaqBook:
    """A tool that knows answers to common bakery questions."""

    def __init__(self, answers):
        """Store the answers this tool can look up."""
        self.answers = answers

    def find_topic(self, text):
        """Return the first known topic mentioned in text, or None."""
        for topic in self.answers:
            if topic in text.lower():
                return topic
        return None

    def answer_for(self, topic):
        """Return the answer for one topic, or None if unknown."""
        if topic in self.answers:
            return self.answers[topic]
        return None