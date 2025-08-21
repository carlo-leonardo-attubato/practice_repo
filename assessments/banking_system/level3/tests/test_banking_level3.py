import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from banking_system.level3.model_solution.banking import BankingSystem

class TestBankingLevel3:
    def test_interest_calculation(self):
        bank = BankingSystem()
        bank.create_account("user1", 1000)
        
        # Test interest calculation
        initial_balance = bank.get_balance("user1")
        bank.apply_interest("user1", 0.05)  # 5% interest
        new_balance = bank.get_balance("user1")
        
        assert new_balance == initial_balance * 1.05
        
    def test_account_types(self):
        bank = BankingSystem()
        bank.create_account("user1", 1000, "savings")
        bank.create_account("user2", 1000, "checking")
        
        assert bank.get_account_type("user1") == "savings"
        assert bank.get_account_type("user2") == "checking"
        
    def test_overdraft_protection(self):
        bank = BankingSystem()
        bank.create_account("user1", 100, "checking")
        
        # Test overdraft protection
        result = bank.withdraw("user1", 150)
        assert result == False  # Should fail due to overdraft protection
        assert bank.get_balance("user1") == 100
        
    def test_savings_withdrawal_limit(self):
        bank = BankingSystem()
        bank.create_account("user1", 1000, "savings")
        
        # Test savings withdrawal limit
        result = bank.withdraw("user1", 800)
        assert result == False  # Should fail due to withdrawal limit
        assert bank.get_balance("user1") == 1000
        
        # Test successful withdrawal within limit
        result = bank.withdraw("user1", 200)
        assert result == True
        assert bank.get_balance("user1") == 800
