import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block import Block

pnconfig = PNConfiguration()
# subscribe_key from admin panel
pnconfig.subscribe_key = "sub-c-12acc292-856b-11ea-b883-d2d532c9a1bf"
# publish_key from admin panel (only required if publishing)
pnconfig.publish_key = "pub-c-e033f608-3f95-4206-b117-a51ce9de9287"

CHANNELS =  {   'TEST':'TEST',  'BLOCK':'BLOCK' }

class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def message(self,pubnub,message_object):
        print(f'\n--channe:{message_object.channel}|message{message_object.message}')
        if  message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)
            try:
                self.blockchain.replace_chain(potential_chain)
                print(f'\n Succesfully replaced the locla chain ')
            except Exception as e:
                print(f'\n Did not replace :{e}')


class PubSub():
    """
    Handles the publisher/subscriber layer of the application
    it prvides the communication b/w the nhe nodes of the network
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        #This function causes the client to create an open TCP socket to the PubNub Real-Time
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

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

def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'],{'foo':'bar'})    

if __name__ == "__main__":
    main()