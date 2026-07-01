from time import sleep, ctime, time
import threading

def greet_diners(customer):
    print(f"{ctime()} Greetting for customer-{customer}...")
    sleep(1)
    print(f"{ctime()} Greetting for customer-{customer}...Done!")

def custumer_private_workflow(customer):
    #Take Order
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")

    #Do cooking
    print(f"{ctime()} [Thread-{customer}] Cook Spaghetti")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Cook Spaghetti")

    #Manage Bar 
    print(f"{ctime()} [Thread-{customer}] Mange Bar Drink")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Mange Bar Drink")

    print(f"{ctime()} [Thread-{customer}] All served!\n")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    for customer in customers:
        greet_diners(customer)
        
    print(f"]\n{ctime()} --- All customers greeted. splitting into threads...\n")
        
    customer_threads = []

    for customer in customers:
       t = threading.Thread(
           target=custumer_private_workflow,
           args=(customer)
       )
       
       customer_threads.append(t)
       t.start()
       
    for t in customer_threads:
        t.join()

    duration = time() - start_time
    print(f"\n{ctime()} Finished Entire Restaurant Operation in "f"{duration:.2f} secounds")
