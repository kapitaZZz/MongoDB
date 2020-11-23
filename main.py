from pymongo import MongoClient
from random import randint
from tokens import url_database as url


class Cluster:
    def __init__(self):
        self.cluster = MongoClient(url)
        self.db = self.cluster['testdata']  # name of your DB
        self.collection = self.db['testcollection']  # name of your collection in DB

    def add_user(self, post):
        '''
        Add new user in DB, and if data exists -> return message
        :param post: add any points in post list for data
        :return:
        '''
        self.name = input('> ')
        self.balance = randint(1, 1000)

        self.post = [
            {
                '_id': 2,
                'name': self.name,
                'balance': self.balance
            },
            {
                '_id': 3,
                'name': self.name,
                'balance': self.balance
            }
        ]
        if self.collection.count_documents({'_id': 2}) == 0 and self.collection.count_documents({'_id': 2}) == 0:
            self.collection.insert_many(post)
        else:
            print('Data has been added')

    def run(self):
        '''
        :return:
        '''
        self.add_user(self.post)

    def find_name(self, ):
        '''
        Find name or any field in DB with _id
        :return:
        '''
        self.number_id = int(input("insert id number > "))
        self.name_output = self.collection.find_one({'_id': self.number_id})['name']
        print(self.name_output)

    def find_balance(self, ):
        '''
        Find balance or any field in DB with _id
        :return:
        '''
        self.number_id = int(input("insert id number > "))
        self.balance_output = self.collection.find_one({'_id': self.number_id})['balance']
        print(self.balance_output)

    def full_data(self, ):
        '''
        Find full data about user in DB with _id
        :return:
        '''
        self.number_id = int(input("insert id number > "))
        self.full_data_output = self.collection.find({'_id': self.number_id})
        for _ in self.full_data_output:
            print(_)

    def update_balance(self):
        '''
        Update any field in DB with _id
        Use another modifier but $set:
            $unset - unset field in DB (use: {'name': 'User'})
            $inc - change current data(int) with + or - (use: {'balance': 1000} or {'balance': -1000})
            $push - add new element in the end of LIST (use: {'items': 'new_item'})
            $pop - delete element from LIST (use 1 to delete last element, or -1 to delete first one)
            $pull - delete specific element in LIST (use: {'key': 'name_element'})
        :return:
        '''
        self.number_id = int(input("insert id number > "))
        self.new_balance = int(input("insert new value > "))
        self.collection.update_one({'_id': self.number_id}, {'$set': {'balance': self.new_balance}})

    def delete_data(self):
        '''
        Delete any field in DB with _id. Use collection.delete_one() to clear DB
        :return:
        '''
        self.number_id = int(input("insert id number for delete data > "))
        self.collection.delete_one({'_id': self.number_id})


claster = Cluster()
claster.update_balance()
