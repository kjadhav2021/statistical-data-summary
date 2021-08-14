import csv
import sys

def process_trades(input_file_path):
    input_file = open(input_file_path,"r")
    # read input csv file
    csv_reader = csv.reader(input_file)
    trades = []  # trades list
    output = {}  # dictionary with columns <symbol>,<MaxTimeGap>,<Volume>,<WeightedAveragePrice>,<MaxPrice>. Symbol is key for this dictionary
    timestamp, symbol, quantity, price = [],[],[],[] # individual columns from input csv file

    for trade_row in csv_reader:
        trades.append(trade_row)

    for row  in range(0, len(trades)):
        populate_columns(trades, timestamp, symbol, quantity, price, row)

    for col1, col2, col3, col4  in zip(symbol,timestamp, quantity, price ):
        # checking output dictionary , if empty then start adding columns into dictionary
        if (output.get(col1) is None):
            initialize_dictionary(output, col1, col2, col3, col4)
        else:
            # accumulating the trade volumes
            prevvolume = output.get(col1)[1]['Volume']
            newvolume = col3
            newvalueforvolume = int(prevvolume) + int(newvolume)
            # getting maxprice for trades
            prevmaxprice = output.get(col1)[2]['MaxPrice']
            newmaxprice  = col4
            newvaluemaxprice = max(int(prevmaxprice) , int(newmaxprice))
            # calculating the traded price and weighted average price for trade
            prevtradedprice = output.get(col1)[3]['TradedPrice']
            newtradedprice = (int(newvolume)*int(newmaxprice))+int(prevtradedprice)
            weightavgprice = newtradedprice/newvalueforvolume
            # getting occurence and timestamp , to determine the max time gap
            prevoccurence = output.get(col1)[5]['Occurence']
            newoccurence = prevoccurence+1
            prevtimestamp = output.get(col1)[0]['TimeStamp']
            newtimestamp  = col2
            maxtimegap = int(newtimestamp) - int(prevtimestamp)
            currenttimegap = output.get(col1)[6]['MaxTimeGap']
            maxtimegap = max(currenttimegap,maxtimegap)
            if(newoccurence == 1):
                maxtimegap = 0

            # updating the output dictionary values with newvolume,max price,traded price, weighted average price, and max time gap
            setvalues(output, col1, col2, newvalueforvolume, newvaluemaxprice, newtradedprice, weightavgprice, newoccurence, maxtimegap)


    with open("outputfile/output.csv", "w") as csv_file:
        csvwriter = csv.writer(csv_file, sys.stdout, lineterminator='\n')
        # csvwriter.writerow([ 'Symbol', 'MaxTimeGap', 'Volume', 'WeightedAveragePrice','MaxPrice' ])

        for symbol in sorted(output):
            csvwriter.writerow([symbol, output[symbol][6]['MaxTimeGap'],
                            output[symbol][1]['Volume'], round(output[symbol][4]['WeightedAveragePrice']),
                            output[symbol][2]['MaxPrice']])
        csv_file.close()


def setvalues(outputdict, col1, col2, newvolume, newmaxprice, newtradedprice, newweightavgprice, newoccurence, newmaxtimegap):
    outputdict.update({col1:[{'TimeStamp':col2},{'Volume': newvolume},{'MaxPrice': newmaxprice},
                                      {'TradedPrice': newtradedprice},{'WeightedAveragePrice': newweightavgprice},
                                      {'Occurence': newoccurence},{'MaxTimeGap':newmaxtimegap}]})

def initialize_dictionary(outputdict, col1, col2, col3, col4):
    outputdict.update({col1:[{'TimeStamp':col2},{'Volume': col3},{'MaxPrice': col4},
                                      {'TradedPrice': int(col3)*int(col4)},{'WeightedAveragePrice':0},
                                      {'Occurence': 1},{'MaxTimeGap':0}]})

def populate_columns(items, timestamp, symbol, quantity, price, i):
    timestamp.append(items[i][0])
    symbol.append(items[i][1])
    quantity.append(items[i][2])
    price.append(items[i][3])

filepath = input("Enter the input file name.\n")
process_trades(filepath)
# process_trades("inputfile/input.csv")
