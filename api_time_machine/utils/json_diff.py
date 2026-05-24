def find_json_difference(old_json, new_json):

    differences = {}

    for key in old_json:

        if key not in new_json:

            differences[key] = "Removed"

        elif old_json[key] != new_json[key]:

            differences[key] = {
                "old": old_json[key],
                "new": new_json[key]
            }

    for key in new_json:

        if key not in old_json:

            differences[key] = "Added"

    return differences