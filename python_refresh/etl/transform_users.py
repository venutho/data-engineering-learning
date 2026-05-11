def transform_user(user):
    return (
        user["id"],
        user["name"],
        user["email"],
        user["address"]["city"],
        user["company"]["name"]
    )