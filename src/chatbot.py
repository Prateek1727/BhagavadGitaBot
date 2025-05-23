import os
from .ai_function import gitabot_ai
from .database import search_db
from loguru import logger

def gita_chatbot(user_query: str) -> str:
    logger.info("Searching for similar docs in the Bhagavad Gita vector DB")
    doc_list = search_db(user_query=user_query)
    logger.info("Calling the gitabot_ai to get answer")
    answer = gitabot_ai(user_query=user_query, doc_list=doc_list)
    logger.info("Returning the final answer")
    return answer

# if __name__ == "__main__":
#     question = "What is the central message of the Bhagavad Gita?"
#     answer = gita_chatbot(user_query=question)
#     print(answer)