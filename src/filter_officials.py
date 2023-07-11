def handler(pd: "pipedream"):
    all_users = pd.steps["get_all_users"]["$return_value"]
    return list(filter(officials_filter, all_users))

def officials_filter(user):
    """ Filter for users with a user_type of 'Official.'"""
    return user["user_type"] == 'Official'
