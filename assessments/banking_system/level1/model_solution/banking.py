"""
LEVEL 1: Basic Account Management - MODEL SOLUTION
Core account operations and transaction logging.
"""

import time
from collections import defaultdict


class BankingSystem:
    """Basic banking system with account management."""
    
    def __init__(self):
        """Initialize the banking system."""
        self.accounts = {}  # account_number -> account_data
        self.transactions = defaultdict(list)  # account_number -> transaction_list
        self.next_account_number = 1000001
    
    def create_account(self, customer_name, initial_deposit=0.0):
        """Create a new account."""
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        self.accounts[account_number] = {
            'account_number': account_number,
            'customer_name': customer_name,
            'balance': initial_deposit,
            'created_at': time.time()
        }
        
        if initial_deposit > 0:
            self.transactions[account_number].append({
                'type': 'deposit',
                'amount': initial_deposit,
                'timestamp': time.time(),
                'description': 'Initial deposit'
            })
        
        return account_number
    
    def get_account(self, account_number):
        """Get account information."""
        return self.accounts.get(account_number)
    
    def deposit(self, account_number, amount):
        """Deposit money to account."""
        if account_number not in self.accounts or amount <= 0:
            return False
        
        self.accounts[account_number]['balance'] += amount
        self.transactions[account_number].append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': time.time(),
            'description': f'Deposit of ${amount:.2f}'
        })
        
        return True
    
    def withdraw(self, account_number, amount):
        """Withdraw money from account."""
        if account_number not in self.accounts or amount <= 0:
            return False
        
        if self.accounts[account_number]['balance'] < amount:
            return False  # Insufficient funds
        
        self.accounts[account_number]['balance'] -= amount
        self.transactions[account_number].append({
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': time.time(),
            'description': f'Withdrawal of ${amount:.2f}'
        })
        
        return True
    
    def get_balance(self, account_number):
        """Get current account balance."""
        account = self.accounts.get(account_number)
        return account['balance'] if account else None
    
    def get_transaction_history(self, account_number):
        """Get transaction history for account."""
        return self.transactions.get(account_number, [])
    
    def list_all_accounts(self):
        """Get all accounts."""
        return list(self.accounts.values())
