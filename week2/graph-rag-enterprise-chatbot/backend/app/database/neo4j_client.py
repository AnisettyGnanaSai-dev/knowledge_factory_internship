from neo4j import GraphDatabase
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class Neo4jClient:
    def __init__(self):
        self.driver = None

        try:
            self.driver = GraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(
                    settings.NEO4J_USERNAME,
                    settings.NEO4J_PASSWORD
                )
            )

            logger.info(
                "Neo4j connection established"
            )

        except Exception as e:
            logger.error(
                f"Neo4j connection failed: {e}"
            )

    def close(self):
        if self.driver:
            self.driver.close()

    def run_query(
        self,
        query: str,
        params: dict = None
    ):
        try:
            with self.driver.session() as session:

                result = session.run(
                    query,
                    params or {}
                )

                return [
                    record.data()
                    for record in result
                ]

        except Exception as e:

            logger.error(
                f"Neo4j query error: {e}"
            )

            return []


neo4j_client = Neo4jClient()


def get_driver():
    return neo4j_client.driver


def close_driver():
    neo4j_client.close()


def run_query(
    cypher: str,
    params: dict = None
):
    return neo4j_client.run_query(
        cypher,
        params
    )