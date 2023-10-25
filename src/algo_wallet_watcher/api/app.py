from algo_wallet_watcher.api.endpoints.aww_app import app, aww_blueprint
from algo_wallet_watcher.api.endpoints.swagger_app import swagger_ui_blueprint, SWAGGER_URL

from flask_cors import CORS

CORS(app)

app.register_blueprint(aww_blueprint)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0')