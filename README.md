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
<hr>

### Day 1 :
1. complete till ***Section 3***
	***Section 1 *** : **Introduction**  || *completed*
	***Section 2 *** : **Python Fundamentals** || *completed*
	***Section 3 *** : **Start the Blockchain Application** || *in-completed*
		1. **Lecture 16.** The Blockchain and Block class :
				```command line
					$ mkdir HIRE
					$ touch blockchain.py
					$ touch block.py
				``` 
				note: 
					keep the documentations upto date ( use docstring [comment vs docstring](https://stackoverflow.com/questions/19074745/docstrings-vs-comments) )

		**Highlight:**
		
		1. The blockchain is list of blocks where each block represents a unit of storage for data. The list is called a chain because each block references the block before it, creating (chain) links between between blocks. In a blockchain that supports a cryptocurrency, blocks store transactions.

		2. A python module is a file that contains various Python definitions and statements. For example, the block.py file serves as the block module for the project. The __name__ value in Python reflects the name of the module it's used within, except when the file is directly executed. When a file is directly executed the __name__ value becomes '__main__'.

		3.Mining blocks refers to the process of running a computationally expensive algorithm in order to create new blocks for the blockchain. We'll expand on this in the section on Proof of Work.

		4.The genesis block is the first block in the blockchain. Since all blocks must reference the block that came before it, the genesis block serves as a hardcoded starter block for the chain.

		5.A hashing algorithm generates a unique output for every unique output. In the case of this project, we're using the sha-256 algorithm, which produces a unique 256 character hash in binary, and a 64 character hash in hexadecimal.

		6.Encoding is the process of converting data into a particular format (such as the utf-8 format). For example, encoding a string in utf-8, would produce the equivalent byte string in utf-8 characters. Decoding converts the encoded data back into its original form.

		7.A lambda in python is a function that can be declared inline. In the project so far, we've used it for the map() method which can transform a list into a new list. The map function's first parameter is a lambda, which defines how to transform each item in the original list to produce the new list. 

		### Block.py
		```python
			class Block :
		    def __init__(self, last_hash, data):
		        self.timestamp = self.set_timestamp()
		        self.last_hash = last_hash  
		        self.data = data  
		        self.hash = self.get_hash()  
		        self.__repr__()

		```

		### Blockchain.py

		```python
		class Blockchain :
		    def __init__(self):
		        self.chain = [Block.genesis()]

		    def add_block(self,data) :
		        self.chain.append(Block( self.chain[len(self.chain)-1].hash , data))

		```
                 