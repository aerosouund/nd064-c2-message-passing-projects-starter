import os
import time
from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    from app.udaconnect.controllers import create_rpc_server

    print("Server starting on port 5005...")
    server = create_rpc_server()
    server.add_insecure_port("[::]:5005")
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

    app.run(debug=True)
