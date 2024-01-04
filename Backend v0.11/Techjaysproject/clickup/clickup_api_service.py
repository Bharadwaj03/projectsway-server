import requests
from clickupython import client
from django.http import JsonResponse

# If change is required 'https://api.clickup.com/api/v2/team/{team_id}/project'

API_KEY = 'pk_88837892_ET6IHZF34HQH9BBJLVJKJMF8UN87J47B'

CLICKUP_API_KEY = 'YOUR_CLICKUP_API_KEY'  # Replace with your ClickUp API key

def get_clickup_projects():
    url = 'https://api.clickup.com/api/v2/team/{team_id}/project'
    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            projects = response.json().get('projects', [])
            return projects
        except ValueError:
            return []
    else:
        return []  # Handle error cases accordingly
