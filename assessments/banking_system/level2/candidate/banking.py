"""
LEVEL 2: Enhanced Banking Features
Build on Level 1 by adding transaction history and account types.

Time Limit: 20-25 minutes
Points: ~150 points

New Requirements (in addition to Level 1):
- Different account types (checking, savings)
- Transaction history with filtering
- Account search and categorization
- Basic interest calculations
"""

import time
from collections import defaultdict


class BankingSystem:
    """
    Enhanced banking system with account types and transaction analysis.
    
    IMPLEMENT ALL LEVEL 1 METHODS PLUS:
    - create_account(self, customer_name, account_type, initial_deposit): Now with account types
    - get_transactions_in_timerange(self, account_number, start_time, end_time): Filter by time
    - search_transactions(self, account_number, query): Search transaction descriptions
    - calculate_interest(self, account_number, annual_rate): Calculate interest for savings
    - get_accounts_by_type(self, account_type): Filter accounts by type
    - get_account_summary(self, account_number): Comprehensive account info
    """
    
    def __init__(self):
        """Initialize the banking system."""
        # TODO: Initialize storage for accounts and transactions
        pass
    
    # =================== LEVEL 1 METHODS ===================
    # Copy your Level 1 implementation here (but enhance create_account)
    
    def create_account(self, customer_name, account_type="checking", initial_deposit=0.0):
        """Create a new account with type."""
        # TODO: Enhance to include account types
        pass
    
    def get_account(self, account_number):
        """Get account information."""
        # TODO: Copy from Level 1
        pass
    
    def deposit(self, account_number, amount):
        """Deposit money to account."""
        # TODO: Copy from Level 1
        pass
    
    def withdraw(self, account_number, amount):
        """Withdraw money from account."""
        # TODO: Copy from Level 1
        pass
    
    def get_balance(self, account_number):
        """Get current account balance."""
        # TODO: Copy from Level 1
        pass
    
    def get_transaction_history(self, account_number):
        """Get transaction history for account."""
        # TODO: Copy from Level 1
        pass
    
    def list_all_accounts(self):
        """Get all accounts."""
        # TODO: Copy from Level 1
        pass
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_transactions_in_timerange(self, account_number, start_time, end_time):
        """
        Get transactions within a time range.
        
        Args:
            account_number (str): Account number
            start_time (float): Start timestamp (inclusive)
            end_time (float): End timestamp (inclusive)
            
        Returns:
            list: List of transactions in the time range
        """
        # TODO: Implement time-based transaction filtering
        pass
    
    def search_transactions(self, account_number, query):
        """
        Search transactions by description.
        
        Args:
            account_number (str): Account number
            query (str): Search query (case-insensitive)
            
        Returns:
            list: List of matching transactions
        """
        # TODO: Implement transaction search
        pass
    
    def calculate_interest(self, account_number, annual_rate=0.02):
        """
        Calculate monthly interest for savings accounts.
        
        Args:
            account_number (str): Account number
            annual_rate (float): Annual interest rate (default 2%)
            
        Returns:
            float: Monthly interest amount, 0.0 if not savings account
        """
        # TODO: Implement interest calculation
        pass
    
    def get_accounts_by_type(self, account_type):
        """
        Get all accounts of a specific type.
        
        Args:
            account_type (str): Account type ("checking" or "savings")
            
        Returns:
            list: List of accounts of the specified type
        """
        # TODO: Implement account type filtering
        pass
    
    def get_account_summary(self, account_number):
        """
        Get comprehensive account summary.
        
        Args:
            account_number (str): Account number
            
        Returns:
            dict: Account summary with statistics, None if not found
        """
        # TODO: Implement account summary
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    bank = BankingSystem()
    print("Level 2: Implement the enhanced banking features!")
