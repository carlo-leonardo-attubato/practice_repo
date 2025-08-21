"""
LEVEL 3: Advanced Banking Logic
Build on Level 2 by adding complex financial operations and validation.

Time Limit: 30-40 minutes
Points: ~250 points (FOCUS HERE - MOST POINTS!)

New Requirements (in addition to Level 1-2):
- Overdraft protection and fees
- Transfers between accounts
- Account freezing/unfreezing
- Fraud detection patterns
- Scheduled transfers
"""

import time
from collections import defaultdict


class BankingSystem:
    """
    Advanced banking system with financial logic and fraud detection.
    
    IMPLEMENT ALL PREVIOUS LEVELS PLUS:
    - transfer_funds(self, from_account, to_account, amount, description): Transfer between accounts
    - freeze_account(self, account_number, reason): Freeze account
    - unfreeze_account(self, account_number): Unfreeze account
    - detect_suspicious_activity(self, account_number, time_window): Fraud detection
    - schedule_transfer(self, from_account, to_account, amount, schedule_time): Schedule future transfer
    - process_scheduled_transfers(self): Process due transfers
    - get_account_summary(self, account_number): Enhanced summary with fraud info
    """
    
    def __init__(self):
        """Initialize the banking system."""
        # TODO: Initialize storage for accounts, transactions, frozen accounts, and scheduled transfers
        pass
    
    # =================== LEVEL 1-2 METHODS ===================
    # Copy your Level 1-2 implementation here (enhance create_account for overdraft limits)
    
    def create_account(self, customer_name, account_type="checking", initial_deposit=0.0):
        """Create a new account with overdraft limits."""
        # TODO: Enhance to include overdraft limits based on account type
        pass
    
    def get_account(self, account_number):
        """Get account information."""
        # TODO: Copy from Level 1
        pass
    
    def deposit(self, account_number, amount):
        """Deposit money to account."""
        # TODO: Copy from Level 1 (add frozen account check)
        pass
    
    def withdraw(self, account_number, amount):
        """Withdraw money from account."""
        # TODO: Enhance to handle overdraft protection and fees
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
    
    def get_transactions_in_timerange(self, account_number, start_time, end_time):
        """Get transactions within a time range."""
        # TODO: Copy from Level 2
        pass
    
    def search_transactions(self, account_number, query):
        """Search transactions by description."""
        # TODO: Copy from Level 2
        pass
    
    def calculate_interest(self, account_number, annual_rate=0.02):
        """Calculate interest for savings accounts."""
        # TODO: Copy from Level 2
        pass
    
    def get_accounts_by_type(self, account_type):
        """Get accounts by type."""
        # TODO: Copy from Level 2
        pass
    
    def get_account_summary(self, account_number):
        """Get account summary."""
        # TODO: Enhance to include fraud detection info
        pass
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def transfer_funds(self, from_account, to_account, amount, description="Transfer"):
        """
        Transfer funds between accounts.
        
        Args:
            from_account (str): Source account number
            to_account (str): Destination account number
            amount (float): Amount to transfer
            description (str): Transfer description
            
        Returns:
            bool: True if successful, False if failed
        """
        # TODO: Implement fund transfers with overdraft handling
        pass
    
    def freeze_account(self, account_number, reason="Security hold"):
        """
        Freeze an account to prevent transactions.
        
        Args:
            account_number (str): Account to freeze
            reason (str): Reason for freezing
            
        Returns:
            bool: True if frozen, False if account not found
        """
        # TODO: Implement account freezing
        pass
    
    def unfreeze_account(self, account_number):
        """
        Unfreeze an account.
        
        Args:
            account_number (str): Account to unfreeze
            
        Returns:
            bool: True if unfrozen, False if account not found
        """
        # TODO: Implement account unfreezing
        pass
    
    def detect_suspicious_activity(self, account_number, time_window=3600):
        """
        Detect potentially fraudulent activity.
        
        Args:
            account_number (str): Account to analyze
            time_window (int): Time window for analysis (seconds)
            
        Returns:
            list: List of suspicious activity flags
        """
        # TODO: Implement fraud detection
        pass
    
    def schedule_transfer(self, from_account, to_account, amount, schedule_time, description="Scheduled transfer"):
        """
        Schedule a future transfer.
        
        Args:
            from_account (str): Source account
            to_account (str): Destination account
            amount (float): Amount to transfer
            schedule_time (float): When to execute transfer
            description (str): Transfer description
            
        Returns:
            int: Transfer ID if scheduled, None if failed
        """
        # TODO: Implement transfer scheduling
        pass
    
    def process_scheduled_transfers(self):
        """
        Process all due scheduled transfers.
        
        Returns:
            int: Number of transfers processed
        """
        # TODO: Implement scheduled transfer processing
        pass


# Quick test - uncomment when ready
if __name__ == "__main__":
    bank = BankingSystem()
    print("Level 3: Implement the advanced banking logic!")
