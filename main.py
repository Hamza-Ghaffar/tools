# ================================================================
# MAIN - Entry point only
# ================================================================

from tools import list_registered_tools
from agent import ask_with_tools


if __name__ == "__main__":
    
    # Show loaded tools on startup
    list_registered_tools()
    
    # Run questions
    ask_with_tools("What is the weather in London?")
    ask_with_tools("Get stock price for AAPL")
    ask_with_tools("Show user info for user ID 101")
    ask_with_tools("What is 2 + 2?")           # No tool needed