import rumps
import requests

def get_eth_cryptonkt():
    url_cryptomkt = "https://api.cryptomkt.com/v1/ticker"
    payload = {'market': 'ETHCLP'}
    r = requests.get(url_cryptomkt, params=payload, verify="ca-cert.pem")
    return r.json()["data"][0]["ask"]

def get_eth_surbtc():
    url_surbtc = "https://www.surbtc.com/api/v2/markets/eth-clp/ticker.json"
    r = requests.get(url_surbtc, verify="ca-cert.pem")
    return r.json()["ticker"]["min_ask"][0][:-2]

pem_path = "lib/python2.7/certifi/cacert.pem"

class CryptoAppStatusBarApp(rumps.App):

    eth_cryptomkt = "Actualizando"
    eth_surbtc = "Actualizando"

    @rumps.clicked("Refresh")
    def sayhi(self, _):
        self.refresh_title()

    @rumps.timer(5)
    def refresh_title(self, _):
        cm = "CMKT " + self.eth_cryptomkt
        sb = "SBTC " + self.eth_surbtc
        self.title = sb + " || " + cm

    @rumps.timer(5)
    def refresh_cryptomkt(self, _):
        try:
            self.eth_cryptomkt = get_eth_cryptonkt()
        except Exception:
            self.eth_cryptomkt = "Actualizando"

    @rumps.timer(5)
    def refresh_surbtc(self, _):
        try:
            self.eth_surbtc = get_eth_surbtc()
        except Exception:
            self.eth_surbtc = "Actualizando"

if __name__ == "__main__":
    CryptoAppStatusBarApp("CryptoApp", "CryptoApp").run()

