adress="1.1.1.1"
my_list=adress.split(".")
output=adress.replace(".","[.]")

final=" ".join(output)
print(my_list)
print(output)
print(final)