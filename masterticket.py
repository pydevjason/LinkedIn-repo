# masterticket.py
# ticket purchasing application

SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100

def calculate_price(purchased_tickets):
    return (purchased_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print(f"There are currently {tickets_remaining} tickets remaining")
    user = input("Please enter your name: ")
    try:
        purchased_tickets = int(input(f"{user.title()}, how many tickets would you like to \
purchase? "))
        # raise a ValueError if request for tickets exceeds available tickets
        if purchased_tickets > tickets_remaining:
            raise ValueError(f"there are only {tickets_remaining} tickets remaining!")
    except ValueError as err:
        print(f"Uh oh, we ran into an issue. {err} Please try again.")
    else:
        amount_due = calculate_price(purchased_tickets)
        print(f"A ${SERVICE_CHARGE:.2f} service charge will apply")
        print(f"The total due is ${amount_due}")
        proceed = input("Would you like to proceed? ")

        if proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= purchased_tickets

        else:
            print(f"Thank you, {user}!")

print("All tickets have been sold.")
