# Command Parsing Pattern - ANTHROPIC CODESIGNAL FORMAT

## The EXACT Pattern Anthropic Uses

Based on the Reddit post, **every Anthropic CodeSignal follows this format:**

1. **You get a list of commands** (like `["FILE_UPLOAD", "Cars.txt", "200kb"]`)
2. **You write a parser** that converts commands to method calls
3. **You implement the underlying system** (file system, database, etc.)
4. **You return results** in the expected format

## The 4 Progressive Levels

### **Level 1**: Basic Operations
```python
["FILE_UPLOAD", "Cars.txt", "200kb"]     → fs.upload_file("Cars.txt", "200kb")
["FILE_GET", "Cars.txt"]                 → fs.get_file("Cars.txt")
["FILE_COPY", "Cars.txt", "Cars2.txt"]   → fs.copy_file("Cars.txt", "Cars2.txt")
```

### **Level 2**: Search Operations
```python
["FILE_SEARCH", "Ba"]                    → fs.search_files("Ba")
```

### **Level 3**: Time-based Operations (TTL!)
```python
["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "file.txt", "150kb", 3600]
                                         → fs.upload_file("file.txt", "150kb", timestamp, ttl=3600)
["FILE_GET_AT", "2021-07-01T13:00:01", "file.txt"]
                                         → fs.get_file("file.txt", timestamp)
```

### **Level 4**: System State Management
```python
["ROLLBACK", "2021-07-01T12:10:00"]      → fs.rollback_to_time(timestamp)
```

## The Conversion Strategy

### Step 1: Write the OOP Class First
```python
class FileSystemSimulator:
    def __init__(self):
        self.files = {}
    
    def upload_file(self, filename, size, timestamp=None, ttl=None):
        # Your familiar OOP logic here
        pass
```

### Step 2: Write the Command Parser
```python
def simulate_coding_framework(commands):
    fs = FileSystemSimulator()
    results = []
    
    for command in commands:
        if command[0] == "FILE_UPLOAD":
            result = fs.upload_file(command[1], command[2])
            results.append(result)
        # ... handle other commands
    
    return results
```

### Step 3: Handle the Weird Parts
- **Timestamps**: Convert ISO strings to Unix timestamps
- **TTL**: Track expiration times
- **Rollback**: Save state history for restoration
- **Search**: Filter by filename prefixes

## Why This Matters

**The Reddit user said:** *"if you do a few practice problems you'll have an advantage because you won't need to relearn the basic concept"*

**Your advantage**: You now understand the conversion pattern!
- Commands → Method calls
- Familiar OOP logic inside
- Return formatted strings
- Handle time-based operations

## Practice Strategy

1. **Study the conversion** in `file_system_simulation.py`
2. **Practice command parsing** with different scenarios
3. **Focus on TTL logic** - it's always Level 3
4. **Master rollback patterns** - it's always Level 4

**This is the EXACT format you'll see tomorrow!** 🎯
