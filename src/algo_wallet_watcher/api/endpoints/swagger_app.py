from flask_swagger_ui import get_swaggerui_blueprint
from algo_wallet_watcher.api.endpoints.aww_app import app
from flask import jsonify
import json, os
from algo_wallet_watcher.Infrastructure.config import SWAGGER_JSON_URL


# Configure Swagger UI
SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:5005/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Algorand Wallet Watcher - AWW"}
)


@app.route("/swagger.json")
def swagger():
    with open(
        os.path.join(os.getcwd(), SWAGGER_JSON_URL),
        "r",
    ) as f:
        return jsonify(json.load(f))
