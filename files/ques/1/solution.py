# Use the file name mbox-short.txt as the file name
"""Write a program that prompts for a file name, then opens that file and reads through 
the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute 
the average of those values and produce an output

 Average spam confidence: 0.750718518519
 
 """
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        word = line.split()
        q, number = word
        total += float(number)


average = total/count
print("Average spam confidence:", average, "\n")
