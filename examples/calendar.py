import sys
import calendar
from datetime import datetime

args = sys.argv


month = datetime.today().month
year = datetime.today().year


if len(args) == 1:
    pass

if len(args) == 2:
    month = args[0]
