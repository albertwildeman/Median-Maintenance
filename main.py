from FileReadLib import get_array
from MedianMaintenanceLib import median_maintenance

import statistics as stats

filename = "Median"
a = get_array(filename)

medians = median_maintenance(a)
answer = sum(medians)%10000

print("Answer: " + str(answer))

# check
# errs = [x for x in range(len(a)) if stats.median(a[:x+1])!=medians[x]]

print("all done.")
