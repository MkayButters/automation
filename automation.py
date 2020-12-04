import re

file1 = open("potential-contacts.txt", "wt")



find_email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', file1)
find_email


# (\W*?)(@\W*?)\.(\w{3})
