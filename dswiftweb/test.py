import requests
import time
from datetime import date
today = date.today()
today = str(today)
user_id = 1
url = 'https://gym-management97.herokuapp.com/api/attendance'
data = {
        'fingerprint_id': user_id,
        'date':today
        }
r = requests.post(url,data= data)
print(r.text);
