import uuid
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import ( encode_dss_signature, decode_dss_signature) #digital signature standard
from cryptography.hazmat.primitives import hashes #sha256
from cryptography.hazmat.primitives import serialization #helps in specifying the endoding
from cryptography.exceptions import InvalidSignature
from backend.config import STARTING_BALANCE

class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of hte miner's balance.
    Allows a miner to  authorize transactions
    """
    def __init__(self):
        self.address =  str(uuid.uuid4())[0:8]
        self.balance = STARTING_BALANCE
        self.private_key = ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.serialize_public_key()

    def sign(self,data):
        """
        Generate a signature based on the data using the local prv. key
        """
        #Eleptic crypography digital signatutre algo
        # decode_dss_signature returns a tuple
        return decode_dss_signature(self.private_key.sign(
            json.dumps(data).encode('utf-8'), 
            ec.ECDSA(hashes.SHA256())
        ))

    def serialize_public_key(self):
        """
        Rest the public key to its serialized version. 
        """
        self.public_key_bytes =\
        self.public_key.public_bytes(
            encoding= serialization.Encoding.PEM, #converts objs to byte string format in PEM format
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        #print(f'self.public_key_bytes: {self.public_key_bytes}')

        decoded_public_key = self.public_key_bytes.decode('utf-8')
        self.public_key = decoded_public_key
        # this will create error ::public_key.verify(
        #    AttributeError: 'str' object has no attribute 'verify'
        #print(f'\nself.public_key: {self.public_key}')
        #print(f'\n decoded_public_key: {decoded_public_key}')

    @staticmethod
    def verify(public_key,data,signature):
        """
        Verify a signature based on the original public key and data
        """
        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        #print(f'\n signature : {signature}\n')
        (r,s) = signature
        
        try:
            deserialized_public_key.verify(
                encode_dss_signature(r,s),
                #signature.encode('utf-8'),
                json.dumps(data).encode('utf-8'), 
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature : #import InvalidSignature
            return False

def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')

    data = {'foo': 'bar'}

    signature = wallet.sign(data)
    print(f'signature:{signature}')

    should_be_valid = wallet.verify(wallet.public_key,data,signature)
    print(f'should_be_valid:{should_be_valid}')

    should_be_invalid = wallet.verify(Wallet().public_key,data,signature)
    print(f'should_be_invalid:{should_be_invalid}')


if __name__ == '__main__':
    main()