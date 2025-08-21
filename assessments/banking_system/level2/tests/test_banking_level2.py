import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Import configuration
from assessments.test_config import get_full_import_path

# Get the correct import path based on configuration
import_path = get_full_import_path('banking_system', 'level2')
exec(f"from {import_path} import BankingSystem")

class TestBankingLevel2:
    def test_transfer_between_accounts(self):
        bank = BankingSystem()
        acc1 = bank.create_account("alice", initial_deposit=1000)
        acc2 = bank.create_account("bob", initial_deposit=500)
        
        # Test successful transfer
        result = bank.transfer(acc1, acc2, 300)
        assert result == True
        assert bank.get_balance(acc1) == 700
        assert bank.get_balance(acc2) == 800
        
        # Test insufficient funds
        result = bank.transfer(acc1, acc2, 1000)
        assert result == False
        assert bank.get_balance(acc1) == 700
        assert bank.get_balance(acc2) == 800
        
        # Test invalid accounts
        result = bank.transfer(acc1, "charlie", 100)
        assert result == False
        
    def test_account_history(self):
        bank = BankingSystem()
        acc1 = bank.create_account("user1", initial_deposit=1000)
        acc2 = bank.create_account("user2", initial_deposit=0)
        bank.deposit(acc1, 200)
        bank.withdraw(acc1, 100)
        bank.transfer(acc1, acc2, 150)
        
        history = bank.get_account_history(acc1)
        assert len(history) >= 4  # create, deposit, withdraw, transfer
        
    def test_multiple_accounts(self):
        bank = BankingSystem()
        acc1 = bank.create_account("user1", initial_deposit=100)
        acc2 = bank.create_account("user2", initial_deposit=200)
        acc3 = bank.create_account("user3", initial_deposit=300)
        
        assert bank.get_balance(acc1) == 100
        assert bank.get_balance(acc2) == 200
        assert bank.get_balance(acc3) == 300
        
        # Test total system balance
        total = sum([bank.get_balance(acc1), bank.get_balance(acc2), bank.get_balance(acc3)])
        assert total == 600
