"""
LEVEL 3: Advanced Banking Logic - MODEL SOLUTION
Complex financial operations and validation.
"""

import time
from collections import defaultdict


class BankingSystem:
    """Advanced banking system with financial logic."""
    
    def __init__(self):
        """Initialize the banking system."""
        self.accounts = {}
        self.transactions = defaultdict(list)
        self.next_account_number = 1000001
        self.frozen_accounts = set()
        self.overdraft_fees = {}  # account_number -> fee_amount
    
    # =================== LEVEL 1-2 METHODS ===================
    
    def create_account(self, customer_name, account_type="checking", initial_deposit=0.0):
        """Create a new account with type."""
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        self.accounts[account_number] = {
            'account_number': account_number,
            'customer_name': customer_name,
            'account_type': account_type,
            'balance': initial_deposit,
            'created_at': time.time(),
            'overdraft_limit': 500.0 if account_type == "checking" else 0.0
        }
        
        if initial_deposit > 0:
            self.transactions[account_number].append({
                'type': 'deposit',
                'amount': initial_deposit,
                'timestamp': time.time(),
                'description': 'Initial deposit',
                'category': 'initial'
            })
        
        return account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def deposit(self, account_number, amount, category="general"):
        if account_number not in self.accounts or amount <= 0:
            return False
        
        if account_number in self.frozen_accounts:
            return False
        
        self.accounts[account_number]['balance'] += amount
        self.transactions[account_number].append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': time.time(),
            'description': f'Deposit of ${amount:.2f}',
            'category': category
        })
        
        return True
    
    def withdraw(self, account_number, amount, category="general"):
        if account_number not in self.accounts or amount <= 0:
            return False
        
        if account_number in self.frozen_accounts:
            return False
        
        account = self.accounts[account_number]
        available_balance = account['balance'] + account['overdraft_limit']
        
        if available_balance < amount:
            return False
        
        # Check if overdraft will occur
        overdraft_amount = max(0, amount - account['balance'])
        
        account['balance'] -= amount
        
        transaction = {
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': time.time(),
            'description': f'Withdrawal of ${amount:.2f}',
            'category': category
        }
        
        # Add overdraft fee if applicable
        if overdraft_amount > 0:
            fee = 35.0  # Standard overdraft fee
            account['balance'] -= fee
            self.overdraft_fees[account_number] = self.overdraft_fees.get(account_number, 0) + fee
            
            transaction['overdraft_fee'] = fee
            transaction['description'] += f' (Overdraft fee: ${fee:.2f})'
        
        self.transactions[account_number].append(transaction)
        return True
    
    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        return account['balance'] if account else None
    
    def get_transaction_history(self, account_number, category=None):
        transactions = self.transactions.get(account_number, [])
        if category:
            return [t for t in transactions if t.get('category') == category]
        return transactions
    
    def list_all_accounts(self):
        return list(self.accounts.values())
    
    def get_transactions_in_timerange(self, account_number, start_time, end_time):
        transactions = self.transactions.get(account_number, [])
        return [t for t in transactions if start_time <= t['timestamp'] <= end_time]
    
    def search_transactions(self, account_number, query):
        transactions = self.transactions.get(account_number, [])
        query_lower = query.lower()
        return [t for t in transactions if query_lower in t['description'].lower()]
    
    def calculate_interest(self, account_number, annual_rate=0.02):
        account = self.accounts.get(account_number)
        if not account or account['account_type'] != 'savings':
            return 0.0
        return account['balance'] * (annual_rate / 12)  # Monthly interest
    
    # =================== LEVEL 3 NEW METHODS ===================
    
    def transfer_funds(self, from_account, to_account, amount, description="Transfer"):
        """Transfer funds between accounts."""
        if from_account not in self.accounts or to_account not in self.accounts:
            return False
        
        if amount <= 0:
            return False
        
        # Check if sender has sufficient funds (including overdraft)
        sender = self.accounts[from_account]
        available_balance = sender['balance'] + sender['overdraft_limit']
        
        if available_balance < amount:
            return False
        
        # Process withdrawal from sender
        withdraw_success = self.withdraw(from_account, amount, "transfer_out")
        if not withdraw_success:
            return False
        
        # Process deposit to receiver
        deposit_success = self.deposit(to_account, amount, "transfer_in")
        if not deposit_success:
            # Rollback withdrawal
            self.deposit(from_account, amount, "transfer_rollback")
            return False
        
        # Update transaction descriptions
        sender_transactions = self.transactions[from_account]
        receiver_transactions = self.transactions[to_account]
        
        sender_transactions[-1]['description'] = f"Transfer to {to_account}: {description}"
        receiver_transactions[-1]['description'] = f"Transfer from {from_account}: {description}"
        
        return True
    
    def freeze_account(self, account_number, reason="Security hold"):
        """Freeze an account to prevent transactions."""
        if account_number not in self.accounts:
            return False
        
        self.frozen_accounts.add(account_number)
        self.transactions[account_number].append({
            'type': 'freeze',
            'amount': 0,
            'timestamp': time.time(),
            'description': f'Account frozen: {reason}',
            'category': 'administrative'
        })
        
        return True
    
    def unfreeze_account(self, account_number):
        """Unfreeze an account."""
        if account_number not in self.accounts:
            return False
        
        self.frozen_accounts.discard(account_number)
        self.transactions[account_number].append({
            'type': 'unfreeze',
            'amount': 0,
            'timestamp': time.time(),
            'description': 'Account unfrozen',
            'category': 'administrative'
        })
        
        return True
    
    def detect_suspicious_activity(self, account_number, time_window=3600):
        """Detect potentially fraudulent activity."""
        current_time = time.time()
        recent_transactions = self.get_transactions_in_timerange(
            account_number, current_time - time_window, current_time
        )
        
        # Flag suspicious patterns
        suspicious_flags = []
        
        # High frequency transactions
        if len(recent_transactions) > 10:
            suspicious_flags.append("high_frequency")
        
        # Large withdrawal amounts
        large_withdrawals = [t for t in recent_transactions 
                           if t['type'] == 'withdrawal' and t['amount'] > 5000]
        if large_withdrawals:
            suspicious_flags.append("large_withdrawals")
        
        # Multiple overdrafts
        overdraft_transactions = [t for t in recent_transactions 
                                if t.get('overdraft_fee', 0) > 0]
        if len(overdraft_transactions) > 2:
            suspicious_flags.append("multiple_overdrafts")
        
        return suspicious_flags
    
    def schedule_transfer(self, from_account, to_account, amount, schedule_time, description="Scheduled transfer"):
        """Schedule a future transfer."""
        # For simplicity, we'll store scheduled transfers and process them when requested
        if not hasattr(self, 'scheduled_transfers'):
            self.scheduled_transfers = []
        
        transfer = {
            'from_account': from_account,
            'to_account': to_account,
            'amount': amount,
            'schedule_time': schedule_time,
            'description': description,
            'status': 'pending'
        }
        
        self.scheduled_transfers.append(transfer)
        return len(self.scheduled_transfers) - 1  # Return transfer ID
    
    def process_scheduled_transfers(self):
        """Process all due scheduled transfers."""
        if not hasattr(self, 'scheduled_transfers'):
            return 0
        
        current_time = time.time()
        processed_count = 0
        
        for transfer in self.scheduled_transfers:
            if (transfer['status'] == 'pending' and 
                transfer['schedule_time'] <= current_time):
                
                success = self.transfer_funds(
                    transfer['from_account'],
                    transfer['to_account'],
                    transfer['amount'],
                    transfer['description']
                )
                
                transfer['status'] = 'completed' if success else 'failed'
                transfer['processed_at'] = current_time
                
                if success:
                    processed_count += 1
        
        return processed_count
    
    def get_account_summary(self, account_number):
        """Get comprehensive account summary."""
        if account_number not in self.accounts:
            return None
        
        account = self.accounts[account_number]
        transactions = self.transactions[account_number]
        
        # Calculate transaction stats
        deposits = [t for t in transactions if t['type'] == 'deposit']
        withdrawals = [t for t in transactions if t['type'] == 'withdrawal']
        
        return {
            'account_number': account_number,
            'customer_name': account['customer_name'],
            'account_type': account['account_type'],
            'current_balance': account['balance'],
            'overdraft_limit': account['overdraft_limit'],
            'total_deposits': sum(t['amount'] for t in deposits),
            'total_withdrawals': sum(t['amount'] for t in withdrawals),
            'transaction_count': len(transactions),
            'overdraft_fees': self.overdraft_fees.get(account_number, 0),
            'is_frozen': account_number in self.frozen_accounts,
            'suspicious_flags': self.detect_suspicious_activity(account_number)
        }


if __name__ == "__main__":
    bank = BankingSystem()
    
    # Test Level 3 functionality
    print("Testing Level 3 banking functionality...")
    
    # Create accounts
    acc1 = bank.create_account("Alice Johnson", "checking", 1000.0)
    acc2 = bank.create_account("Bob Smith", "savings", 5000.0)
    
    # Test transfers
    transfer_success = bank.transfer_funds(acc1, acc2, 200.0, "Monthly savings")
    print(f"Transfer successful: {transfer_success}")
    
    # Test overdraft
    overdraft_success = bank.withdraw(acc1, 1500.0)  # Should trigger overdraft
    print(f"Overdraft withdrawal: {overdraft_success}")
    
    # Test fraud detection
    suspicious = bank.detect_suspicious_activity(acc1)
    print(f"Suspicious activity flags: {suspicious}")
    
    # Test account freezing
    bank.freeze_account(acc1, "Suspicious activity detected")
    frozen_withdraw = bank.withdraw(acc1, 100.0)  # Should fail
    print(f"Withdrawal from frozen account: {frozen_withdraw}")
    
    # Get summary
    summary = bank.get_account_summary(acc1)
    print(f"Account summary: {summary}")
    
    print("✅ Level 3 implementation complete!")
