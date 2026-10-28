# Imports
import datetime

# A variable is a name that holds a value
description = "Coffee"
amount = 3.50
category = "Food/Drink"
date = datetime.date.today()

# f-strings let you put variables inside text
print(f"{date} | {description} | {category} |  £{amount:.2f} ")