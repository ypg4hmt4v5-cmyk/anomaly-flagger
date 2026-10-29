import pandas as pd
from pathlib import Path

folder = Path(__file__).parent

payments = pd.read_csv(folder / "transactions.csv")

print(payments.head())
print(payments.info())
print()
print(payments.describe())
print()
print("number_of_transactions:", len(payments))
print("average_transaction_amount:", payments['amount'].mean())
print()
print("10_largest_transactions:", payments.nlargest(10, 'amount'))

big = payments[payments['amount'] > 10000]
print()
print("number_of_big_transactions:", len(big))

btw = payments[(payments['amount'] > 9500.00) & (payments['amount'] < 9999.99)]
print()
print("number_of_transactions_between_9500_and_9999.99:", len(btw))

dups = payments[payments.duplicated(subset=["supplier", "amount", "date"], keep=False)]
print()
print("Duplicate payments:")
print(dups)

payments["date"] = pd.to_datetime(payments["date"])
payments["weekday"] = payments["date"].dt.dayofweek
payments["hour"] = pd.to_datetime(payments["time"], format="%H:%M").dt.hour

odd_timing = payments[(payments["weekday"] >= 5) | (payments["hour"] < 8)]
print()
print("Odd timing payments:")
print(odd_timing)

big = big.copy()
big["reason"] = "Unusually large payment"

btw  = btw.copy()
btw ["reason"] = "Just below approval limit"

dups = dups.copy()
dups["reason"] = "Possible duplicate payment"

odd_timing = odd_timing.copy()
odd_timing["reason"] = "Odd timing (weekend or out of hours)"

columns = ["id", "date", "time", "supplier", "amount", "approved_by", "reason"]

report = pd.concat([big[columns], btw[columns], dups[columns], odd_timing[columns]])
report["date"] = pd.to_datetime(report["date"])
report = report.sort_values("date")

print()
print("FLAGGED PAYMENTS:")
print(report)
print()
print("Total flagged:", len(report))

report.to_excel(folder / "flagged_payments.xlsx", index=False)
print("Saved to flagged_payments.xlsx")
