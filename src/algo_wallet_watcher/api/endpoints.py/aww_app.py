from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from algo_wallet_watcher.Infrastructure.orm_mapper import orm
import algo_wallet_watcher.Infrastructure.config as config

from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import WalletRepository
from algo_wallet_watcher.core.domain.wallet import Wallet
from algo_wallet_watcher.api.services import aww_service


orm.start_mappers()
engine = create_engine(config.get_db_uri())
get_session = sessionmaker(bind=engine)
orm.metadata.create_all(engine)

app = Flask(__name__)

aww_blueprint = Blueprint('aww', __name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.get_db_uri()

db = SQLAlchemy(app)

@aww_blueprint.route("/add_wallet", methods=["POST"])
def add_wallet():
    session = get_session()
    repo = WalletRepository(session)
    try:
        aww_service.add_wallet(
            request.json["address"],
            request.json["amount"],
            request.json["state"],
            repo,
            session,
        )
    except aww_service.InvalidAddress as e:
        return {"message": str(e)}, 400
    return "OK", 201


app.register_blueprint(aww_blueprint)

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0')

