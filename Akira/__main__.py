import asyncio
from multiprocessing import Process
from Akira.bot import main
from web import run_web

if __name__ == "__main__":
    try:
        # Start Flask web server in a separate process
        flask_process = Process(target=run_web)
        flask_process.start()

        # Run the bot asynchronously
        asyncio.run(main())

    except Exception as e:
        print(f"Error while starting bot or Flask: {e}")
