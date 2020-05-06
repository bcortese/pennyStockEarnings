Penny Stock History Project
I wanted more insite on not my total stock investment portfolio, but narrow the scope down to the penny stocks I had invested in. Mainly to see how my investment strategies were paying off. I decided to create a quick script that will show me the amount of money I have currently spent on penny stocks, and the amount returned. 


Prerequisites
User login: You can set this up however you want, but this function I have set up is used to contact the Robinhood database using my credentials. I currently have mine saved in a csv file, but you may just put your creds in however you want. 
The historical data: Using robin_stocks api function (export_completed_stock_orders) exports past transactions to  csv

Instructions
Script gives the user the option to return one of two bar graphs, one including open investments and the other with just closed investments. When an option is selected, the data will be displayed into a bar graph using matplotlib.



Built With the following packages.
robin_stocks - Robinhood Api
pandas
csv
matplotlib

