temp_file = open ("tempt.txt","w")
print ("first line", file = temp_file)
print ("second_line", file=temp_file)
temp_file.close()
