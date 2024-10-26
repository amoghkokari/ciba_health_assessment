import os
from app.core.config import config
from app.core.logger import setup_logger
import asyncio

# Set up logger for this script
logger = setup_logger("initialize_app")

async def check_api_key():
    """
    Checks if the LLM API key is set in the environment.
    """
    if not config.llm_api_key:
        logger.error("LLM API key is missing. Please set it in the .env file.")
        return False
    logger.info("LLM API key found.")
    return True

async def check_llm_endpoint():
    """
    Checks if the LLM endpoint is reachable.
    """
    from app.services.llm_client import GeminiClient
    llm_client = GeminiClient()
    try:
        response = await llm_client.generate_content("Test prompt")
        if response:
            logger.info("LLM endpoint is reachable.")
            return True
    except Exception as e:
        logger.error(f"Failed to reach LLM endpoint: {e}")
    return False

async def initialize_database():
    """
    Placeholder function for initializing database connections or migrations.
    """
    # Example: Database connection check (replace with actual database setup if applicable)
    # from app.db import db_connection  # Import your database connection setup
    # try:
    #     await db_connection.connect()
    #     logger.info("Database connection established.")
    # except Exception as e:
    #     logger.error(f"Failed to connect to the database: {e}")
    logger.info("Database initialization is currently a placeholder.")
    return True

async def main():
    """
    Main initialization function that performs all necessary checks and setup.
    """
    logger.info("Starting application initialization...")

    # Step 1: Check if essential environment variables are set
    if not await check_api_key():
        logger.error("Initialization failed due to missing API key.")
        return

    # Step 2: Check LLM endpoint connectivity
    if not await check_llm_endpoint():
        logger.error("Initialization failed due to LLM endpoint connectivity issues.")
        return

    # Step 3: Initialize database
    if not await initialize_database():
        logger.error("Initialization failed due to database issues.")
        return

    logger.info("Application initialization completed successfully.")

if __name__ == "__main__":
    # Run the initialization script
    asyncio.run(main())
