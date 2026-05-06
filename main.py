# ================================================================
# MAIN - Test all chaining scenarios
# ================================================================

from tools import list_registered_tools
from agent import ask_with_tools


if __name__ == "__main__":
    
    list_registered_tools()
    
    print("\n" + "█"*55)
    print("SCENARIO 1: PARALLEL CHAIN")
    print("█"*55)
    ask_with_tools(
        "Get weather in London AND stock price for LLOY "
        "at the same time"
    )
    # LLM calls: get_weather + get_stock_price TOGETHER
    # Total turns: 2
    
    
    print("\n" + "█"*55)
    print("SCENARIO 2: SEQUENTIAL CHAIN")
    print("█"*55)
    ask_with_tools(
        "Look up user ID 101 and then check weather "
        "in their country"
    )
    # LLM calls: query_database THEN get_weather
    # Total turns: 3
    
    
    print("\n" + "█"*55)
    print("SCENARIO 3: LONG CHAIN")
    print("█"*55)
    ask_with_tools(
        "Get user 101 info, check weather in their city, "
        "check LLOY stock, then email summary to james@test.com"
    )
    # LLM calls: query_database → get_weather 
    #            → get_stock_price → send_email
    # Total turns: 4 or 5
    
    
    print("\n" + "█"*55)
    print("SCENARIO 4: NO TOOL NEEDED")
    print("█"*55)
    ask_with_tools("What is 10 multiplied by 5?")
    # LLM answers directly
    # Total turns: 1