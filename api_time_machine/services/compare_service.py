class CompareService:

    @staticmethod
    def compare_json(old_response, new_response):

        differences = {}

        old_keys = set(old_response.keys())
        new_keys = set(new_response.keys())

        added = list(new_keys - old_keys)
        removed = list(old_keys - new_keys)

        changed = []

        for key in old_keys.intersection(new_keys):

            if old_response[key] != new_response[key]:

                changed.append({
                    "field": key,
                    "old": old_response[key],
                    "new": new_response[key]
                })

        differences["added_fields"] = added
        differences["removed_fields"] = removed
        differences["changed_fields"] = changed

        return differences