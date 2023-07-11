import datetime
from datetime import timezone

dateThreshold = datetime.datetime.now(timezone.utc) - datetime.timedelta(days = 10)

def handler(pd: "pipedream"):
    empty_postal_code_officials = pd.steps["filter_empty_postal_code_officials"]["$return_value"]
    created_on_dates_by_permission_id = pd.inputs["data_store"]
    users_to_delete = []
    for permission_id, date in created_on_dates_by_permission_id.items():
        if datetime.datetime.fromisoformat(date) < dateThreshold:
            user_to_delete = [i for i in empty_postal_code_officials if i["permission_id"] == permission_id]
            if len(user_to_delete) == 1:
                user_to_delete[0]["created_on"] = date
                users_to_delete += user_to_delete
    return users_to_delete
