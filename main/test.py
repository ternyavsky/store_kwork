from yoomoney import Authorize, Quickpay
# Authorize(
#         client_id='E4E5FA2D44D006C6DD1C8523833DDCB1610FFE147F54E17E7784FB015F5F2F11',
#         redirect_uri='http://store.3d-mitra.ru/decline',
#         scope=["account-info",
#              "operation-history",
#              "operation-details",
#              "incoming-transfers",
#              "payment-p2p",
#              "payment-shop",
#              ]
#     )410014797761818
quickpay = Quickpay(
            receiver=" 410011820942473",
            quickpay_form="shop",
            targets="Оплата товара",
            paymentType="SB",
            sum=1500,
            )
print(quickpay.base_url)
print(quickpay.redirected_url)