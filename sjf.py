def user_input(total):

    total_processes = input('Enter total processes: ')

    for i in range(total_processes):

	process_list.append([])
	arrival_time.append([])
	burst_time.append([])

        process_list[i].append(int(input("Enter process number: ")))
        arrival_time[i].append(int(input("Enter arrival time: ")))
        burst_time[i].append(int(input("Enter burst time:  ")))

    return total_processes;     

def waiting_time(total_processes):
    
    j=1
    for i in range(number):
        p=i
        for j in range(number):
            if burst_time[j]<burst_time[p]:
                p=j
            temp=burst_time[i]
            burst_time[i]=burst_time[p]
            burst_time[p]=temp
            temp=a[i]
            process_list[i]=a[p]
            process_list[p]=temp
    return;


process_list = []
burst_time = []
arrival_time = []
waiting_time = 0;
start_time = 0;
total_processes = 0;

processes = user_input( total_processes );

waiting_time(total_processes);
