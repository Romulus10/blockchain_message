.. blockchain_message documentation master file, created by
   sphinx-quickstart on Wed May  9 10:05:31 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to blockchain_message's documentation!
==============================================

The Ethereum network has attracted a considerable volume of attention in
recent months for its native currency, Ether. During the
cryptocurrency bubble beginning in early 2017 and apparently ending
nearly a year later the value of Ether skyrocketed from just a few
dollars to over a thousand dollars. It attracted a staggering number of
investors hoping to make a fortune speculating on the value of Ether,
Bitcoin, and other currencies. Now that the prices have leveled off, the
noise has died down somewhat, but is Ethereum's usefulness over?
Ethereum itself was never intended as an investment vehicle. Ether was
originally conceived of as a way to handle time-sharing on a distributed
computing platform. The Ethereum Virtual Machine itself was designed as
a sort of "world computer" which can be used to distribute and run
theoretically any program that can be conceived of. People deploying
their distributed applications to the EVM or requesting processing time
from one of those applications pay a gas fee which sets an upper limit on the
amount of time an operation can take on the machine. My
intention is to build a client/server-analog which uses the Ethereum
virtual machine and blockchain as the middleware and backend of an
email-type service.


Since email, instant messaging, and SMS are all commonplace in
technology this project may seem to simply reinvent the wheel. These
services, though all practical and convenient, tend to be held by a
particular group of companies or entities. Content sent between two
participants in a conversation are not sent directly from person to
person; there must be some intermediary to handle delivery. This project
will take advantage of the transaction structure of the blockchain and
use Ethereum as the delivery and storage system. By committing messages
to Ethereum, the ownership and control of the content a party is sending
is maintained by the holder of the private keys for the origination of
transactions and for the decryption of messages sent to the chain.


Consider two conversation partners, Alice and Bob. Bob sends a text
message to Alice, which is sent from his device to his carrier. It is
relayed through cell towers and data centers, stopping along the way in
some unknown number of locations and being saved. Finally it will
eventually be delivered, not by the device itself but by the combination
of cell carriers, to Alice. There is no promise of security, privacy, or
control over the data being sent between endpoints. A message delivery
service built on Ethereum would, by nature, circumvent these concerns.
Everything occurring on the Ethereum virtual machine is committed to the
blockchain. This occurs by distributing every transaction
to every computer running a copy of the core Ethereum software. Because
every node has a
copy of that action, it is by definition decentralized. Each transaction
is also associated with a pair of public keys (called addresses in
cryptocurrency), which allows them to prove their origin and
destination. As the chain is processed by a number of computers (called
miners) tasked with validating and verifying the integrity of the
chain, each miner checks to make sure that every one of
these transactions, and the metadata associated with them, is completely
correct in relation to the rest of the
blockchain.
This allows us to be absolutely certain that every message that this
application sends or receives is immutably and provably
present.

On the technical end, this project will ostensibly consist of a database
module which will allow us to store content client-side, a
cryptographical module using GPG, and a blockchain module which will
allow us to communciate directly with a local version of Ethereum
through web3. These functions will all be internal, with a set of
functions exposed to the end-user for interacting with the project as a
library.


I intend for this project to be a proof-of-concept library written in
Python. It will require a Python version greater than 3.6, as well as
the web3
implementation for Python. For testing purposes it will also
require a test RPC installed locally in order to test and
debug the smart contracts associated with the application. This
smart contract will require a Solidity compiler to be installed in order
to produce the compiled bytecode for the contract. In order to maintain
the privacy of the messages sent to the blockchain, the library will
make direct use of GNU Privacy Guard and RSA keypairs to send encrypted
messages between users. The test RPC I plan on using (Ganache) will
require that the latest version of Node.js installed on the local
system. The process of deploying the contract and interacting with it
will be handled entirely by Python scripts, and in order to deploy the
contract to the Ethereum mainnet an RPC pointed at the Ethereum
Foundation's official blockchain will be necessary. All of these may be
easily installed on most operating systems.


Given the time available to me, I am confident that I can implement the
core functionality of the client. The database and cryptographical
modules will be comparatively simple to implement. I am anticipating
that the actual process of writing the smart contract to handle
transaction processing will be the largest challenge. In terms of goals
I would like to reach but which may be more challenging, the current
project uses a full local Ethereum node to communicate with the network.
The storage requirement for a full node is O(n) where n is the number of
transactions in the blockchain. This is impractical for devices with
smaller available storage, so the implementation of a light client (with storage requirement O(log(n)))
integrated into the system would simplify setup and reduce resource
usage considerably. I also hope to implement an efficient enough smart
contract to optimize the gas usage of the system and thereby retain
reasonable transaction fees for users of the service.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
