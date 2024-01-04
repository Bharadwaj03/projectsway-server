#!/usr/local/bin/python3
#python3 code to get ClickUp Spaces in a Workspaces
#command to run the code -> python3 ./get_spaces.py
import sys
import json
import requests
import pandas as pd
 
 
def get_spaces(clickup_api, workspace_id):
    try:
        url = f"https://api.clickup.com/api/v2/team/{workspace_id}/space?archived=false"
        headers = {"Authorization": clickup_api}
        r = requests.get(url = url, headers = headers)
        response_dict = json.loads(r.text)
 
        spaces = response_dict["spaces"]
       
        clickup_spaces = pd.DataFrame()
        clickup_spaces_list = []
        if spaces:
            for space in spaces:
                tmp_dict = {}
                space_id = space['id']
                space_name = space['name']
                features = space['features']
                #print("\nspace name : %s | Space id : %s "% (space_name, space_id))
                tmp_dict["space_id"] = space_id
                tmp_dict["space_name"] = space_name
       
                clickup_spaces_list.append(tmp_dict)
 
        clickup_spaces = pd.DataFrame.from_records(clickup_spaces_list)
 
        return clickup_spaces
    except:
        print("\n get_spaces Failed : ",sys.exc_info())
 
 
 
if __name__ == '__main__':
    try:
        print("\n ClickUp get spaces process starts")
 
        clickup_api = "Replace with ClickUp API key"
        workspace_id = "Replace with workspace Id eg: 10xxxx73"
 
        spaces_df = get_spaces(clickup_api, workspace_id)
        print(spaces_df)
 
        print("\n ClickUp get spaces process Finished.")
    except:
        print("\n ClickUp get spaces process Failed : ", sys.exc_info())