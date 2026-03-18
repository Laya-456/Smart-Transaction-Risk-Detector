n=int(input("enter number of transactions: "))
transactions=[]
for i in range(n):
    m=int(input("Enter Transaction:"))
    transactions.append(m)
categories={
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
for i in transactions:
    if i<=0:
        categories["invalid"].append(i)
    elif i>0 and i<=500:
        categories["normal"].append(i)
    elif i>500 and i<=2000:
        categories["large"].append(i)
    else:
        categories["high_risk"].append(i)
valid=[i for i in transactions if i>0]
total=sum(valid)
count=len(transactions)
is_frequent = count>5
is_large_spender=total>5000
is_suspicious=len(categories["high_risk"])>=3
if is_suspicious and is_frequent:
    risk="High Risk"
elif is_large_spender or is_frequent:
    risk="Moderate Risk"
else:
    risk="Low Risk"
summary=(total,count)

print("FINANCIAL RISK REPORT:")
print("categorized transactions:",categories)
print("transaction summary:",summary)
print("total transaction value:",total)
print("number of transactions:",count)
print("final risk classification:",risk)