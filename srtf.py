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

def waiting_and_turnaround_time(total_processes):
    
    time=0
    remain=0
    j=i   	
    while remain!=n:
        smallest=j
	i=0;        
	while i<n:
            if at[i]<=time and rt[i]<rt[smallest] and rt[i]>0:
                smallest=i
            i+=1       
        rt[smallest]-=1
        if rt[smallest]==0:
            remain+=1
            endTime=time+1
            print (smallest+1)
            print("\t","\t")
            print(endTime-at[smallest])
            print("\t","\t")
            print(endTime-bt[smallest]-at[smallest])
            sum_wait+=endTime-bt[smallest]-at[smallest]
            sum_turnaround+=endTime-at[smallest]
    	time+=1


process_list = []
burst_time = []
arrival_time = []
remaining_time = []
waiting_time = 0;
start_time = 0;
total_processes = 0;

processes = user_input( total_processes );

waiting_and_turnaroundtime(total_processes);
