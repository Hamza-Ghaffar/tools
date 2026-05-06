# ── TOOL REGISTRY ───────────────────────────────────────────────
# This file is the "registry" of all tools available to the LLM.
# Each tool is imported and added to the TOOLS list.

from tools import database_tool
from tools import weather_tool


# 2. Extract schemas automatically
# 3. Route tool calls to correct function

# 4. Adding new tool = just import here + done

TOOL_REGISTRY = {
    "get_weather":    weather_tool.get_weather,
    "get_stock_price": stock_tool.get_stock_price,
    "query_database": database_tool.query_database,

    # New tool? Add one line:
    # "send_email":   email_tool.send_email,
}

ALL_SCHEMAS = [
    weather_tool.SCHEMA,
    stock_tool.SCHEMA,
    database_tool.SCHEMA,
    # New tool? Add one line:
    # email_tool.SCHEMA,
]

# ── DISPATCHER FUNCTION ──────────────────────────────────────────
def execute_tool(tool_name: str, tool_arguments: dict) -> str:
    """
    Executes a tool by name with given arguments.
    """
    print(f"\n🔧 TOOL CALLED:  {tool_name}")
    print(f"📥 ARGUMENTS:    {tool_arguments}")

    # Check tool exists in registry
    if tool_name not in TOOL_REGISTRY:
        error = {"error": f"Tool '{tool_name}' not found in registry"}
        print(f"❌ ERROR:        {error}")
        return json.dumps(error)

    # Get function from registry

    tool_function = TOOL_REGISTRY[tool_name]
    result = tool_function(**tool_arguments)
    return json.dumps(result)

# ── HELPER: Show what tools are loaded ───────────────────────────
def list_registered_tools() -> None:
    print("\n📋 REGISTERED TOOLS:")
    for i, name in enumerate(TOOL_REGISTRY.keys(), 1):
        print(f"   {i}. {name}")
    print(f"   Total: {len(TOOL_REGISTRY)} tools loaded\n")

