"""
LEVEL 4: Premium Banking Features - MODEL SOLUTION
Investment accounts, loans, credit scoring, and premium features.
"""

import time
import random
from collections import defaultdict


class BankingSystem:
    """Premium banking system with investment and loan features."""
    
    def __init__(self):
        """Initialize the premium banking system."""
        self.accounts = {}  # account_number -> account_data
        self.transactions = defaultdict(list)  # account_number -> transaction_list
        self.investments = defaultdict(dict)  # account_number -> investment_data
        self.loans = {}  # loan_id -> loan_data
        self.credit_scores = {}  # account_number -> credit_score
        self.next_account_number = 1000001
        self.next_loan_id = 10001
    
    def create_account(self, customer_name, initial_deposit=0.0, account_type="checking"):
        """Create a new account with type."""
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        self.accounts[account_number] = {
            'account_number': account_number,
            'customer_name': customer_name,
            'balance': initial_deposit,
            'account_type': account_type,
            'created_at': time.time(),
            'is_premium': account_type in ["premium", "investment"]
        }
        
        if initial_deposit > 0:
            self.transactions[account_number].append({
                'type': 'deposit',
                'amount': initial_deposit,
                'timestamp': time.time(),
                'description': 'Initial deposit'
            })
        
        # Initialize credit score
        self.credit_scores[account_number] = random.randint(600, 750)
        
        return account_number
    
    def invest(self, account_number, amount, investment_type):
        """Invest money in investment account."""
        if account_number not in self.accounts:
            return False
        
        account = self.accounts[account_number]
        if account['account_type'] != 'investment':
            return False
        
        if account['balance'] < amount:
            return False
        
        account['balance'] -= amount
        
        if account_number not in self.investments:
            self.investments[account_number] = {}
        
        investment_id = f"inv_{len(self.investments[account_number]) + 1}"
        self.investments[account_number][investment_id] = {
            'type': investment_type,
            'amount': amount,
            'timestamp': time.time()
        }
        
        return True
    
    def get_investment_balance(self, account_number):
        """Get total investment balance."""
        if account_number not in self.investments:
            return 0
        
        total = sum(inv['amount'] for inv in self.investments[account_number].values())
        return total
    
    def withdraw_investment(self, account_number, amount):
        """Withdraw from investment account."""
        if account_number not in self.investments:
            return False
        
        current_balance = self.get_investment_balance(account_number)
        if current_balance < amount:
            return False
        
        # Simple withdrawal - in reality would need more complex logic
        self.accounts[account_number]['balance'] += amount
        return True
    
    def request_loan(self, account_number, amount, months):
        """Request a loan."""
        if account_number not in self.accounts:
            return None
        
        credit_score = self.credit_scores.get(account_number, 600)
        if credit_score < 650:
            return None
        
        loan_id = str(self.next_loan_id)
        self.next_loan_id += 1
        
        self.loans[loan_id] = {
            'loan_id': loan_id,
            'account_number': account_number,
            'amount': amount,
            'months': months,
            'status': 'pending',
            'requested_at': time.time()
        }
        
        return loan_id
    
    def get_loan_status(self, loan_id):
        """Get loan status."""
        loan = self.loans.get(loan_id)
        return loan['status'] if loan else None
    
    def get_credit_score(self, account_number):
        """Get credit score."""
        return self.credit_scores.get(account_number, 600)
    
    def make_payment(self, account_number, amount):
        """Make a payment to improve credit score."""
        if account_number not in self.accounts:
            return False
        
        # Improve credit score with payment
        current_score = self.credit_scores.get(account_number, 600)
        improvement = min(10, amount // 100)  # Max 10 point improvement
        self.credit_scores[account_number] = min(850, current_score + improvement)
        
        return True
    
    def has_premium_features(self, account_number):
        """Check if account has premium features."""
        account = self.accounts.get(account_number)
        return account and account.get('is_premium', False)
    
    def get_monthly_fee(self, account_number):
        """Get monthly fee for account."""
        account = self.accounts.get(account_number)
        if not account:
            return 0
        
        if account.get('is_premium', False):
            return 0
        elif account['account_type'] == 'checking':
            return 10
        elif account['account_type'] == 'savings':
            return 5
        else:
            return 15
    
    # Basic methods from level 1
    def get_balance(self, account_number):
        """Get current account balance."""
        account = self.accounts.get(account_number)
        return account['balance'] if account else None
    
    def deposit(self, account_number, amount):
        """Deposit money to account."""
        if account_number not in self.accounts or amount <= 0:
            return False
        
        self.accounts[account_number]['balance'] += amount
        return True
    
    def withdraw(self, account_number, amount):
        """Withdraw money from account."""
        if account_number not in self.accounts or amount <= 0:
            return False
        
        if self.accounts[account_number]['balance'] < amount:
            return False
        
        self.accounts[account_number]['balance'] -= amount
        return True
