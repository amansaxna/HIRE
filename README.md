# H.I.R.E
## Healthcare Information Records & Exchange
### Building a blockchain  with Python, JavaScript, and React
Learning from : 
1. Course link :
	[udemy course link](https://www.udemy.com/course/python-js-react-blockchain/learn/lecture/16601462#overview) 
2. .md(MARKDOWN) link :
	[cheat sheet link](https://www.udemy.com/course/python-js-react-blockchain/learn/lecture/16601462#overview)
3. Git link :
	[Referesnce list]()
4. pubnub link:
	https://www.pubnub.com/docs/python/api-reference-publish-and-subscribe

Important Dependencies: [See requrement.txt]
1. pyhton 3 (Python 3.8.0)
2. pip (pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
3. sudo pip3 install virtualenv
<hr>

<details><summary>Day 1 :</summary><br>
1. complete till ***Section 3*** :<br>
	***Section 1 *** : **Introduction**  || *completed* <br>
	***Section 2 *** : **Python Fundamentals** || *completed* <br>
	***Section 3 *** : **Start the Blockchain Application** || *in-completed* <br>
  
  1.  **Lecture 16.** The Blockchain and Block class :
				```
				$ mkdir HIRE
				$ touch blockchain.py
				$ touch block.py
				``` <br>
  
	  note: 
					keep the documentations upto date ( use docstring [comment vs docstring](https://stackoverflow.com/questions/19074745/docstrings-vs-comments) )

**Highlight:**
	1. The blockchain is list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between between blocks. In a blockchain that supports a cryptocurrency, blocks store transactions.
	2. A python module is a file that contains various Python definitions and statements. For example, the block.py file serves as the block module for the project. The __name__ value in Python reflects the name of the module it's used within, except when the file is directly executed. When a file is directly executed the __name__ value becomes '__main__'.
	3. Mining blocks refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. We'll expand on this in the section on Proof of Work.
	4. The genesis block is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain.
	5. A hashing algorithm generates a unique output for every unique output. In the case of this project, we're using the sha-256 algorithm, which produces a unique 256 character hash in binary, and a 64 character hash in hexadecimal.
	6. Encoding is the process of converting data into a particular format (such as the utf-8 format). For example, encoding a string in utf-8, would produce the equivalent byte string in utf-8 characters. Decoding converts the encoded data back into its original form.
	7. A lambda in python is a function that can be declared inline. In the project so far, we've used it for the map() method which can transform a list into a new list. The map function's first parameter is a lambda, which defines how to transform each item in the original list to produce the new list. 

</details>
**Block.py**

```python
GENESIS_DATA = {
    'last_hash': 0 ,
    'data':'genesis'
    }

class Block :
	def __init__(self, last_hash, data):
		self.timestamp = self.set_timestamp()
		self.last_hash = last_hash  
		self.data = data  
		self.hash = self.get_hash()  
	def genesis() :
	def get_timestamp(self):
	def get_hash(self):
 ```
 
**Blockchain.py**
```python
  
		class Blockchain :
		    def __init__(self):
		        self.chain = [Block.genesis()]

		    def add_block(self,data) :
		        self.chain.append(Block( self.chain[len(self.chain)-1].hash , data))

```
                
<details><summary>Day 2 :</summary><br>
	
1. complete till ***Section 6*** :<br>
	***Section 4 *** : ** Test the Application**  || *in-completed* <br>
	***Section 5 *** : **Proof of work** || *in-completed* <br>
	***Section 6 *** : **Preparing the Blockchain for Collaboration** || *in-completed* <br>

### Section 4

<details><summary>4 :</summary><br>

```bash

  pip3 search pytest(5.2.1)

```

  Steps::
  	1. create a ***virtual envirnment*** for the current project
```bash
python3 -m venv blockchain-env
!or
virtualenv -p python3 HIRE-env
```

        this will create avirtual evnv.
        NOTE::
        	<p>IF error:Error: Command '['/home/fmr/projects/ave/venv/bin/python3.4', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1</p>
        	[resolve ::link](https://stackoverflow.com/questions/24123150/pyvenv-3-4-returned-non-zero-exit-status-1)
        	```
    2. Start the blockchain-env:
    	```console
    	$	source blockchian-env/bin/activate
		!or
		. HIRE-env/bin/activate

    	```
		[ERROR-Window] 
    	TO CHECK whether you are in the virtual env use::
    	```CONSOLE
    	$	echo $VIRTUAL_ENV
    	``` this will print the path
3. Install pytest (5.1.2)
```
$	pip3 install pytest==5.1.2
``` 
4. Automate the dependency donload using **requirement.txt**
5. execute the package using ::
```bash
!this will call the module backend then blockchian
python3 -m backend.blockchain.blockchain
```

6. create a tests file --> test_block.py , test_blockchain.py

7. run the tests

```bash

python3 -m pytest backend/tests

```

**Hilights :**

1. A virtual environment allows you to create an isolated space where your project (or a group of projects) can install its external packages. This is especially helpful when you're managing multiple projects on your machine. Often, external packages update their classes and methods when new versions are released. However, separate virtual environments can have different versions of the same package installed - that way, each project can rely on the versions of their dependencies to stay consistent.
2. A package in python allows you to group together related modules. To create a package, create a directory with an __init__.py file. Python will then recognize the directory as a package, allowing you to import modules contained in that package with a dot syntax. For example, the blockchain/ directory contains both __init__.py and block.py. This allows other files to import the block module with blockchain.block.
3. The general approach to tests is to create a series of assert statements that verify whether or not a value is equal to some other value.

</details>


### SECTION 5 :

<details><summary>5:</summary><br>

**Steps**::
1. 


</details>
</details>


### Day 3:Blockchain network

<details><summary>6:</summary><br>
1. set up flask::
```bash

pip3 install Flask==1.1.1
# to check every present modules on the v-env
```bash
pip3 freeze

```
Add "Flask==1.1.1" in requiements.txt

to run flask (in development mode):
```bash

export FLASK_ENV=development
python3 -m backend.app

```
development mode allows the server to restart whenever there is a change in the code

2. Set up PUBNUB
***https://www.pubnub.com/developers/tech/key-concepts/publish-subscribe/**
**https://www.pubnub.com/docs/python/api-reference-configuration**

1. create a new app over the website https://www.pubnub.com/

2. install pubnub
```bash
pip3 install pubnub==4.1.6
```
update the requirements

3. to set envirnment variable on the bash
```
export PEER = True && python3 -m backend.app
#try set as a replacement on windows 10
#to run the pubsub
pyhton3 -m backend.pubsub
```
https://superuser.com/questions/1500272/equivalent-of-export-command-in-windows

4.	install requests -> Synchronize a peer at startup
```bash
pip3 install requests==2.22.0
```
**Summary**
	An API, or Application Programming Interface is a medium that allows external parties to call code within an existing system.

	HTTP stands for hypertext transfer protocol - and http allows allows you to fetch resources over the web. For example, a GET http request is associated with reading data from an API. A POST http request is associated with sending data to the API.

	Flask is a widely used python module that helps build web servers.

	JSON, which stands for JavaScript Object Notation, is a format for structuring data that is commonly used for sharing objects over the web. Even though the name includes JavaScript, it's actually supported by multiple languages. This makes it a great format to use for sending objects across applications - for example, from a backend server, to a frontend web application.

	The publisher/subscriber pattern, or pub/sub for short, is a networking pattern that exposes various communication channels. Publishers broadcast messages on those channels. And subscribers receive messages on those channels.

	Serialization is the process of converting a complex custom object into a simpler format that can be shared across the web, or perhaps stored in a database more easily. Most often, the end result of serialization is a string representation of the original object. Deserialization would then take the string representation, and convert it back to the complex custom object.


</details>
<details><summary>8: Adding cryptocurrency</summary><br>
1. digital Wallets
2. Signatures and Verification
3. Transactions

## Wallets:
1. use uuid module for adrress of the wallet
2. use cryptogrophy module for encryption
```bash
pip3 install cryptography==2.7
```
To run the wallet module
```bash
python3 -m backend.wallet.wallet
```
3. creare methods for creating signatures, verifying it
4. **test file :: not created**
5. Create transactions , various operations :: validate, update , create

## transaction.py

```python
class Transaction:
	#sender_wallet :: so as to make use of the wallet's object attributes such as keys..  
	#recipient :: wallet's address string
	#amount  :: how much currency to exchange
```
To run the wtransaction module
```bash
python3 -m backend.wallet.transaction

```
***summary***
	A wallet keeps track of an individual's amount of currency. Each wallet has an address, and a pair of keys (a private and a public key).

	The private key of a wallet must be kept secret. It's used to generate signatures (see signatures below) on behalf of the wallet owner for based on objects of data. For example, a wallet owner will sign a generated transaction to make it official.

	The public key is the other half of the keypair, and it can be publicly shared with other entities.

	Signatures are unique data objects created using the private key of keypair and an original data object to sign. With the signature, public key, and the original data object, other entities can verify if the signature was generated by the true owner of the public key.

	ECDSA stands for elliptic cryptography digital signature algorithm, and it's the underlying implementation of the cryptography python module used in the project. The mathematics behind the system use elliptic curves to create keypairs and signatures.

	A transaction consists of an input and output field. The input contains metadata, including the address, public key, and the balance amount of the sender. The input also includes a signature that's generated by the sender, using the transaction output as the underlying data. The output contains a series of entries where recipient addresses will receive certain amounts as a result of the transaction. The transaction can have any number of recipients. At least one of the recipients is the sender address itself, because this details how much currency the sender should have after the transaction is completed.

	Validating transactions involves checking that the total currency sent to the recipients is correct, and that the signature is correct according to the presented public key and transaction output.
</details>

<details><summary>9:Transactions on the network</summary><br>

**GOALS**
1. Create an API method that will allow the application owner to create transaction
2. And also, these transactions shouls be published in the network(serialize and deserialize the transactions)

#### Steps

1. Download postman :: use chrome pugin
2. create a POST request method for transactions

```bash
@app.route('/wallet/transact',methods= ['post'])
#{'recipient' :'foo', 'amount' :15}
```
3. restructure the wallet object to json format
4. USE POSTMAN ::
	1. POST :: http://127.0.0.1:5000/wallet/transact
	2. set Body -> SELECT RAW -> Select json
	3. set POST data -> 

```json
{
	"recipient": "foo",
	"amount": 15
}
```
	4. send
<br>

5. **transaction pool**
Collects all the transaction created in the network
should do ::

1. unique set of transaction object
2. update existing stored transaction when there is an update
3. Rewrite multiple transaction
	
6. broadcast the pool

**SUMMARY**
	The new /wallet/transact endpoint is the first POST request of the API. A POST request allows the requester to send data to the application, for methods that usually create new objects.

	Serializing the wallet's public key took a more complex approach since the public key byte string is not in the utf-8 encoding. Instead, the public key's default format is in an encoding format called PEM, that's defined within the cryptography module. But by encoding and decoding the public key using this format, a public key can be shared across the network, and restored back into a rich public key object when it comes to validating signatures.

	The transaction pool is an object that collects transactions that have been broadcasted across the network. It stores transactions according to their id. The idea is that this transaction pool will collect the transactions that miners will use as the basis of data for new blocks.

	Truthy values in Python act like True when placed in a boolean context. Any value that is not falsy (values that like False in a boolean context) is truthy. So it's important to know what values are falsy: None, 0, the empty string, or any empty collection, like an empty list or dictionary.
</details>

<details><summary>10:Connecting modules</summary><br>
Connect the Blockchain and Cryptocurrency

1. Mine Transaction
2. Wallet Balance
3. Mining Reward

python3 -m backend.scripts.test_app

</detail>

### FRONTEND :
1. REACT JS
2. REACT HOOK

Install
1. nodejs(v12.14.0) ::  https://nodejs.org/en/download/
2. npm(6.13.4)
3. npx(6.13.4)

**Steps** :<br>
1. Initialize react app
```bash

npx create-react-app frontend
```
2. update the .html and .css files
3. start the app
```bash
HIRE/frontend$ npm run start
```
3. set CORS polocies{important}to allow the access
	a. Way 1:
 		https://chrome.google.com/webstore/detail/moesif-orign-cors-changer/digfbfaphojjndkpccljibejjbppifbc?hl=en
		Easily add (Access-Control-Allow-Origin: *) rule to the response header.
		Allow CORS: Access-Control-Allow-Origin lets you easily perform cross-domain Ajax requests in web applications.

		Simply activate the add-on and perform the request. CORS or Cross Origin Resource Sharing is blocked in modern browsers by default (in JavaScript APIs). Installing this add-on will allow you to unblock this feature. Please note that, when the add-on is added to your browser, it is in-active by default (toolbar icon is grey C letter). If you want to activate the add-on, please press on the toolbar icon once. The icon will turn to orange C letter.

	b. way 2:
	Install Flask-Cors
```bash
pip3 install Flask-Cors==3.0.8
``` 

<details><summary>10:Connecting modules</summary><br>

## test_block.py 

```python
def test_block():
    last_block = Block.genesis()
    data = 'tets-data'
    new_block = Block(last_block.hash,data)

    assert isinstance(last_block, Block)
    assert new_block.data == data
    assert new_block.last_hash == last_block.hash

def test_genesis():
    genesis = Block.genesis()
    assert isinstance(genesis, Block)
    assert genesis.last_hash == GENESIS_DATA['last_hash']
    assert genesis.data == GENESIS_DATA['data']
```

## test_blockchain.py 

```python
def test_blockchain_instance():
    blockchain =Blockchain()
    assert blockchain.chain[0].data == GENESIS_DATA['data']

def test_add_block():
    blockchain =Blockchain()
    data = "test data"
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data
    assert blockchain.chain[-2].hash == blockchain.chain[-1].last_hash
```

### Activate the virtual envirnment

```bash

source HIRE-env/bin/ativate
. HIRE-env/bin/activate

```

### Install all packages

```bash

pip3 install -r requirements.txt

```

### Run the tests

Make sure to activate the virtual environment.

```bash

pyhton3 -m pytest backend/test

```
### Run the application and the API

```bash

pyhton3 -m backend.app

```

### Run a peer instance

```bash
export PEER = True && python3 -m backend.app
```

### Run a front end

```bash
HIRE/frontend$ npm run start
```
https://github.com/gatsbyjs/gatsby/issues/11406