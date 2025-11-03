# Token backend

# Token backend 

## 💰 ERC20 토큰 구현


> Solidity `^0.8.20` 기반으로 작성되었으며,  
> 토큰의 발행(`mint`)과 소각(`burn`) 기능을 포함한 기본 ERC20 기능을 제공합니다.

---

### Remix - Ethereum IDE 사용

<p align="center">
  <img src="https://github.com/user-attachments/assets/29b87f31-03b6-483a-a7e4-02bf4a4f9f1d" alt="ERC20 Project Preview" width="600">
</p>

### ⚙️ 코드 설명

아래는 토큰 찍기 구현한 코드(`ERC20.sol`)입니다.  


```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract ERC20 {
    mapping(address => uint256) private _balance;
    string private _name;
    string private _symbol;
    uint8 private _decimal;
    address private _owner;
    uint256 private _totalSupply;
    constructor(string memory name_, string memory symbol_, uint8 decimal_) {
        _name = name_;
        _symbol = symbol_;
        _decimal = decimal_;

        _owner = msg.sender;
    }

    function name() view external returns ( string memory ) {
        return _name;
    }

    function symbol() view external returns ( string memory ) {
        return _symbol;
    }

    function decimal() view external returns ( uint8 ) {
        return _decimal;
    }

    function totalSupply() view external returns ( uint256 ) {
        return _totalSupply;
    }

    function balanceOf(address account) view external returns ( uint256 ) {
        return _balance[account]; 
    }

    function transfer(address to, uint256 value) external returns (bool) {
        _balance[msg.sender] = _balance[msg.sender] - value;
        _balance[to] = _balance[to] + value;

        return true;
    }

    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        _balance[from] = _balance[from] - value;
        _balance[to] = _balance[to] + value;

        return true;
    }

    function mint(address account, uint256 value) external {
        require(msg.sender == _owner, "not owner");

        _balance[msg.sender] += value;
        _totalSupply += value;
    }

    function burn(address account, uint256 value) external {
        require(msg.sender == _owner, "not owner");

        _balance[msg.sender] -= value;
        _totalSupply -= value;
    }


}
