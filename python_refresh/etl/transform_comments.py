def transform_comment(comment):
    return (
        comment["postId"],
        comment["id"],
        comment["name"],
        comment["email"],
        comment["body"]
    )