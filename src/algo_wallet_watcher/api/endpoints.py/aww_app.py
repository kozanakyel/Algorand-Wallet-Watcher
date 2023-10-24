from flask import Flask, request, jsonify, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from algo_wallet_watcher.Infrastructure.orm_mapper import orm
import algo_wallet_watcher.Infrastructure.config as config

from algo_wallet_watcher.Infrastructure.adapters.wallet_repository import WalletRepository
from algo_wallet_watcher.core.domain.wallet import Wallet


orm.start_mappers()
engine = create_engine(config.get_api_url())
get_session = sessionmaker(bind=engine)
orm.metadata.create_all(engine)

app = Flask(__name__)

aww_blueprint = Blueprint('aww', __name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.get_api_url()

db = SQLAlchemy(app)

@aww_blueprint.route("/add_wallet", methods=["POST"])
def add_wallet():
    session = get_session()
    repo = WalletRepository(session)
    address = 'newaddress'
    amount = 123456
    state = 'Offline'
    wallet = Wallet(address=address, amount=amount, state=state)
    try:
        wallet_list = repo.list()
        wallet_address_list = [x.address for x in wallet_list]

        if address in wallet_address_list:
            raise ValueError(f"Error This Wallet is exist: {wallet}")
        repo.add(wallet)
        session.commit()
    except ValueError as e:
        return {"message": str(e)}, 400
    return "OK", 201

