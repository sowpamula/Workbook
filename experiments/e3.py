member = input("Add a new member: ")



file = open('downloads/members.txt', 'r')
members = file.readlines()
file.close()

members.append(member)

file = open('downloads/members.txt', 'r')
members = file.writelines()
file.close()