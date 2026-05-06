# ================================================================
# AGENT - Tool Chaining Logic
# KEY DIFFERENCE from single tool:
# while loop instead of if/else
# Keeps looping until LLM stops requesting tools
# ================================================================


import openai
import json
from tools import execute_tool, ALL_SCHEMAS , list_registered_tools    # ← Clean import
from config.settings import OPENAI_API_KEY, OPENAI_MODEL


#
def ask_with_tools(user_question: str) -> str:

    # 1. Create OpenAI client
    client  = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    messages = [{"role": "user", "content": user_question}]
    
    print(f"\n{'='*55}")
    print(f"👤 USER: {user_question}")
    print(f"{'='*55}")

    # track how many LLM calls
     turn_number = 0     

    while True:
        turn_number += 1
        print(f"\n── LLM TURN {turn_number} ──────────────────────")
        
        # ── CALL LLM ─────────────────────────────────────────
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            tools=ALL_SCHEMAS,
            tool_choice="auto"
        )
        
        llm_message   = response.choices[0].message
        finish_reason = response.choices[0].finish_reason
        
        print(f"🤖 FINISH REASON: {finish_reason}")
        # finish_reason tells you WHY LLM stopped:
        # "tool_calls" → LLM wants to call tool(s)
        # "stop"       → LLM finished with text answer
        
        # ── CHECK IF LLM IS DONE ─────────────────────────────
        if finish_reason == "stop":
            # LLM gave final text answer - chain complete
            final_answer = llm_message.content
            print(f"\n✅ CHAIN COMPLETE after {turn_number} turns")
            print(f"✅ FINAL: {final_answer}")
            return final_answer
        
        # ── LLM WANTS TOOLS - EXECUTE ALL OF THEM ────────────
        if finish_reason == "tool_calls":
            
            # Add LLM message to history
            messages.append(llm_message)
            
            print(f"🔗 TOOLS REQUESTED: {len(llm_message.tool_calls)}")
            
            # Loop through ALL tool calls in this turn
            # Could be 1 (sequential) or many (parallel)
            for i, tool_call in enumerate(llm_message.tool_calls):
                
                print(f"\n   Tool {i+1}/{len(llm_message.tool_calls)}:")
                
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                # Execute tool
                result = execute_tool(tool_name, tool_args)
                
                # Add each result to messages
                messages.append({
                    "role":         "tool",
                    "tool_call_id": tool_call.id,   # link to request
                    "content":      result
                })
            
            # ── LOOP CONTINUES ───────────────────────────────
            # Goes back to while True
            # Calls LLM again with all tool results
            # LLM decides: more tools needed? or final answer?





   














