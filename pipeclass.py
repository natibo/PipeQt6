#!/usr/bin/env python3


class Pipe:

    def __init__(self, name='', maker='', shape='', store='', buyyear=''):
        self.name = name
        self.maker = maker
        self.shape = shape
        self.store = store
        self.buyyear = buyyear
        
    def create_Pipe(self):
        name = self.name.text()
        age = self.maker.text()
        address = self.shape.text()
        email = self.store.text()
        phone = self.buyyear.text()

        pipex = Pipe(name, age, address, email, phone)
