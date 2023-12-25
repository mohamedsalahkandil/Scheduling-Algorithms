
from queue import PriorityQueue


class Process:
    def __init__(self, process_name, burst_time, arrival_time):
        self.name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.wait_time = 0
        self.start_time = -1
        self.end_time = arrival_time - 1
        self.remaining_time = burst_time

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time


def SRTF_algorithm(processes):
    ready_queue = PriorityQueue()
    timer = 0
    rem = len(processes)
    while rem:
        for process in processes:
            if process.arrival_time == timer:
                ready_queue.put(process)

        if ready_queue.empty():
            timer += 1
            continue

        pro = ready_queue.get()

        if pro.start_time == -1:
            pro.start_time = timer

        pro.wait_time += timer - pro.end_time - 1
        pro.end_time = timer

        if (pro.remaining_time != 1):
            pro.remaining_time -= 1
            ready_queue.put(pro)
        else:
            rem -= 1

        timer += 1


def read_input_from_file(file_path):
    processes = []

    with open(file_path, 'r') as file:
        flag = 0

        for line in file:
            line = line.strip().split()
            if flag:
                pname, burst_time, arrival_time = line[0], int(line[1]), int(line[2])
                processes.append(Process(pname, burst_time, arrival_time))
            flag = 1
    return processes


if __name__ == "__main__":
    file_path = 'input.txt'
    processes = read_input_from_file(file_path)

    SRTF_algorithm(processes)

    tot_wait_time = 0
    tot_response_time = 0
    tot_turn_arround_time = 0

    for process in processes:
        tot_wait_time += process.wait_time
        tot_response_time += process.start_time - process.arrival_time
        tot_turn_arround_time += process.end_time - process.arrival_time + 1

    avg_wait_time = tot_wait_time / len(processes)
    avg_response_time = tot_response_time / len(processes)
    avg_turn_arround_time = tot_turn_arround_time / len(processes)
    print("Shortest remaining time first:\n",
            f"the average waiting time for the algorithm = {avg_wait_time}"
            f"\nthe average response time for the algorithm = {avg_response_time}"
            f"\nthe average turn arround time for the algorithm = {avg_turn_arround_time}")

