bitcoin_number = int(input())
uan_number = float(input())
commission = float(input())

bitcoin = 1168 * bitcoin_number
uan = 0.15 * uan_number
usd_to_bgn = uan * 1.76

total_bgn = bitcoin + usd_to_bgn

bgn_to_eur = total_bgn / 1.95

commission_fee = bgn_to_eur * commission / 100

result = bgn_to_eur - commission_fee

print(f'{result:.2f}')