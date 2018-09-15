# Bank

This challenge consists of using Python json, time, math, and unittest libraries along with the flask framework to create a simple Banking program.

## Description

`v0.0.5`

## Personal user information will have following structure
 
```json
{
  "id": 1,
  "first_name": "Tera",
  "last_name": "Gong",
  "email": "tgong0@uiuc.edu",
  "password" : "qwerty12345",
  "dob": "3/27/1995",
  "gender": "F",
  "opened": "3/27/2012"
}
```
and an edit function
## Accounts will have the following structure

This class will hold account information.

- balance
- account_number
- user
- pin
- transactions[]


```json
{

}
```

This class will perform following actions.

- update_account()
- view_transactions()
- view_account()
- equals()
- deposit()
- withdraw()

- get_account_number()
- get_balance()
- get_pin()
- get_user()

- set_account_number()
- set_balance()
- set_pin()
- set_user()

Accounts types:
- CHEKING
- SAVINGS
- GIC
- JOINT
- CREDIT

## The user will have the following structure:
### members
- accounts[]
- Id
### functions
- search_account()
- merge_account()

## The card will have the following structure
- pin
- Type (of card)


## This class will hold transaction information

### members
- balance
- account_number_from
- account_number_to
- transaction_id

###  functions
- view_transaction()

- get_account_number_from()
- get_account_number_to()
- get_balance()
- get_transaction_id()

- set_account_number_from()
- set_account_number_to()
- set_balance()
- set_transaction_id()

## Solution Capture

Coming soon...

```json``` ```time``` ```math``` ```unittest``` ```colorama``` ```flask```
