import uvicorn


def run_server():
    # Create Uvicorn config
    config = uvicorn.Config("main:app", port=8000, log_level="info")

    # Create Uvicorn server
    server = uvicorn.Server(config)

    # Run the server
    server.run()
