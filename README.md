# CodeSignal Speed Drill Practice Repository

## What You Have

✅ **Speed Drills** (unimplemented - for you to practice):
- `basic_store.py` - Basic dictionary operations
- `nested_userstore.py` - Nested dictionary patterns  
- `ttl_store.py` - Time-based expiration (TTL)
- `inventory_system.py` - List filtering operations
- `backup_restore.py` - Backup/restore functionality

✅ **Unit Tests** (fully implemented and working):
- `tests/test_01_basic_store.py` - Tests for basic store
- `tests/test_02_nested_userstore.py` - Tests for user store
- `tests/test_03_ttl_store.py` - Tests for TTL store
- `tests/test_04_inventory_system.py` - Tests for inventory
- `tests/test_05_backup_restore.py` - Tests for database

## How to Practice

1. **Pick a speed drill** (start with `basic_store.py`)
2. **Implement the methods** marked with TODO
3. **Run the tests** to see if you pass
4. **Move to the next drill** when current one passes

## Running Tests

```bash
# Test specific drill
python -m pytest tests/test_01_basic_store.py -v

# Test all drills
python -m pytest tests/ -v

# Quick test from test file
python tests/test_01_basic_store.py
```

## Your Goal

Implement each speed drill so that **ALL TESTS PASS**. This builds the muscle memory you need for CodeSignal.

## Assessment Strategy

- **Level 1-2**: Basic CRUD operations (20-25 min)
- **Level 3**: Complex filtering and search (40-50 min)  
- **Level 4**: Advanced features and edge cases (15-20 min)

**Remember**: Working code beats perfect code in CodeSignal!
