from collections import namedtuple
import csv
import gc
import tracemalloc

# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__
class RowWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_tuples(filename):
	'''
	Read the bus ride data as a list of tuples
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			# A tuple
			record = (route, date, daytype, rides)
			records.append(record)

	return records

def read_rides_as_dictionary(filename):
	'''
	Read the bus ride data as a list of dictionaries
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			# A dictionary
			record = {
			    'route': route,
			    'date': date,
			    'daytype': daytype,
			    'rides': rides,
			}
			records.append(record)

	return records

def read_rides_as_class(filename):
	'''
	Read the bus ride data as a list of class objects
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			# A class instance
			record = Row(route, date, daytype, rides)
			records.append(record)

	return records

def read_rides_as_named_tuple(filename):
	'''
	Read the bus ride data as a list of named tuples
	'''
	records = []
	Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			# A named tuple
			record = Row(route=route, date=date, daytype=daytype, rides=rides)
			records.append(record)

	return records

def read_rides_as_class_slots(filename):
	'''
	Read the bus ride data as a list of class slots objects
	'''
	records = []
	with open(filename) as f:
		rows = csv.reader(f)
		headings = next(rows)
		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			# A class slots instance
			record = RowWithSlots(route=route, date=date, daytype=daytype, rides=rides)
			records.append(record)

	return records

def measure_memory(fn, filename, label):
	gc.collect()
	tracemalloc.reset_peak()
	tracemalloc.start()
	res = fn(filename)
	current, peak = tracemalloc.get_traced_memory()
	print(f"{label} Memory Use: Current {current}, Peak {peak}")
	tracemalloc.stop()

if __name__ == "__main__":
	measure_memory(read_rides_as_tuples, '../Data/ctabus.csv', "Tuple")
	measure_memory(read_rides_as_dictionary, '../Data/ctabus.csv', "Dictionary")
	measure_memory(read_rides_as_class, '../Data/ctabus.csv', "Class")
	measure_memory(read_rides_as_named_tuple, '../Data/ctabus.csv', "Named Tuple")
	measure_memory(read_rides_as_class_slots, '../Data/ctabus.csv', "Class Slots")

	# Approaches from most memory efficient to least
	# 0. Streaming as 1KB chunks (7KB-33KB)
	# 1. Reading file into a single contiguous string (12-24MB)
	# 2. Reading file into lines (~40MB)
	# 3. Reading file into class instances with __slots__ (~110MB)
	# 4. Reading file into tuples (~114MB)
	# 4. Reading file into named tuples (~119MB)
	# 5. Reading file into class instances (~133MB)
	# 6. Reading file into dictionaries (~179MB)
