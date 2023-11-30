# Q1. Write 5 examples of a dictionary
# Q2. Using examples, explain how the following methods work:
# - get, update, setdefault, popitem, pop


# Q1. Write 5 examples of a dictionary
studedent_record = {'name': 'muhammad' ,'age' :43 }
books = {'book1': 'accoumting 101'}
people = {'mukhtar': 'person 1' , 'ali':'person2'}
lib = {'lib101':'downfall'}

# Q1. Write 5 examples of a dictionary
# Q2. Using examples, explain how the following methods work:
# - get, update, setdefault, popitem, pop
print(studedent_record.get('name'))
(studedent_record.update({'profession': 'programmer'}))
print(studedent_record)
l = lib.setdefault('lib201', 'pool')
print(l)
studedent_record.popitem()
print(studedent_record)
studedent_record.pop('age')
print(studedent_record)
b = books.keys()
print(b)
b = books.values()
print(b)

yoo = ('key6' , 'key4')
r = 8
zee = dict.fromkeys(yoo , r )
print(zee)