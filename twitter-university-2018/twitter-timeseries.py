# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import datetime

# To split string based on hypens
def datesplit(date):
    return date.split("-")

# Function to check if date of datapoint falls in given interval
def checkDateInterval(givenInterval, yearOfData, monthOfData, dayOfData):
    # Get the start interval and end interval
    startInterval = givenInterval[0]
    endInterval   = givenInterval[1]
        
    # Get the year and month of the start interval and end interval
    startYearInterval, startMonthInterval = datesplit(startInterval)
    endYearInterval,   endMonthInterval   = datesplit(endInterval)

    # Examine date of datapoint
    return datetime.date(int(startYearInterval),int(startMonthInterval), 1) <= datetime.date(int(yearOfData),int(monthOfData),int(dayOfData)) < datetime.date(int(endYearInterval), int(endMonthInterval), 1)

# Function to aggregate datapoints
def aggregateTimeseriesData(datapoints, givenInterval):

    # Use dictionary table to store final results
    result = {}
    
    # iterate through datapoints
    for datapoint in datapoints:
        
        # split datapoint by its component
        dateOfDatapoint, enggagementType, enggagementValue = datapoint.replace(" ","").split(",")
        
        # Get the details of datapoint's date
        yearOfData, monthOfData, dayOfData = datesplit(dateOfDatapoint)
        
        # Clarify date interval of each data and aggregate enggagement type value by date (year and month)
        if checkDateInterval(givenInterval, yearOfData, monthOfData, dayOfData):
            dateKey = (yearOfData) + "-" + (monthOfData)
            if not dateKey in result:
                result[dateKey] = {} # use nested dict
            try:
                result[dateKey][enggagementType] += int(enggagementValue.split()[0])
            except:
                result[dateKey][enggagementType]  = int(enggagementValue.split()[0])

    # Sort by key descending and return dict result as a list
    return(sorted(result.items(), key=lambda kv: kv[0], reverse=True))
    
# main function
def main():
    # Capture start interval and end interval
    interval  = input().split(",")
    # Capture blank line
    blankLine = input()
    
    datapoints = []
    # Capture datapoints while stdin
    for line in sys.stdin:
        datapoints.append(line)
    
    # Invoke function to aggregate datapoints based on timeseries
    aggregatedData = aggregateTimeseriesData(datapoints, interval)
    
    # Final result 
    # format of aggegated data : [(datekey),{dict of enggagement}]
    for datapoints in aggregatedData:
        # Print datekey
        print(datapoints[0], end="")
        # Print aggegated enggagement
        for enggagementType, enggagementNumber in sorted(datapoints[1].items()):
            print(", "+ enggagementType + ", " + str(enggagementNumber), end="")
        # Print next line
        print()
        
# main function triggered here
if __name__ == "__main__":
    main()