names = [{'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Molly'},
        {'id': 3, 'name': 'Jane'}]

# array of names
# array of names with begins with J

class MyMagic:
    def __init__(self, list_of_users):
        self.database = list_of_users

    def names_as_list(self):
        return list(map(lambda db : db['name'], self.database))

    def names_start_with_j(self):
        # return list(filter(lambda name : name[0] == 'J', self.names_as_list())) # name[0] - nem szep!!!
        return list(filter(lambda name : name.startswith('J'), self.names_as_list()))
