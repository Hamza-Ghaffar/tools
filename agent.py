# ================================================================
# AGENT - Core conversation logic
# NOTICE: No tool details here at all
# Only imports from tools package
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

    answer_from_model = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        functions=ALL_SCHEMAS,  # ← Pass all tool schemas to the model
        function_call="auto"   # ← Let model decide when to call tools
    )

    # 2. Check if model wants to call a tool
    llm_message=answer_from_model.choices[0].message

    if llm_message.tool_calls:
        messages.append(llm_message)

        for tool_call in llm_message.tool_calls:
            
            result = execute_tool(               # ← From registry
                tool_call.function.name,
                json.loads(tool_call.function.arguments)
            )
            
            messages.append({
                "role":         "tool",
                "tool_call_id": tool_call.id,
                "content":      result
            })
        # 3. Final answer after tool calls 
        final = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            tools=ALL_SCHEMAS
        )
        answer = final.choices[0].message.content
    
    else:
        answer = llm_message.content
    
    print(f"\n✅ FINAL: {answer}")
    return answer
    













