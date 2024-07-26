from aiogram import types

from email_validator import validate_email, EmailNotValidError

def validate_email_address(message: types.Message) -> dict[str, str]:
    try:
        email = validate_email(message.text)
    except EmailNotValidError:
        return None
    return {"email": email.normalized.lower()}