#  Smart Transaction Risk Detector

A lightweight Python tool that analyzes user transaction data and identifies potential risk patterns based on spending behavior.

---

##  What It Does

The **Smart Transaction Risk Detector** processes a list of transaction amounts and:

* Categorizes each transaction based on value ranges
* Detects behavioral patterns such as high spending and frequent activity
* Flags high risk only when suspicious activity and frequent transactions occur together
* Generates a final risk classification for the user

This can be useful as a **basic fraud detection prototype** in digital payment systems.

---

## How It Works

1. **Input Handling**
   Accepts multiple transaction values from the user.

2. **Transaction Classification**
   Each transaction is categorized into:

   * `normal` → ₹1–₹500
   * `large` → ₹501–₹2000
   * `high_risk` → Above ₹2000
   * `invalid` → ≤ ₹0

3. **Pattern Detection**
   The system checks for:

   * High number of transactions
   * Total spending exceeding a threshold
   * Multiple high-risk transactions

4. **Risk Evaluation**
   Based on detected patterns, the system assigns:

   * **Low Risk**
   * **Moderate Risk**
   * **High Risk**

---

## Getting Started

### Prerequisites

* Python 3.x installed

### Run the Program

```bash id="g30a2x"
python main.py
```

## Example Input

```id="0p4r9y"
Enter number of transactions: 4
Enter Transaction: 100
Enter Transaction: 2500
Enter Transaction: 3000
Enter Transaction: 200
```


## Sample Output

```id="6u6rj7"
FINANCIAL RISK REPORT:
categorized transactions: {'normal': [100, 200], 'large': [], 'high_risk': [2500, 3000], 'invalid': []}
transaction summary: (5800, 4)
total transaction value: 5800
number of transactions: 4
final risk classification: Moderate Risk
```

---

## Key Concepts Used

* Lists & List Comprehension
* Dictionaries for classification
* Conditional Logic
* Looping structures
* Tuple for summary representation
