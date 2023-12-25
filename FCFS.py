def fcfs(processes):
    n = len(processes)

    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[1])

    dispatch_time = 0  # Initialize dispatch time
    previous_burst = 0
    waiTimes = []
    for i in range(n):
        process_name, arrival_time, burst_time = processes[i]

        # Calculate dispatch time process
        dispatch_time = max(previous_burst + dispatch_time, arrival_time)

        # Calculate response time
        response_time = dispatch_time - arrival_time if dispatch_time > arrival_time else 0

        # Calculate turnaround time
        turnaround_time = burst_time + response_time

        waiTimes.append(response_time)

        print(f"Process {process_name}:")
        print(f"  Response Time: {response_time}")
        print(f"  Turnaround Time: {turnaround_time}")
        print(f"  Dispatch Time: {dispatch_time}")

        previous_burst = burst_time
    print(f"  Average Wait Times: {sum(waiTimes) / len(waiTimes)}\n")


def read_input_from_file(file_path):
    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split()
            pname, burst_time, arrival_time = line[0], int(line[1]), int(line[2])
            process_name = pname
            arrival_time = arrival_time
            burst_time = burst_time
            processes.append((process_name, arrival_time, burst_time))
    return processes


file_path = 'input.txt'

processes = read_input_from_file(file_path)
fcfs(processes)
