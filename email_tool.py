# ================================================================
# EMAIL TOOL - needed for chaining example
# ================================================================

SCHEMA = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Send email summary to user. Use after collecting data.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "Email address"
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject line"
                },
                "body": {
                    "type": "string",
                    "description": "Email body content"
                }
            },
            "required": ["to", "subject", "body"]
        }
    }
}


def send_email(to: str, subject: str, body: str) -> dict:
    # Real: use smtplib, SendGrid, AWS SES
    print(f"\n📧 SENDING EMAIL:")
    print(f"   TO:      {to}")
    print(f"   SUBJECT: {subject}")
    print(f"   BODY:    {body[:50]}...")
    
    return {
        "status":    "sent",
        "to":        to,
        "subject":   subject,
        "timestamp": "2024-01-14T10:30:00Z"
    }