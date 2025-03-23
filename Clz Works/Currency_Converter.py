import requests

def currenty_convert(amount, Current, Next):
    url = f"https://v6.exchangerate-api.com/v6/04e870f6d0d9facfc2360ac5/latest/{Current}"
    data = requests.get(url)
    toJsons = data.json()
    basecurrency = toJsons['base_code']
    print(basecurrency)
    
    totoalamount = amount * toJsons['conversion_rates'][Next]
    print(totoalamount)
    
currenty_convert(1000,"NPR","USD")
try: 
    amount = int(input("Enter the amount: "))
    Current = input("Enter the current Currency").upper()
    Next = input ("Enter the changeable amount: ")
    currenty_convert(amount, Current, Next)
except Exception as Error:
    print(Error)