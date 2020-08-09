
___ hanoi(n,rod_from,rod_middle,rod_to

	#when n-1 plates are in the final position
	__ n__1:
		print("Plate 1 from %s to %s"%(rod_from,rod_to))
		r_
		
	#moving n-1 plates off the largest one to be able to move that
	hanoi(n-1,rod_from,rod_to,rod_middle)
	#moving the actual largest one
	print("Plate %s from %s to %s"%(n,rod_from,rod_to))
	#placing n-1 plates on the top of the largest one
	hanoi(n-1,rod_middle,rod_from,rod_to)
        
__ __name__ __ "__main__":

	hanoi(3,'A','B','C')