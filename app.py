from methods.facebook import get_facebook
from methods.amazon import get_amazon
from methods.flipkart import get_flipkart
from methods.swiggy import get_swiggy
from methods.revv import get_revv
from methods.whatsapp import get_whatsapp
from methods.ola import get_ola

email = "aamirbaugwala@gmail.com"
mobile = '9930952429'

# print(get_amazon(email))
# print(get_facebook(email))
# print(get_flipkart(email))
# print(get_revv(email))
# print(get_swiggy(mobile))
# print(get_ola(mobile))
print(get_whatsapp(mobile))