import sys
fna_file = open(sys.argv[1])
contents = fna_file.readlines()
new_list = []
#[contents = '>Pa\n', 'ACGTCCTGAGGGAGAAAGTGGGGGATCTTCGGACCTCACGCTATCAGATGAGCCTAGGTC\n', '>Vc\n', 'AACCTCGCAAGAGCAAAGCAGGGGACCTTCGGGCCTTGCGCTACCGGATATGCCCAGGTG\n']
for i in range(1, len(contents), 2):
    new_list.append(contents[i].strip())
#print(new_list)
#new_list:['ACGTCCTGAGGGAGAAAGTGGGGGATCTTCGGACCTCACGCTATCAGATGAGCCTAGGTC', 'AACCTCGCAAGAGCAAAGCAGGGGACCTTCGGGCCTTGCGCTACCGGATATGCCCAGGTG']
x,y = new_list
print(x)  #ACGTCCTGAGGGAGAAAGTGGGGGATCTTCGGACCTCACGCTATCAGATGAGCCTAGGTC
#print(y) #AACCTCGCAAGAGCAAAGCAGGGGACCTTCGGGCCTTGCGCTACCGGATATGCCCAGGTG
counter = 0
for char in x:
	if char == y[counter]:
		print("|", end = "")
	else:
		print(" ", end = "")
	counter += 1
print()
print(y)
fna_file.close()