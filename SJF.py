class Process:
  def __init__(self,process_name,arrival_time,burst_time):
    self.name = process_name
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    self.wait_time = 0
    self.start_time = 0
    self.end_time = 0
  
def SJF_algorithm(processes):
  total_time = 0
  for process in processes :
    total_time += process.burst_time
  current_time = 0
  total_wait_time = 0 
  processes.sort(key = lambda x : x.arrival_time)
  burstProcess = processes
  burstProcess.sort(key = lambda x : x.burst_time)
  print('Process ID\tstart at\t waiting time')
  while True:
   
    for pro in burstProcess:
      if current_time >= pro.arrival_time:
        pro.start_time = current_time
        pro.wait_time = pro.start_time - pro.arrival_time
        current_time += pro.burst_time
        total_wait_time += pro.wait_time
        print(f"  {pro.name}\t\t  {pro.start_time}\t\t\t{pro.wait_time}")
      if current_time >= total_time:
        break 
    if current_time >= total_time:
      break
  return total_wait_time


if __name__ == "__main__":

  processes = [
    Process(1, 0, 5), # (process id ,arrival time , burst time)
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 2),
    Process(5, 4, 3),
  ]
  avg_wait_time = SJF_algorithm(processes) / len(processes)
  print(f"\nthe average waiting time for the algorithm = {avg_wait_time}")
