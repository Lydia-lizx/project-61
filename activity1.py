
"""
PYTHON TICKET MACHINE PROJECT

STEP 1: CREATE THE CHANGE FUNCTION
Create a function called calculate_change(paid, price).
Subtract the ticket price from the amount paid.
Return the change.

STEP 2: SET UP THE TICKET PRICE
Set ticket_price to 30.
Display a welcome message.
Show the accepted coins: 1, 5, 10, and 25.

STEP 3: CREATE STARTING COUNTERS
Set total_inserted to 0.
Set coins_inserted to 0.

STEP 4: START THE WHILE LOOP
Use while True to keep asking for coins.

STEP 5: SKIP INVALID COINS
Check if the coin is not 1, 5, 10, or 25.
If invalid, print an error message.
Use continue to skip that coin.

STEP 6: ADD VALID COINS
Add each valid coin to total_inserted.
Increase coins_inserted by 1.
Print the running total.

STEP 7: STOP THE LOOP
When total_inserted >= ticket_price:
    Print a success message.
    Use break to stop the loop.

STEP 8: CHECK FOR CHANGE
Call calculate_change() to find the change.
If change_due is 0, use pass.
Otherwise, print the change amount.

STEP 9: PRINT THE FINAL SUMMARY
Display:
- Ticket price
- Number of coins inserted
- Total amount paid
- Change given

STEP 10: TEST YOUR PROGRAM
Test valid and invalid coins.
Try paying exactly 30.
Try paying more than 30.
"""

def calculate_change(paid, price):
     change = paid - price
     return change

ticket_price = 30
print("Welcome to the Ticket Machine!")
print("Accepted coins: 1, 5, 10, 25")

total_inserted = 0
coins_inserted = 0
while True:
     coin = int(input("Insert a coin: (1, 5, 10, 25): "))
     if coin not in [1, 5, 10, 25]:
         print("Invalid coin. Please insert a valid coin.")
         continue
     total_inserted += coin
     coins_inserted += 1
     print(f"Total inserted: {total_inserted}")
     if total_inserted >= ticket_price:
          print("Ticket purchased successfully!")
          break
change_due = calculate_change(total_inserted, ticket_price)
print("printing your parking ticket...")
if change_due == 0:
     pass
else:
        print(f"Change due: {change_due}")

print("\n-----Final Summary-----")
print(f"Ticket price: {ticket_price}")
print(f"Number of coins inserted: {coins_inserted}")
print(f"Total amount paid: {total_inserted}")
print(f"Change given: {change_due}")