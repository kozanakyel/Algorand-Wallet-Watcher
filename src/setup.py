from setuptools import setup

with open('../LICENSE') as f:
    license_text = f.read()

setup(
    name="algo_wallet_watcher",
    version="0.1",
    packages=["algo_wallet_watcher"],
    author="Uğur (Kozan) Akyel",
    author_email="kozanakyel@gmail.com",
    license=license_text
)