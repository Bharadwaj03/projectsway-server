from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import pandas as pd
from mock_api.models import ClickUpData
from mock_api.serializers import ClickUpDataSerializer

class ClickUpSpacesView(APIView):
    def get(self, request):
        try:
            clickup_api = "pk_88837892_ET6IHZF34HQH9BBJLVJKJMF8UN87J47B"
            workspace_id = "9002025943"
            
            url = f"https://api.clickup.com/api/v2/team/{workspace_id}/space?archived=false"
            headers = {"Authorization": clickup_api}
            r = requests.get(url=url, headers=headers)
            response_dict = json.loads(r.text)
 
            spaces = response_dict["spaces"]
           
            clickup_spaces_list = []
            if spaces:
                for space in spaces:
                    tmp_dict = {}
                    space_id = space['id']
                    space_name = space['name']
                    # features = space['features']  # Commenting this out as it's not used in the response
                    tmp_dict["space_id"] = space_id
                    tmp_dict["space_name"] = space_name
           
                    clickup_spaces_list.append(tmp_dict)
 
            clickup_spaces = pd.DataFrame.from_records(clickup_spaces_list)
            
            return Response(clickup_spaces.to_dict(orient='records'), status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ClickUpDataListCreateView(generics.ListCreateAPIView):
    queryset = ClickUpData.objects.all()
    serializer_class = ClickUpDataSerializer