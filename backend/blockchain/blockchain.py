from backend.blockchain.block import Block
import datetime

class Blockchain :
    """

    Blockchain: a public ledger of transactions.
    implemented as a list of block - data sets of transaction
    """
    def __init__(self):
        self.chain = [Block.genesis()]
        print("length of the chain :"+ str(len(self.chain)))

    def add_block(self,data) :
        self.chain.append(Block( self.chain[len(self.chain)-1].hash , data))
        print("length of the chain :"+ str(len(self.chain)))
    
    #to print formal string of the object ||Called when print(blockchain_instance)::
    def __repr__(self):
        return f'Blockchain: {self.chain}'

    #    
    #def get(self):
    #    for i in self.chain:
    #        to_string = "Block\n Timestamp :{}\n LastHash : {}\n Hash : {}\n DATA : {}"
            # check  for prnt(f"sdjvb,fjkb{i.shv}")
     #       print(to_string.format(i.timestamp, i.lastHash , i.hash , i.data))
            
    #create blkchain validation to eleminate forks 
    #isValidChain(chain) 
    #replaceChain(newChain)
    #

#rough
b1 = Blockchain()
b1.add_block("lofo")
b1.add_block("kofo")
#print(b1)


