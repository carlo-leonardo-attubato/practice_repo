# Mock Assessment: File System Commands (EXACT ANTHROPIC PATTERN!)

## Overview
**This is the EXACT pattern Anthropic uses based on Reddit user who took it twice!**

Build a command-driven file system simulation progressively across 4 levels. Every Anthropic CodeSignal follows this command parsing format.

## Assessment Structure

### Level 1: Basic File Operations (15-20 min)
**Goal**: Parse basic file commands and implement core operations
- FILE_UPLOAD: Upload files with size tracking
- FILE_GET: Retrieve files by name
- FILE_COPY: Copy files to new names
- Command parsing to OOP conversion

### Level 2: Enhanced File Features (20-25 min)
**Goal**: Add search and filtering capabilities
- FILE_SEARCH: Find files by name prefix
- Enhanced file metadata
- Result formatting and sorting
- Pattern matching operations

### Level 3: Time-based Operations (30-40 min)
**Goal**: Add TTL and timestamp-based operations (ALWAYS Level 3!)
- FILE_UPLOAD_AT: Upload with timestamps and TTL
- FILE_GET_AT: Time-aware file retrieval
- FILE_COPY_AT: Timestamp-based copying
- FILE_SEARCH_AT: Time-aware searching
- Expiration handling

### Level 4: System State Management (15-20 min)
**Goal**: Add rollback and system state operations (ALWAYS Level 4!)
- ROLLBACK: Restore system to previous timestamp
- State history tracking
- Time-based state restoration
- System consistency

## Time Management
- **Total**: 90 minutes
- **Level 1-2**: 25 minutes (basic commands + search)
- **Level 3**: 50 minutes (TTL operations - FOCUS HERE)
- **Level 4**: 15 minutes (rollback functionality)

## Scoring Strategy
- **Level 1**: ~100 points (basic command parsing)
- **Level 2**: ~150 points (search operations)
- **Level 3**: ~250 points (time-based operations - FOCUS HERE)
- **Level 4**: ~100 points (rollback functionality)
- **Total**: 600 points (need 520+ to pass)

## Key Patterns from Reddit User
1. **Command parsing is ALWAYS the format** - practice this conversion
2. **TTL operations are ALWAYS Level 3** - files expire after time
3. **Rollback is ALWAYS Level 4** - restore system state
4. **Speed matters more than code quality** - get tests passing fast

## The Conversion Pattern
```python
# Command format:
["FILE_UPLOAD", "Cars.txt", "200kb"]

# Converts to:
fs.upload_file("Cars.txt", "200kb")

# Returns:
"uploaded Cars.txt"
```

## Critical Success Factors
- **Practice command parsing** - this is the EXACT format
- **Master TTL logic** - expiration is always tested
- **Understand rollback** - state management is always Level 4
- **Focus on speed** - typing speed and mouse dexterity matter

**This assessment gives you the EXACT advantage the Reddit user mentioned!**
