from datetime import timezone
import datetime

def handler(pd: "pipedream"):
    empty_postal_code_officials = pd.steps["filter_empty_postal_code_officials"]["$return_value"]
    permission_ids = [i['permission_id'] for i in empty_postal_code_officials]
    created_on_by_permission_id = pd.inputs["data_store"]

    # Remove extraneous entries from the data store.
    data_store_keys = created_on_by_permission_id.keys()
    for stored_id in data_store_keys:
        if stored_id not in permission_ids:
            del created_on_by_permission_id[stored_id]

    # Add new entries to data store.
    for official in empty_postal_code_officials:
        if official["permission_id"] not in created_on_by_permission_id:
            created_on_by_permission_id[official["permission_id"]] = datetime.datetime.now(timezone.utc).isoformat()
