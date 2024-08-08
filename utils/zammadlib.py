import requests

from config import ZAMMAD_API_KEY, ZAMMAD_URL


async def submit_to_zammad(zammad_user_info: dict) -> None:
    headers = {
        'Authorization': f'Bearer {ZAMMAD_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'title': 'Question from' + zammad_user_info['inn'],
        'group': 'Техническая поддержка',
        'article': {
            'subject': 'Support request',
            'body': zammad_user_info['question'],
            'type': 'note',
            'internal': False
        },
        'customer': {
            'firstname': zammad_user_info['full_name'],
            'email': zammad_user_info['email'],
            'phone': zammad_user_info['phone_number']
        },
        'note': 'forwarded by bot'
    }
    response = requests.post(ZAMMAD_URL + '/api/v1/tickets', headers=headers, json=payload)
    if response.status_code != 201:
        raise Exception(f"Failed to submit to Zammad: {response.text}")