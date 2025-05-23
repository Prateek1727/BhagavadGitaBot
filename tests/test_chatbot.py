import pytest
from src.chatbot import gita_chatbot

def test_gita_chatbot_returns_string(mocker):
    """
    Test that gita_chatbot returns a string response.
    """
    user_query = "What is the central message of the Bhagavad Gita?"

    # Mock the external dependencies
    mock_search_db = mocker.patch('src.chatbot.search_db')
    mock_gitabot_ai = mocker.patch('src.chatbot.gitabot_ai')

    # Define return values for the mocks
    mock_search_db.return_value = [
        "The central message of the Bhagavad Gita is to perform one's duty without attachment to the results.",
        "Krishna teaches Arjuna about selfless action, devotion, and the imperishable nature of the soul.",
        "The Gita emphasizes the importance of righteousness (dharma) and devotion (bhakti)."
    ]
    mock_gitabot_ai.return_value = (
        "The central message of the Bhagavad Gita is to perform your duty selflessly, "
        "with devotion and without attachment to the outcomes, as taught by Krishna to Arjuna."
    )

    # Call the function
    response = gita_chatbot(user_query)

    # Assertions
    mock_search_db.assert_called_once_with(user_query=user_query)
    mock_gitabot_ai.assert_called_once_with(user_query=user_query, doc_list=[
        "The central message of the Bhagavad Gita is to perform one's duty without attachment to the results.",
        "Krishna teaches Arjuna about selfless action, devotion, and the imperishable nature of the soul.",
        "The Gita emphasizes the importance of righteousness (dharma) and devotion (bhakti)."
    ])
    assert isinstance(response, str)
    assert response == (
        "The central message of the Bhagavad Gita is to perform your duty selflessly, "
        "with devotion and without attachment to the outcomes, as taught by Krishna to Arjuna."
    )

def test_gita_chatbot_empty_query(mocker):
    """
    Test gita_chatbot behavior with an empty query.
    """
    user_query = ""

    mock_search_db = mocker.patch('src.chatbot.search_db')
    mock_gitabot_ai = mocker.patch('src.chatbot.gitabot_ai')

    mock_search_db.return_value = []
    mock_gitabot_ai.return_value = "Please provide a valid query."

    response = gita_chatbot(user_query)

    mock_search_db.assert_called_once_with(user_query=user_query)
    mock_gitabot_ai.assert_called_once_with(user_query=user_query, doc_list=[])
    assert response == "Please provide a valid query."

# Add more test functions as needed