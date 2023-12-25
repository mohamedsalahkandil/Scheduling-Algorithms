
class Process:
    def __init__(self):
        self.arrivalTime = 0
        self.burstTime = 0
        self.startTime = []
        self.waitTime = 0
        self.responseTime = 0
        self.finalTime = 0
        self.turnAroundTime = 0
        self.pname = 0


def round_robin_scheduling(n, processes, quantum):
    remaining_processes_count = n
    s = [[-1] * 111 for _ in range(n)]
    time = 0
    # mini = float('inf')  # infinity
    burst_Times = [process.burstTime for process in processes]
    arrival_times = [process.arrivalTime for process in processes]
    gantt_chart = []

    total_wait_time = 0
    total_turn_around_time = 0
    total_responseTime = 0
    while remaining_processes_count != 0:
        mini = float('inf')
        flag = False

        for i in range(n):
            p = time + 1
            if arrival_times[i] <= p and mini > arrival_times[i] and burst_Times[i] > 0:
                index = i
                mini = arrival_times[i]
                flag = True

        # This flag indicates that there was a process in this timeframe
        if not flag:
            time += 1
            gantt_chart.append(-1)  # Idle time
            continue

        j = 0
        while s[index][j] != -1:
            j += 1

        if s[index][j] == -1:
            s[index][j] = time
            processes[index].startTime.append(time)

        # All the conditions of the burst time values
        # 7-2-2-2 1
        if burst_Times[index] <= quantum:
            gantt_chart.extend([index + 1])
            time += burst_Times[index]  # هتزود الوقت بالبيرست تايم عشان مش هنعرف نزوده بالوقت العادي
            burst_Times[index] = 0  # وبعد كده نصفر البيرست تايم
        else:
            gantt_chart.extend([index + 1])
            time += quantum
            burst_Times[index] -= quantum

        if burst_Times[index] > 0:
            arrival_times[index] = time + 1

        if burst_Times[index] == 0:
            remaining_processes_count -= 1
            processes[index].finalTime = time

            processes[index].waitTime = processes[index].finalTime - processes[index].arrivalTime - processes[
                index].burstTime
            total_wait_time += processes[index].waitTime

            processes[index].turnAroundTime = processes[index].burstTime + processes[index].waitTime
            total_turn_around_time += processes[index].turnAroundTime

            processes[index].responseTime = processes[index].startTime[0] - processes[index].arrivalTime
            total_responseTime += processes[index].responseTime

    print("Gantt Chart:")
    print("-------------")
    print("|", end="")
    for time_unit in gantt_chart:
        if time_unit == -1:
            print("   |", end="")
        else:
            print(f" P{time_unit} |", end="")
    print("\n-------------")

    avg_wt = total_wait_time / n
    avg_tat = total_turn_around_time / n
    avg_rt = total_responseTime / n
    print(f"The average wait time is: {avg_wt}")
    print(f"The average TurnAround time is: {avg_tat}")
    print(f"The average response time is: {avg_rt}")


def read_input_from_file(file_path):
    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split()
            pname, burst_time, arrival_time = line[0], int(line[1]), int(line[2])
            process = Process()
            process.pname = pname
            process.burstTime = burst_time
            process.arrivalTime = arrival_time
            processes.append(process)
    return processes


file_path = 'input.txt'
processes = read_input_from_file(file_path)
round_robin_scheduling(len(processes), processes, 2)
