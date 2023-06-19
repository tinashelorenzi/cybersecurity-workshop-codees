import time

def brute_force_pin(target_pin):
    start_time = time.time()
    attempt = 0

    while True:
        # Convert the attempt number to a 4-digit string, padded with leading zeros if necessary
        current_pin = str(attempt).zfill(4)
        print(current_pin)

        if current_pin == target_pin:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return current_pin, elapsed_time

        attempt += 1

# Main program
target = input("Enter the target PIN: ")

print("Brute forcing PIN...")
found_pin, elapsed_time = brute_force_pin(target)

print("The PIN has been found!")
print("PIN: ", found_pin)
print("Elapsed time: ", elapsed_time, " seconds")
