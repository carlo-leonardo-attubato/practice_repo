# Speed Drills Practice Guide

## How to Practice

### 1. Start with MessageStore (Beginner)
- **File**: `message_store.py`
- **Tests**: `test_message_store.py`
- **Focus**: Basic CRUD operations, timestamps, cleanup logic
- **Time Target**: 15-20 minutes

### 2. Move to TTLStore (Intermediate)
- **File**: `ttl_store.py`
- **Tests**: `test_ttl_store.py`
- **Focus**: Time-based expiration, automatic cleanup
- **Time Target**: 20-25 minutes

### 3. Advanced: InventorySystem (Hard)
- **File**: `inventory_system.py`
- **Tests**: `test_inventory_system.py`
- **Focus**: Complex filtering, search, data organization
- **Time Target**: 30-40 minutes

## Practice Workflow

### Step 1: Read the Problem
- Understand what each method should do
- Note the return types and parameters
- Identify the data structures you'll need

### Step 2: Plan Your Approach
- Sketch out the storage structure
- Think about edge cases
- Plan the implementation order

### Step 3: Implement Method by Method
- Start with `__init__` and basic operations
- Build up to complex methods
- Test each method as you go

### Step 4: Run Tests
```bash
# Run specific test file
python -m pytest speed_drills/test_message_store.py -v

# Run all tests
python -m pytest speed_drills/ -v

# Quick test from file
python speed_drills/message_store.py
```

## Key Patterns to Master

### Data Structures
```python
# Nested dictionaries
self.data = defaultdict(dict)

# Lists with metadata
self.items = []  # List of dicts

# Separate storage for different data types
self.messages = {}
self.timestamps = {}
```

### Common Operations
```python
# Safe dictionary access
value = self.data.get(key, default_value)

# List filtering
results = [item for item in items if condition]

# Existence checking
if key in self.data:
    # do something
```

### Time Operations
```python
import time

# Current timestamp
current_time = time.time()

# Check if expired
if current_time > expiry_time:
    # item is expired
```

## Speed Tips

1. **Don't overthink** - Get working code first
2. **Use built-ins** - `get()`, `defaultdict`, list comprehensions
3. **Handle edge cases** - Empty lists, missing keys, invalid inputs
4. **Test incrementally** - Run tests after each method
5. **Copy patterns** - Reuse working code structures

## Assessment Strategy

- **Level 1-2**: Basic CRUD operations (20-25 min)
- **Level 3**: Complex filtering and search (40-50 min)
- **Level 4**: Advanced features and edge cases (15-20 min)

Remember: **Working code beats perfect code** in CodeSignal!
