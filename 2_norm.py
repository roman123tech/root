# import csv

# def read_csv(filename):
#     with open(filename,mode='r') as file:
#         reader=csv.DictReader(file)
#         rows=list(reader)
#     return rows

# def write_csv(output_file,fieldnames,rows):
#     with open(output_file,mode='w',newline='') as file:
#         writer=csv.DictWriter(file,fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)

# def minmax(rows,column,newMin,newMax,minm,maxm):
#     for row in rows:
#         val=float(row[column])
#         val=((val-minm)/(maxm-minm))*(newMax-newMin)
#         val+=newMin
#         row[column]=str(val)

# def zScore(rows,column,mean,std_dev):
#     for row in rows:
#         val=float(row[column])
#         val=(val-mean)/std_dev
#         row[column]=str(val)

# def getmean_stddev(values):
#     n=len(values)
#     mean=sum(values)/n
#     std_dev=(sum((x-mean)**2 for x in values)/n)**0.5
#     return mean,std_dev




# input_file='AirQualityUCI.csv'
# rows=read_csv(input_file)
# headers=list(rows[0].keys())

# print("Choose Normalization Type: ")
# print("1. MinMax")
# print("2. ZScore")
# choice=int(input("Enter the choice: "))

# if choice==1:
#     print("Enter the column to normalize")
#     ctr=0
#     for val in headers:
#         print(ctr," ",val)
#         ctr+=1
#     colnum=int(input("Enter column number: "))
#     column=headers[colnum]
#     values=[float(row[column]) for row in rows]
#     minm=min(values)
#     maxm=max(values)
#     # print(values)
#     newMin=float(input("New Min: "))
#     newMax=float(input("New Max: "))
#     minmax(rows,column,newMin,newMax,minm,maxm)
#     # print(rows)
#     output_file=f'minMaxNormalize{column}.csv'
#     write_csv(output_file,rows[0].keys(),rows)
    
# elif choice==2:
#     for attr in headers:
#         values=[float(row[attr]) for row in rows]
#         mean,std_dev=getmean_stddev(values)
#         zScore(rows,attr,mean,std_dev)
#     output_file=f'ZScore.csv'
#     write_csv(output_file,rows[0].keys(),rows)































