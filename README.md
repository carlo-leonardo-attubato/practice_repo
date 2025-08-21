# CodeSignal Practice Repository

## Overview
Practice CodeSignal assessments with progressive 4-level mock assessments that mirror the real CodeSignal format.

## Repository Structure

```
practice_repo/
├── assessments/
│   ├── inventory_system/          # Mock Assessment 1
│   │   ├── level1/                # Basic CRUD (~100 pts)
│   │   │   ├── candidate/         # Your implementation
│   │   │   ├── model_solution/    # Working reference
│   │   │   └── tests/             # Unit tests
│   │   ├── level2/                # Enhanced features (~150 pts)
│   │   ├── level3/                # Complex logic (~250 pts)
│   │   └── level4/                # Advanced ops (~100 pts)
│   ├── user_management/           # Mock Assessment 2 (coming soon)
│   └── data_cache/                # Mock Assessment 3 (coming soon)
├── assessment_runner.py           # Test runner
└── README.md
```

## Available Assessments

### 1. Inventory Management System ✅ **COMPLETE**
**Total Points**: 600 (need 520+ to pass)

- **Level 1** (15-20 min, ~100 pts): Basic CRUD operations
- **Level 2** (20-25 min, ~150 pts): Filtering and search
- **Level 3** (30-40 min, ~250 pts): Stock management and business logic ⭐ **FOCUS HERE**
- **Level 4** (15-20 min, ~100 pts): Advanced operations

### 2. Model Welfare Tracker 🚧 **IN PROGRESS**
**Anthropic-specific scenario** - AI model usage monitoring and welfare tracking

- **Level 1** (15-20 min, ~100 pts): Model registration and interaction logging
- **Level 2** (20-25 min, ~150 pts): Interaction analysis and filtering
- **Level 3** (30-40 min, ~250 pts): Welfare scoring and rate limiting ⭐ **FOCUS HERE**
- **Level 4** (15-20 min, ~100 pts): System monitoring and management

### 3. Banking System 🚧 **IN PROGRESS**
**Financial operations** - Account management and transaction processing

- **Level 1** (15-20 min, ~100 pts): Basic account operations
- **Level 2** (20-25 min, ~150 pts): Transaction history and account types
- **Level 3** (30-40 min, ~250 pts): Financial logic and fraud detection ⭐ **FOCUS HERE**
- **Level 4** (15-20 min, ~100 pts): System operations and compliance

### 4. Chat Platform 🚧 **IN PROGRESS**
**Real-time messaging** - Message management and communication features

- **Level 1** (15-20 min, ~100 pts): Basic messaging
- **Level 2** (20-25 min, ~150 pts): Message filtering and search
- **Level 3** (30-40 min, ~250 pts): Advanced chat features and moderation ⭐ **FOCUS HERE**
- **Level 4** (15-20 min, ~100 pts): Platform management

### 5. Task Queue System 🚧 **IN PROGRESS**
**Job scheduling** - Priority queues and task management

- **Level 1** (15-20 min, ~100 pts): Basic task operations
- **Level 2** (20-25 min, ~150 pts): Priority and filtering
- **Level 3** (30-40 min, ~250 pts): Dependencies and scheduling ⭐ **FOCUS HERE**
- **Level 4** (15-20 min, ~100 pts): System operations

## How to Practice

### Option 1: Progressive Practice
1. **Start with Level 1** of an assessment
2. **Implement the required methods** in the candidate folder
3. **Run tests** to verify your implementation
4. **Move to Level 2** and build on your Level 1 code
5. **Continue through Level 4**

### Option 2: Study Mode
1. **Study model solutions** to understand patterns
2. **Run tests on model solutions** to see expected behavior
3. **Practice implementing** from memory
4. **Compare your solution** with the model

### Option 3: Timed Assessment Mode
1. **Run full 90-minute simulation** with timer
2. **Focus on Level 3** for maximum points
3. **Submit working code** even if imperfect

## Running Assessments

### Using the Assessment Runner (Recommended)

```bash
# List available assessments
python assessment_runner.py --list

# Run full assessment on your implementation
python assessment_runner.py inventory_system

# Run specific level only
python assessment_runner.py inventory_system --level level1

# Test model solutions (to verify they work)
python assessment_runner.py inventory_system --mode model

# Timed 90-minute simulation
python assessment_runner.py inventory_system --timed

# Verbose output
python assessment_runner.py inventory_system --verbose
```

### Manual Testing
```bash
# Test specific level manually
python -m pytest assessments/inventory_system/level1/tests/ -v
```

## Assessment Strategy

### Time Management (90 minutes total)
- **Levels 1-2**: 25 minutes (get basics working)
- **Level 3**: 50 minutes ⭐ **FOCUS HERE - most points**
- **Level 4**: 15 minutes (attempt what you can)

### Scoring Strategy
- **Target**: 520+ out of 600 points (87% success rate)
- **Level 3 is critical** - prioritize completing it over perfecting earlier levels
- **Working code beats perfect code** - submit as soon as tests pass

### Key Principles
1. **Read ALL levels first** (5 minutes) to understand the big picture
2. **Build progressively** - each level extends the previous
3. **Don't refactor** - focus on making tests pass
4. **Use simple data structures** - lists and dictionaries
5. **Copy-paste between levels** - reuse working code

## Progress Tracking

Track your practice progress:
- ✅ **Inventory System Level 1**: Basic CRUD
- ⏳ **Inventory System Level 2**: Filtering & Search  
- ⏳ **Inventory System Level 3**: Stock Management
- ⏳ **Inventory System Level 4**: Advanced Operations

## Getting Started

1. **Choose an assessment**: Start with `inventory_system`
2. **Run the model solution**: `python assessment_runner.py inventory_system --mode model`
3. **Study the requirements**: Check the README in the assessment folder
4. **Implement Level 1**: Start coding in the candidate folder
5. **Test your solution**: `python assessment_runner.py inventory_system --level level1`
6. **Progress to Level 2**: Build on your Level 1 implementation

**Remember**: The goal is to build muscle memory for rapid implementation under time pressure!