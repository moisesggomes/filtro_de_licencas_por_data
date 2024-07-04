from datetime import datetime

date1_str = "12/10/2013"
date2_str = "15/10/2013"

date1 = datetime.strptime(date1_str, "%d/%m/%Y")
date2 = datetime.strptime(date2_str, "%d/%m/%Y")

if date1 < date2:
    print("Date 1 is earlier than Date 2.")
else:
    print("Date 1 is not earlier than Date 2.")