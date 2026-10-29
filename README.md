# Payment Anomaly Flagger

**Problem:** Companies make thousands of supplier payments, and a small
number are mistakes or fraud. Nobody has time to read every line, so finance
teams need a way to find the payments worth checking first.

**Overview:** A Python tool, built with pandas, that scans a payment file and
flags suspicious transactions with a reason for each. It detects:

- Unusually large payments (over £10,000)
- Payments just below the £10,000 approval limit (£9,500 to £9,999.99),
  a known pattern when someone tries to avoid approval
- Possible duplicate payments (same supplier, amount and date)
- Odd timing (weekends, or before 8am)

**Output:** One Excel report listing every flagged payment, with the reason
beside it, sorted by date.

**Results:** Tested on 214 practice payments containing 12 planted problems.
The tool found all 12 (13 rows, because each duplicate shows as a pair).
It also exposed a split payment: two Dell UK payments on the same day
(£9,950 and £9,875) that together exceed the limit.

**Limitations:** Thresholds are fixed values I chose by judgement, and a
flag means "worth a look", not proof of fraud. Future versions could
calculate thresholds statistically and detect split payments automatically.

**Built with:** Python, pandas, openpyxl

*All data is fake and generated for practice.*
