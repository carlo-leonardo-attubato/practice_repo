"""
Unit Tests for Level 1: Basic Account Management
"""

import pytest
import sys
import os

# Import configuration
from assessments.test_config import get_full_import_path

# Get the correct import path based on configuration
import_path = get_full_import_path('banking_system', 'level1')
exec(f"from {import_path} import BankingSystem")


class TestBankingSystemLevel1:
    """Test cases for Level 1 BankingSystem."""
    
    def setup_method(self):
        """Set up a fresh BankingSystem instance before each test."""
        self.bank = BankingSystem()
    
    def test_initialization(self):
        """Test that BankingSystem initializes correctly."""
        assert self.bank is not None
        assert hasattr(self.bank, 'accounts')
        assert hasattr(self.bank, 'transactions')
    
    def test_create_account_basic(self):
        """Test basic account creation."""
        account_number = self.bank.create_account("John Doe", 100.0)
        assert account_number is not None
        assert isinstance(account_number, str)
        
        account = self.bank.get_account(account_number)
        assert account is not None
        assert account['customer_name'] == "John Doe"
        assert account['balance'] == 100.0
    
    def test_create_account_no_initial_deposit(self):
        """Test account creation without initial deposit."""
        account_number = self.bank.create_account("Jane Smith")
        account = self.bank.get_account(account_number)
        assert account['balance'] == 0.0
    
    def test_create_multiple_accounts(self):
        """Test creating multiple accounts with unique numbers."""
        acc1 = self.bank.create_account("Alice", 500.0)
        acc2 = self.bank.create_account("Bob", 1000.0)
        
        assert acc1 != acc2
        assert self.bank.get_account(acc1)['customer_name'] == "Alice"
        assert self.bank.get_account(acc2)['customer_name'] == "Bob"
    
    def test_deposit_valid(self):
        """Test valid deposit operation."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        result = self.bank.deposit(account_number, 50.0)
        assert result is True
        
        balance = self.bank.get_balance(account_number)
        assert balance == 150.0
    
    def test_deposit_invalid_amount(self):
        """Test deposit with invalid amount."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        result = self.bank.deposit(account_number, -50.0)
        assert result is False
        
        result = self.bank.deposit(account_number, 0.0)
        assert result is False
        
        # Balance should remain unchanged
        assert self.bank.get_balance(account_number) == 100.0
    
    def test_deposit_nonexistent_account(self):
        """Test deposit to non-existent account."""
        result = self.bank.deposit("nonexistent", 50.0)
        assert result is False
    
    def test_withdraw_valid(self):
        """Test valid withdrawal operation."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        result = self.bank.withdraw(account_number, 30.0)
        assert result is True
        
        balance = self.bank.get_balance(account_number)
        assert balance == 70.0
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        account_number = self.bank.create_account("John Doe", 50.0)
        
        result = self.bank.withdraw(account_number, 100.0)
        assert result is False
        
        # Balance should remain unchanged
        assert self.bank.get_balance(account_number) == 50.0
    
    def test_withdraw_invalid_amount(self):
        """Test withdrawal with invalid amount."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        result = self.bank.withdraw(account_number, -30.0)
        assert result is False
        
        result = self.bank.withdraw(account_number, 0.0)
        assert result is False
    
    def test_get_balance(self):
        """Test balance retrieval."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        assert self.bank.get_balance(account_number) == 100.0
        
        self.bank.deposit(account_number, 50.0)
        assert self.bank.get_balance(account_number) == 150.0
        
        self.bank.withdraw(account_number, 25.0)
        assert self.bank.get_balance(account_number) == 125.0
    
    def test_get_balance_nonexistent(self):
        """Test balance retrieval for non-existent account."""
        balance = self.bank.get_balance("nonexistent")
        assert balance is None
    
    def test_transaction_history(self):
        """Test transaction history tracking."""
        account_number = self.bank.create_account("John Doe", 100.0)
        
        # Initial deposit should be recorded
        history = self.bank.get_transaction_history(account_number)
        assert len(history) >= 1
        assert history[0]['type'] == 'deposit'
        assert history[0]['amount'] == 100.0
        
        # Additional transactions
        self.bank.deposit(account_number, 50.0)
        self.bank.withdraw(account_number, 25.0)
        
        history = self.bank.get_transaction_history(account_number)
        assert len(history) >= 3
    
    def test_list_all_accounts(self):
        """Test listing all accounts."""
        accounts = self.bank.list_all_accounts()
        assert len(accounts) == 0
        
        self.bank.create_account("Alice", 500.0)
        self.bank.create_account("Bob", 1000.0)
        
        accounts = self.bank.list_all_accounts()
        assert len(accounts) == 2
        
        names = [acc['customer_name'] for acc in accounts]
        assert "Alice" in names
        assert "Bob" in names


def run_tests():
    """Run all tests and display results."""
    print("🧪 Level 1: Basic Account Management")
    print("=" * 50)
    
    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
    
    print("\n" + "=" * 50)
    print("✅ Level 1 tests completed!")


if __name__ == "__main__":
    run_tests()
