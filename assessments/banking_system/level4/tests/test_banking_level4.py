import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from banking_system.level4.model_solution.banking import BankingSystem

class TestBankingLevel4:
    def test_investment_accounts(self):
        bank = BankingSystem()
        bank.create_account("user1", 10000, "investment")
        
        # Test investment operations
        result = bank.invest("user1", 1000, "stocks")
        assert result == True
        assert bank.get_investment_balance("user1") == 1000
        
        # Test investment withdrawal
        result = bank.withdraw_investment("user1", 500)
        assert result == True
        assert bank.get_investment_balance("user1") == 500
        
    def test_loan_processing(self):
        bank = BankingSystem()
        bank.create_account("user1", 5000)
        
        # Test loan approval
        loan_id = bank.request_loan("user1", 2000, 12)  # 12 months
        assert loan_id is not None
        
        # Test loan status
        status = bank.get_loan_status(loan_id)
        assert status in ["pending", "approved", "rejected"]
        
    def test_credit_score_tracking(self):
        bank = BankingSystem()
        bank.create_account("user1", 1000)
        
        # Test credit score calculation
        score = bank.get_credit_score("user1")
        assert 300 <= score <= 850
        
        # Test credit score improvement
        bank.make_payment("user1", 100)
        new_score = bank.get_credit_score("user1")
        assert new_score >= score
        
    def test_premium_features(self):
        bank = BankingSystem()
        bank.create_account("user1", 50000, "premium")
        
        # Test premium features
        assert bank.has_premium_features("user1") == True
        assert bank.get_monthly_fee("user1") == 0  # No fees for premium
        
        # Test regular account
        bank.create_account("user2", 1000, "checking")
        assert bank.has_premium_features("user2") == False
        assert bank.get_monthly_fee("user2") > 0
