from algo_wallet_watcher.api.endpoints.aww_app import app, aww_blueprint


app.register_blueprint(aww_blueprint)

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0')