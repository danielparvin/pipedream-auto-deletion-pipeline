def handler(pd: "pipedream"):
    if "$return_value" not in pd.steps["get_users_to_delete"]:
        return 'There are no users to delete!'
    users_to_delete = pd.steps["get_users_to_delete"]["$return_value"]
    formatted_list = 'user_id,permission_id,first_name,last_name,email_address,created_on\n'
    for user in users_to_delete:
        row = user["user_id"]
        row += ','
        row += user["permission_id"]
        row += ','
        row += user["first_name"]
        row += ','
        row += user["last_name"]
        row += ','
        row += user["email_address"]
        row += ','
        row += user["created_on"]
        row += '\n'
        formatted_list += row
    return formatted_list
