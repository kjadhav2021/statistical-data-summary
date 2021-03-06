## statistical-data-summary ##

##### Description

_______________________________________________________________________________
This is a data analysis project written using python and its base packages. No add on modules/libraries and pandas are used while developing the solution.

##### Requirements #####

_______________________________________________________________________________

The requirements for the outputs as well as the input file definition are as below.

Input:
The input file represents a very simplified stream of trades on an exchange. Each row represents a trade.  This data can be thought of as a time series of values in columns:

    <TimeStamp>,<Symbol>,<Quantity>,<Price>

Although the provided input file is small, the solution should be able to handle a source dataset well beyond the amount memory and hard disk space on target machine.

Input Definitions

- TimeStamp is value indicating the microseconds since midnight.
- Symbol is the 3 character unique identifier for a financial instrument (Stock, future etc.)
- Quantity is the amount traded
- Price is the price of the trade for that financial instrument.

Safe Assumptions:

- TimeStamp is always for the same day and won't roll over midnight.
- TimeStamp is increasing or same as previous tick (time gap will never be < 0).
- Price - our currency is an integer based currency.  No decimal points.
- Price - Price is always > 0.

Example: here is a row for a trade of 10 shares of aaa stock at a price of 12
1234567,aaa,10,12

##### Problem statements #####

_______________________________________________________________________________
Find the following on a per symbol basis:

- Maximum time gap (time gap = Amount of time that passes between consecutive trades of a symbol) if only 1 trade is in the file then the gap is 0.
- Total Volume traded (Sum of the quantity for all trades in a symbol).
- Max Trade Price.
- Weighted Average Price.  Average price per unit traded not per trade.

Result should be truncated to whole numbers.

     Example: the following trades
     20 shares of aaa @ 18
     5 shares of aaa @ 7
     Weighted Average Price = ((20 * 18) + (5 * 7)) / (20 + 5) = 15

##### Output #####

_______________________________________________________________________________

The solution produces a file called 'output.csv' in following format

    <symbol>,<MaxTimeGap>,<Volume>,<WeightedAveragePrice>,<MaxPrice>

Moreover, The output is sorted by symbol ascending ('aaa' should be first).

        Sample Input:
        52924702,aaa,13,1136
        52924702,aac,20,477
        52925641,aab,31,907
        52927350,aab,29,724
        52927783,aac,21,638
        52930489,aaa,18,1222
        52931654,aaa,9,1077
        52933453,aab,9,756

        Sample Output (given the above input):
        aaa,5787,40,1161,1222
        aab,6103,69,810,907
        aac,3081,41,559,638

##### Constraints #####

_______________________________________________________________________________

No add on modules/libraries and pandas are used while developing the solution.
