from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # ==========================
    # Supabase
    # ==========================
    SUPABASE_URL: str
    SUPABASE_SERVICE_ROLE_KEY: str

    # ==========================
    # JWT
    # ==========================
    JWT_SECRET: str
    JWT_ALGORITHM: str

    # ==========================
    # Neo4j
    # ==========================
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str
    NEO4J_DATABASE: str

    # ==========================
    # Aura
    # ==========================
    AURA_INSTANCEID: str
    AURA_INSTANCENAME: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()