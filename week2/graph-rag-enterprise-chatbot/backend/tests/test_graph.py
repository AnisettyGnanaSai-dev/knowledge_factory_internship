from app.database.neo4j_client import run_query


def test_neo4j_connection():

    result = run_query("""
    MATCH (n)
    RETURN labels(n) AS labels
    LIMIT 5
    """)

    print(result)

    assert len(result) > 0