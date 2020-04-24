import uuid
import time
from backend.wallet.wallet import Wallet
class Transaction:
    """
    Document of an exchange in currency from a sender to one or more recipients.
    """
    def __init__(
        self, 
        sender_wallet=None, 
        recipient=None, 
        amount=None,
        id=None,
        output=None,
        input=None
        ):
        self.id = id or str(uuid.uuid4())[0:8]
        self.output = output or self.create_output(
            sender_wallet,
            recipient,
            amount
        )
        self.input = input or self.create_input(sender_wallet, self.output)
    
    def create_output(self,sender_wallet,recipient,amount):
        """
        Structure the output data for the transaction
        """
        if amount > sender_wallet.balance:
            raise Exception('Amount exceeds Balance')

        output = {} #dict
        output[recipient] = amount
        output[sender_wallet.address] = sender_wallet.balance - amount

        print(output)
        return output

    def create_input(self,sender_wallet,output):
        """
        Structure the input data for the transaction
        Sign the transaction and include 
        public key and address :- public key will help other peers to varify the transaction
        """
        return {
            'timestamp': time.time(),
            'amount': sender_wallet.balance,
            'address' :  sender_wallet.address,
            'public_key' : sender_wallet.public_key,
            'signature' : sender_wallet.sign(output)
        }
    
    def update(self, sender_wallet,recipient,amount):
        """
        Update th etransaction with an existing or new recipient
        """
        if amount > self.output[sender_wallet.address]:
                raise Exception('Amount exceeds Balance')

        if recipient in self.output: #if in output add the rest amount
            self.output[recipient] = self.output[recipient] +amount
        else:  #if not in recipient , add the recipient
            self.output[recipient] = amount
        
        self.output[sender_wallet.address] = \
            self.output[sender_wallet.address] - amount

        self.input = self.create_input(sender_wallet,self.output)

    def to_json(self):
        """
        serialze the transactions
        """
        return self.__dict__

    @staticmethod
    def from_json(transaction_json):
        """
        Deserialize a transaction's json representation back into a
        Transaction Instance
        """
        return Transaction(
            id = transaction_json['id'],
            output = transaction_json['output'],
            input = transaction_json['input']
        )


    @staticmethod
    def is_valid_transaction(transaction):
        """
        Validate a transaction.
        Raise an exception for invalid transactions.
        """
        output_total = sum(transaction.output.values())

        if transaction.input['amount'] != output_total:
            raise Exception('Invalid transaction output values')

        if not Wallet.verify(
            transaction.input['public_key'],
            transaction.output,
            transaction.input['signature']
        ):
            raise Exception('Invalid signature')


def main():
    """
    (sender's wallet, recipient's wallet)
    """
    transaction =Transaction(Wallet(),'recipient',15)
    print(f'transaction.__dict__{transaction.__dict__}')

    transaction_json = transaction.to_json()
    restored_transaction = Transaction.from_json(transaction_json)
    print(f'restored_transaction.__dict__{restored_transaction.__dict__}')

if __name__ == "__main__":
    main() 
