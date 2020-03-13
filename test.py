from payeer_api import PayeerAPI

account = 'P1000000'
api_id = '123456789'
api_pass = 'KRicaFodFrgJer6'

p = PayeerAPI(account, api_id, api_pass)

p.get_balance()