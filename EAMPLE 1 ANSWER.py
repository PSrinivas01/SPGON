input_string=input()[::-1]
output_list=[]
for each_char in input_string:
    a=ord(each_char)
    output_list.append(chr(a+1))
output_string="".join(output_list)
print(output_string)