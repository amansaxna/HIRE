import datetime
import hashlib
import json

class Block :
    """
    Block : a unit storage.
    Store trasactions in a blockchain.
    """
    def __init__(self, last_hash, data):
        self.timestamp = self.set_timestamp()
        self.last_hash = last_hash  
        self.data = data  
        self.hash = self.get_hash()  
        self.__repr__()
        #merkle root :- hash for the block
        # block number :- do we need it?  @chandra: use at blah!
        # do we need to create a mine block

# generic method using static decorator
    @staticmethod
    def genesis() :
        return Block( "0" , "generic")
    
#Generating timestamp
    def set_timestamp(self):
        time =  datetime.datetime.now()
        #print("getting time")#print(self.timestamp)
        return time

#generating hash (timestamp + last_hash +data)
    def get_hash(self):
        dat = (str(self.timestamp) + str(self.last_hash) + str(self.data) )   
        crypt = hashlib.sha256()
        #will print hash object  || encode :: utf8
        crypt.update(dat.encode())       #print(crypt.hexdigest().encode)   print(crypt.digest_size)
        #will print hexa value of the hash object
        return crypt.hexdigest()

#to print formal string of the object ||Called when print(blockchain_instance)::
    def __repr__(self):
        return (
            '\n\nFROM BLOCK.PY Block:-- \n'
            f'Timestamp :{self.timestamp}\n' 
            f'LastHash : {self.last_hash}\n'
            f'Hash : {self.hash}\n' 
            f'DATA : {self.data}'
            )

    #print to string(block_variable)
    #def get(self):
    #    to_string ="FROM BLOCK.PY Block:-- \n Timestamp :{}\n LastHash : {}\n Hash : {}\n DATA : {}"
    #    print(to_string.format(self.timestamp,self.last_hash,self.hash,self.data))

#rough

#b1 = Block.genesis()   
#print(b1)

#b2 = Block( "ax00","aman wnet to the doctor")  
#print(b2)
 
