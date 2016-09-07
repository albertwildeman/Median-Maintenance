from FileReadLib import get_array
from MedianMaintenanceLib import median_maintenance

filename = "Median"
a = get_array(filename)

medians = median_maintenance(a)
answer = sum(medians)%10000

print("Answer: " + str(answer))
print("all done.")
