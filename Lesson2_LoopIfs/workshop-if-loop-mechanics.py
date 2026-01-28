#TASK 2 from workshop - mechanical service
#there are 3 mechanics, working 8h/ day. user specifies number of cars to service.
#for each car there is a number of hours needed to complete the work.
import sys

#print("enter the number of cars")
#job_count = int(input())
job_count = int(sys.argv[1])
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count): #as many iterations as many cars
    print(f"Enter the number of working hours for car {job + 1}")
    job_hours = int(input())
    if job_hours <= 0:
        print("error: Invalid number of hours")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours

print("The nearest mechanic will be free within {} days".format(
    int((min(workload1, workload2, workload3) + 7) / 8)
))

print("All mechnics will be free within {} days".format(
    int((max(workload1, workload2, workload3) + 7) / 8)
))



#print(workload1)
#print(workload2)
#print(workload3)