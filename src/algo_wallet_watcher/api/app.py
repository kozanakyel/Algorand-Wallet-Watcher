from algo_wallet_watcher.api.endpoints.aww_app import app, aww_blueprint
from algo_wallet_watcher.api.endpoints.swagger_app import swagger_ui_blueprint, SWAGGER_URL

from algo_wallet_watcher.Infrastructure.services.periodic_state_check_service import PeriodicStateCheckService

from flask_cors import CORS
import time

CORS(app)

app.register_blueprint(aww_blueprint)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    periodic_service = PeriodicStateCheckService()
    periodic_service.start_periodic_check()
    app.run(port=5005, host='0.0.0.0')
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass