from my_assistant import FaqAssistant
from my_tool import FaqBook


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    book = FaqBook({"hours": "7 am to 3 pm", "wifi": "free wifi"})
    return FaqAssistant("Pip", "Be friendly.", book)


def test_hours_question_uses_the_tool():
    helper = make_assistant()
    assert "7 am to 3 pm" in helper.respond("What are your hours?")


def test_question_without_a_known_topic_asks_for_one():
    helper = make_assistant()
    assert "Which topic?" in helper.respond("Tell me about your cakes")


def test_unknown_request_gets_safe_fallback():
    helper = make_assistant()
    assert "not sure how to help" in helper.respond("I love your logo")


def test_refund_is_passed_to_a_person():
    helper = make_assistant()
    assert "team member" in helper.respond("I want a refund")


def test_history_records_both_sides():
    helper = make_assistant()
    helper.respond("hello")
    assert len(helper.history) == 2
    assert helper.history[0]["role"] == "user"
    assert helper.history[1]["role"] == "assistant"