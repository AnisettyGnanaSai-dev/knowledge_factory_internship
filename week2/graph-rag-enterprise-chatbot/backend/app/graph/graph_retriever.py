import logging

from app.database.neo4j_client import (
    run_query
)

from app.graph.cypher_queries import (
    ADMIN_QUERY,
    DEVELOPER_QUERY,
    INTERN_QUERY,
    CLIENT_QUERY
)

from app.graph.access_filter import (
    determine_sensitivity
)

logger = logging.getLogger(__name__)


def retrieve_context_for_role(
    question: str,
    user_role: str
):

    logger.info(
        f"GRAPH QUERY | role={user_role} | question={question}"
    )

    role = user_role.lower()

    if role == "admin":
        query = ADMIN_QUERY

    elif role == "developer":
        query = DEVELOPER_QUERY

    elif role == "intern":
        query = INTERN_QUERY

    elif role == "client":
        query = CLIENT_QUERY

    else:

        logger.warning(
            f"Unknown role: {user_role}"
        )

        return {
            "context_text": "",
            "nodes": [],
            "sensitivity_level": "public"
        }

    results = run_query(query)

    context_chunks = []

    for row in results:

        title = row.get(
            "title",
            ""
        )

        content = row.get(
            "content",
            ""
        )

        context_chunks.append(
            f"{title}\n{content}"
        )

    sensitivity = determine_sensitivity(
        results
    )

    return {
        "context_text": "\n\n".join(
            context_chunks
        ),
        "nodes": results,
        "sensitivity_level": sensitivity
    }