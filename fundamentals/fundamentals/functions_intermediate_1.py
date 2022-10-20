
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ]
x[1][1]=15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'}, {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print (students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
#  list syn var name : mylist=[], elementet e listes aksesohen me index, indexi nis nga 0 
# dictionary syn  var name : mydictionary={
#   'key': value
# } elemente e dictionary aksesohen me key 
z[0]['y']= 30
print(z)


