import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool


pnconfig = PNConfiguration()
# subscribe_key from admin panel
pnconfig.subscribe_key = "sub-c-12acc292-856b-11ea-b883-d2d532c9a1bf"
# publish_key from admin panel (only required if publishing)
pnconfig.publish_key = "pub-c-e033f608-3f95-4206-b117-a51ce9de9287"

CHANNELS =  {   'TEST':'TEST',  'BLOCK':'BLOCK' , 'TRANSACTION' : 'TRANSACTION'}

class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self,pubnub,message_object):
        print(f'\n--channe:{message_object.channel}|message{message_object.message}')
        
        if  message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)
            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                    self.blockchain
                )
                print(f'\n Succesfully replaced the locla chain ')
            except Exception as e:
                print(f'\n Did not replace :{e}')
        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)
            print('\n -- Set the transaction in the transaction pool')
            


class PubSub():
    """
    Handles the publisher/subscriber layer of the application
    it prvides the communication b/w the nhe nodes of the network
    """
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        #This function causes the client to create an open TCP socket to the PubNub Real-Time
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self,channel,message):
        """
        publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self,block):
        """
        Broadcast a block object to all nodes
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())
    
    def broadcast_transaction(self,transaction):
        """
        Broadcast a transaction to all nodes
        """
        self.publish(CHANNELS['TRANSACTION'],transaction.to_json())

def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'],{'foo':'bar'})    

if __name__ == "__main__":
    main()