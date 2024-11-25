class Process:
    def __init__(self, process_id, burst_time):
        self.process_id = process_id
        self.burst_time = burst_time

class FIFO:
    def __init__(self, processes):
        self.processes = processes

    def calculate_waiting_times(self):
        waiting_times = []
        total_wait_time = 0

        #calculando o tempo de espera doprocesso
        for i in range(len(self.processes)):
            if i == 0:
                waiting_times.append(0) 
            else:
                waiting_times.append(waiting_times[i-1] + self.processes[i-1].burst_time)  #acumula o tempo de espera

            total_wait_time += waiting_times[i]

        #calculando o tempo médio de espera
        avg_wait_time = total_wait_time / len(self.processes)
        return avg_wait_time

#função para capturar os dados
def get_processes_from_user():
    processes = []
    n = int(input("Quantos processos você deseja inserir? "))
    for i in range(n):
        process_id = str(input(f"Digite o nome do processo {i+1}: "))
        burst_time = int(input(f"Digite o tempo de execução (burst time) do processo {i+1}: "))
        processes.append(Process(process_id, burst_time))
    return processes


processes = get_processes_from_user()

# Criando um escalonador FIFO
fifo_scheduler = FIFO(processes)
avg_wait_time = fifo_scheduler.calculate_waiting_times()
print(f'Tempo médio de espera (FIFO): {avg_wait_time} minutos')