# cs-security-and-blockchains

Under the tutelage of Jonathan Lawrence.

## Notebooks
Merkle trees: https://colab.research.google.com/drive/1DfhYYL0dBYfWPLx-1yq4wpYg0cyjBCg8?usp=sharing

## Week 7
Polymarket-style smart contract that implements a decentralized exchange
`ConditionalTokens.sol` - I have it all set up in remix with a showcase but the imports won't work unless you open remix and clone openzeppelin's contracts and put this file in the same directory as ERC1155.sol and also put CTHelpers.sol there. I modified ConditionalTokens.sol from this repo: https://github.com/gnosis/conditional-tokens-contracts/tree/master/contracts.

post tute analysis: this contract is a contrived example to show AMMs and Conditional tokens in the same contract but it doesn't make sense in a real usecase because the CTF (conditional token framework) should be in a separate contract to the AMM because of modularity and gas efficiency.

## Week 6 - How Etheruem chooses who votes
- [x] cool visualization like with Cardano - https://beaconcha.in/
- [x] show current randao_reveal and block proposer
