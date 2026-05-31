def determine_sensitivity(
    nodes: list
) -> str:

    if not nodes:
        return "public"

    for node in nodes:

        sensitivity = node.get(
            "sensitivity",
            "public"
        )

        if sensitivity == "confidential":
            return "confidential"

    return "public"