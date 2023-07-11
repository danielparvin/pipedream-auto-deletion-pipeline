def handler(pd: "pipedream"):
    officials = pd.steps["filter_officials"]["$return_value"]
    return list(filter(empty_postal_code_filter, officials))

def empty_postal_code_filter(user):
    """ Filter for users with an empty postal_code field."""
    return user["postal_code"] == ''
    