from time import sleep, ctime, time

def greet_diners(customer):
    print(f"{ctime()} Greetting for customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Greetting for customer-{customer}...Done!")

def take_orders(customer):
    print(f"{ctime()} Taking Order for customer-{customer}....")
    sleep(1)
    print(f"{ctime()} Taking Order for customer-{customer}...Done!")

def do_cooking(customer):
    print(f"{ctime()} Cooking for customer-{customer}....")
    sleep(1)
    print(f"{ctime()} Cooking for customer-{customer}...Done!")

def mini_bar(customer):
    print(f"{ctime()} Mini Bar for customer-{customer}....")
    sleep(1)
    print(f"{ctime()} Mini Bar for customer-{customer}...Done!")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    
    start_time = time()

    for customer in customers:
        greet_diners(customer)
        take_orders(customer)
        do_cooking(customer)
        mini_bar(customer)

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in{duration:0.2f} secounds.")
