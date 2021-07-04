import random,requests

randomno=random.randint(1,999999)


msg=f"Your One Time Password is {randomno}"


url="https://www.fast2sms.com/dev/bulk"

params={
   
        "authorization":"your api key here",
        "sender_id":"THETCS",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"Your Phone No here without double quote",
    }

requests.get(url,params=params)

