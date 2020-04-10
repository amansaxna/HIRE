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

Important Dependencies: [See requrement.txt]
1. pyhton 3 (Python 3.8.0)
2. pip (pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
3. sudo apt-get install python-virtualenv
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
                 
</details>


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

        ```

        this will create avirtual evnv.
        NOTE::
        	<p>IF error:Error: Command '['/home/fmr/projects/ave/venv/bin/python3.4', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1</p>
        	[resolve ::link](https://stackoverflow.com/questions/24123150/pyvenv-3-4-returned-non-zero-exit-status-1)
        	```
    2. Start the blockchain-env:
    	```console
    	$	source blockchian-env/bin/activate
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
