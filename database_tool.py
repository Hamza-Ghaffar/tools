# ================================================================
# DATABASE TOOL
# ================================================================

SCHEMA = {
    "type": "function",
    "function": {
        "name": "query_database",
        "description": "Query the database for information. Use when user asks about data, records, or anything that requires fetching information from the database.",
        
        # In a real implementation, you would have more specific parameters based on your database schema   
        "parameters": {"type": "string",
                    "enum": ["user_info", "order_history", "account_balance"],
                    "description": "Type of data to retrieve"
                },
                 "user_id": {
                    "type": "integer",
                    "description": "User ID number"
                }
            },
            "required": ["query_type", "user_id"]
        }
    

def query_database(query_type: str, user_id: int) -> dict:
    """
    Queries the database based on the query type and user ID.
    Production: replace mock with real database queries
    """
    
    mock_users = {
        101: {"name": "James Wilson",  "plan": "Premium", "country": "UK"},
        102: {"name": "Anna Schmidt",  "plan": "Basic",   "country": "Germany"},
        103: {"name": "John Martinez", "plan": "Premium", "country": "USA"},
    }
    
    mock_orders = {
        101: [{"order_id": "ORD001", "item": "Laptop",  "status": "Delivered"},
              {"order_id": "ORD002", "item": "Monitor", "status": "Shipped"}],
        102: [{"order_id": "ORD003", "item": "Keyboard","status": "Processing"}],
    }
    
    if query_type == "user_info":
        return mock_users.get(user_id, {"error": "User not found"})
    
    elif query_type == "order_history":
        return {"orders": mock_orders.get(user_id, [])}
    
    return {"error": f"Unknown query_type: {query_type}"}
    
