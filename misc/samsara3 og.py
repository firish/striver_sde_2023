def process_requests(requests, totalslots):
    memory = [0] * totalslots  # 0 indicates free, 1 indicates occupied
    current_slot = 0
    
    def find_free_slots(num_slots):
        nonlocal current_slot
        start_slot = current_slot
        count = 0
        while count < num_slots:
            if memory[current_slot] == 0:
                count += 1
            else:
                count = 0
                start_slot = (current_slot + 1) % totalslots
            current_slot = (current_slot + 1) % totalslots
            # If we complete one full cycle and come back to start_slot, then break
            if current_slot == start_slot:
                return -1
        return start_slot

    results = []
    for req in requests:
        action, start, num_slots = req
        if action == "store":
            start_slot = find_free_slots(num_slots)
            results.append(start_slot)
            if start_slot != -1:
                for i in range(num_slots):
                    memory[(start_slot + i) % totalslots] = 1
        elif action == "free":
            for i in range(num_slots):
                memory[(start + i) % totalslots] = 0
            results.append(None)
    return results

# Example:
requests = [["store", 0, 6], ["store",11, 3], ["free", 0, 3], ["store", 10, 3], ["store", 6, 6]]
totalslots = 15
print(process_requests(requests, totalslots))  # Expected output: [0, -1, 3, None, 0]
