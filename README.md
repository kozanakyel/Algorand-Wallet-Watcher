# ALGORAND WALLET WATCHER - AWW

The main purposes of this project create a watcher list for especially Algorand wallets. Then added to those wallets to watcher list with correctly checked it is truely a algorand wallet like has the 58 string length, mainnet alogo response is correct for this operations, etc.

Additionally this backend structure uses documentation with swagger platform and rest-api for add wallet or list wallet operation. Thirdly AWW has a periodic check state mechanism for always this wallet and balaces saved correctly. Also we logged all this information via the logger object.

How to build a Docker container and run via the terminal:

```
$ docker build -t aww .
$ docker run -p 5005:5005 -v $(pwd)/logs:/app/src/algo_wallet_watcher/Infrastructure/logger/logs aww
```

How to install and running application, via this command: 

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U pip
$ pip install -U requirements.txt
$ pip install -e src
$ export FLASK_APP=src/algo_wallet_watcher/api/app.py
$ flask run
```

I should talk about the system architecture for this application AWW. I have used Clean Architecture principles and you can see Infrastructure, app and domain layers for investigation. 

- We should look to Clean Architecture diagram for AWW:

![Clean Arcitecture diagram for AWW](/assets/images/clean_temp.png)

- Logger example via the terminal for each changing balance operation on the wallets:

![Logger examples for AWW](/assets/images/log_amount.png)

- use "/swagger" endpoint for Documentation via the flask_swagger_ui and you can try it out via swagger UI experiences:

![Swagger ui-1 for AWW](/assets/images/swg1.png)
![Swagger ui-2 for AWW](/assets/images/swg2.png)

You can contact me via email: kozanakyel@gmail.com