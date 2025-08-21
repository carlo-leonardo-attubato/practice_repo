"""
LEVEL 2: Enhanced Banking Features - MODEL SOLUTION
Enhanced banking with account types and transaction analysis.
"""

import time
from collections import defaultdict


class BankingSystem:
    """Enhanced banking system with account types and transaction analysis."""
    
    def __init__(self):
        """Initialize the banking system."""
        self.accounts = {}  # account_number -> account_data
        self.transactions = defaultdict(list)  # account_number -> transaction_list
        self.next_account_number = 1000001
    
    # =================== LEVEL 1 METHODS ===================
    
    def create_account(self, customer_name, account_type="checking", initial_deposit=0.0):
        """Create a new account with type."""
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        self.accounts[account_number] = {
            'account_number': account_number,
            'customer_name': customer_name,
            'account_type': account_type,
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
    
    # =================== LEVEL 2 NEW METHODS ===================
    
    def get_transactions_in_timerange(self, account_number, start_time, end_time):
        """Get transactions within a time range."""
        transactions = self.transactions.get(account_number, [])
        return [t for t in transactions if start_time <= t['timestamp'] <= end_time]
    
    def search_transactions(self, account_number, query):
        """Search transactions by description."""
        transactions = self.transactions.get(account_number, [])
        query_lower = query.lower()
        return [t for t in transactions if query_lower in t['description'].lower()]
    
    def calculate_interest(self, account_number, annual_rate=0.02):
        """Calculate monthly interest for savings accounts."""
        account = self.accounts.get(account_number)
        if not account or account['account_type'] != 'savings':
            return 0.0
        
        return account['balance'] * (annual_rate / 12)  # Monthly interest
    
    def get_accounts_by_type(self, account_type):
        """Get all accounts of a specific type."""
        return [account for account in self.accounts.values() 
                if account['account_type'] == account_type]
    
    def get_account_summary(self, account_number):
        """Get comprehensive account summary."""
        if account_number not in self.accounts:
            return None
        
        account = self.accounts[account_number]
        transactions = self.transactions[account_number]
        
        # Calculate transaction statistics
        deposits = [t for t in transactions if t['type'] == 'deposit']
        withdrawals = [t for t in transactions if t['type'] == 'withdrawal']
        
        total_deposits = sum(t['amount'] for t in deposits)
        total_withdrawals = sum(t['amount'] for t in withdrawals)
        
        return {
            'account_number': account_number,
            'customer_name': account['customer_name'],
            'account_type': account['account_type'],
            'current_balance': account['balance'],
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals,
            'transaction_count': len(transactions),
            'monthly_interest': self.calculate_interest(account_number),
            'account_age_days': (time.time() - account['created_at']) / 86400
        }


if __name__ == "__main__":
    bank = BankingSystem()
    
    # Test Level 2 functionality
    print("Testing Level 2 functionality...")
    
    # Create different account types
    checking = bank.create_account("Alice Johnson", "checking", 1000.0)
    savings = bank.create_account("Bob Smith", "savings", 5000.0)
    
    # Test transactions
    bank.deposit(checking, 500.0)
    bank.withdraw(checking, 200.0)
    bank.deposit(savings, 1000.0)
    
    # Test filtering by type
    checking_accounts = bank.get_accounts_by_type("checking")
    savings_accounts = bank.get_accounts_by_type("savings")
    print(f"Checking accounts: {len(checking_accounts)}")
    print(f"Savings accounts: {len(savings_accounts)}")
    
    # Test interest calculation
    interest = bank.calculate_interest(savings)
    print(f"Monthly interest for savings: ${interest:.2f}")
    
    # Test transaction search
    deposit_transactions = bank.search_transactions(checking, "deposit")
    print(f"Deposit transactions: {len(deposit_transactions)}")
    
    # Test account summary
    summary = bank.get_account_summary(checking)
    print(f"Account summary: {summary}")
    
    print("✅ Level 2 implementation complete!")
