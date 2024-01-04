from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests
import json

from clickupython import client
from django.http import JsonResponse

API_KEY = 'pk_88837892_ET6IHZF34HQH9BBJLVJKJMF8UN87J47B'
cl = client.ClickUpClient(API_KEY)


def get_task(request, task_id):
    c = client.ClickUpClient(API_KEY)
    task = client.get_task(c, task_id)

    response = requests.get(task)
    data_single = response.json()
    return JsonResponse(data_single)


def get_task_from_list(request, task_id,list_id):
    c = client.ClickUpClient(API_KEY)
    list = c.get_list(list_id)
    tasks = list.get_tasks(c)
    filtered_tasks = list.get_tasks(c, subtasks=True, statuses=["todo", "in progress"])
    task = list.get_task(c, task_id)


    response = requests.get(filtered_tasks)
    data = response.json()
    return JsonResponse(data)


def get_list(request, list_id):
    c = client.ClickUpClient(API_KEY)
    tasks = c.get_tasks(list_id)
    response = requests.get(tasks)
    data_list = response.json()
    return JsonResponse(data_list)


def get_filtered_list(request, task_id, list_id):
    c = client.ClickUpClient(API_KEY)
    list = c.get_list(list_id)
    tasks = list.get_tasks(c)
    filtered_tasks = list.get_tasks(c, subtasks=True, statuses=["todo", "in progress"])
    task = list.get_task(c, task_id)
    response = requests.get(filtered_tasks)
    data = response.json()
    return JsonResponse(data)


from .clickup_api_service import get_clickup_projects

class ClickUpProjectsAPIView(APIView):
    def get(self, request):
        projects = get_clickup_projects()
        if projects:
            return Response(projects)
        else:
            return Response({"error": "Failed to fetch projects from ClickUp"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
