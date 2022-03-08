# SecretNumber

Author: Achintya Kumar

Flag: `CTF{f7f9d6f7be55a00}`

## Problem Statement

Neha's teacher puts the answer in the code and makes things a little too easy.
She is given a smart contract which takes 0.1 eth for each guess.
This time Teacher has only stored the hash of the number. Good luck reversing a cryptographic hash!

For the flag,calculate the first 15 characters from hash of the secret number when expressed in words

Ex: 111=onehundredeleven is to be hashed

Flag format: CTF{...}

## Relevant files / links

Link to the smartcontract metadata 
- [contract.sol](https://bafybeie7tsbyzkuvsbpskmm2fm55rhbbkkixghcmmvvudywpgyr3zib2ui.ipfs.dweb.link/)

- [contractInteraction](https://ropsten.etherscan.io/address/0xc4e02bf49a7d07315660557130fca0061106a55e)

## Hint

Take a look at the arguments
0x is appended by ethereum hash calculator

## Solution

It is essentially a cryptographic problem with little bit of blockchain know-how. We need to supply a number which will be hashed to match the hash stored in the contract.

Notice how the number we provide is defined as an uint8 which is just an 8-byte integer. 

We can brute-force all possible 2^8=256 numbers and compute the hash for each one of them and compare it to the smart contract hash

```
const bruteForceHash = (range: number, targetHash: string) => {
  for (let i = 0; i < range; i++) {
    const hash = ethers.utils.keccak256([i]);
    if (targetHash.includes(hash)) return i;
  }
  throw new Error(`No hash found within range ${range}`);
};

const number = bruteForceHash(
  2 ** 8,
  `0xcd12d024c534d7b48c6ae66ced407348a5d6b7187ee786c4ee3ec079dee7aa20`
);
```