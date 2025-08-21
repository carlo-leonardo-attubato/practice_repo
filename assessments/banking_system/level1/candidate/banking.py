"""
LEVEL 1: Basic Account Management
Implement core banking operations.

Time Limit: 15-20 minutes
Points: ~100 points

Requirements:
- Create accounts with unique account numbers
- Deposit and withdraw funds
- Check account balances
- Basic transaction logging
"""

from collections import defaultdict


class BankingSystem:
    """
    Basic banking system with account management.
    
    IMPLEMENT THESE METHODS:
    - __init__(self): Initialize the banking system
    - create_account(self, customer_name, initial_deposit): Create new account
    - get_account(self, account_number): Get account information
    - deposit(self, account_number, amount): Deposit funds
    - withdraw(self, account_number, amount): Withdraw funds
    - get_balance(self, account_number): Get current balance
    - get_transaction_history(self, account_number): Get all transactions
    - list_all_accounts(self): Get all accounts
    """
    
    def __init__(self):
        """Initialize the banking system."""
        # TODO: Initialize storage for accounts and transactions
        pass
    
    def create_account(self, customer_name, initial_deposit=0.0):
        """
        Create a new account.
        
        Args:
            customer_name (str): Name of the account holder
            initial_deposit (float): Initial deposit amount
            
        Returns:
            str: Account number if successful, None if failed
        """
        # TODO: Implement account creation
        pass
    
    def get_account(self, account_number):
        """
        Get account information.
        
        Args:
            account_number (str): Account number
            
        Returns:
            dict: Account data if found, None if not found
        """
        # TODO: Implement account retrieval
        pass
    
    def deposit(self, account_number, amount):
        """
        Deposit money to account.
        
        Args:
            account_number (str): Account number
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False if failed
        """
        # TODO: Implement deposit operation
        pass
    
    def withdraw(self, account_number, amount):
        """
        Withdraw money from account.
        
        Args:
            account_number (str): Account number
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False if insufficient funds
        """
        # TODO: Implement withdrawal operation
        pass
    
    def get_balance(self, account_number):
        """
        Get current account balance.
        
        Args:
            account_number (str): Account number
            
        Returns:
            float: Current balance, None if account not found
        """
        # TODO: Implement balance retrieval
        pass
    
    def get_transaction_history(self, account_number):
        """
        Get transaction history for account.
        
        Args:
            account_number (str): Account number
            
        Returns:
            list: List of transactions, empty if account not found
        """
        # TODO: Implement transaction history retrieval
        pass
    
    def list_all_accounts(self):
        """
        Get all accounts.
        
        Returns:
            list: List of all account data
        """
        # TODO: Implement account listing
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    bank = BankingSystem()
    print("Level 1: Implement the BankingSystem class methods!")
