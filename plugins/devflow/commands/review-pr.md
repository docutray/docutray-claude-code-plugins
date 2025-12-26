---
description: "Perform complete technical review of Pull Requests including branch checkout, technical tests, error correction, and quality validation"
allowed-tools:
  - Read
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
argument-hints:
  - "<pr-number>"
  - "--fix-issues"
  - "--run-full-suite"
  - "--auto-approve"
  - "--functional-tests"
  - "--skip-functional"
---

# Pull Request Review Command (/review-pr)

Command to perform complete technical review of Pull Requests, including branch checkout, technical test execution, error correction, and quality validation following professional QA methodology.

## 📋 Complete Technical Details

**See**: `.claude/details/commands/review-pr.md` for complete technical implementation, including:
- Detailed procedures for each phase
- Optional functional testing configuration
- Troubleshooting and advanced configurations

## Usage

```bash
/review-pr <pr-number> [--fix-issues] [--run-full-suite] [--auto-approve] [--functional-tests] [--skip-functional]
```

## Objective

Perform complete technical review of a Pull Request as part of structured development flow, including:

### 🔧 Technical Validations
- Read and analyze PR information
- Identify original implemented issue
- Checkout corresponding branch
- Execute tests, linting, type checking, and build using `/check`
- Automatic correction of found problems
- Validation against original issue acceptance criteria

### 🧪 Optional: Functional Validations (QA)
- Automatic start of local server (if configured)
- Automated functional tests (if configured)
- User flow validation according to implemented changes
- Critical functionality verification
- Functional regression detection
- Evidence capture (screenshots, logs)

### 📊 Reports and Feedback
- Request user feedback for additional modifications
- Generate consolidated technical reports
- Constructive review comments

## Parameters

### Basic Parameters
- `<pr-number>`: Pull Request number to review (required)
- `--fix-issues`: Automatically correct found problems (optional)
- `--run-full-suite`: Run complete test suite (optional, default only related tests)
- `--auto-approve`: Auto-approve if no problems (optional)

### Optional: Functional Test Parameters
- `--functional-tests`: Enable automatic functional tests (if configured)
- `--skip-functional`: Skip functional tests (only technical validations)

## 🔄 Review Process

### **Phase 1: PR Analysis** 🔍
1. **Initial verification** - GitHub auth, permissions, complete PR info
2. **Issue identification** - Automatic extraction of implemented issue
3. **Impact analysis** - Modified files, affected areas, statistics

### **Phase 2: Environment Preparation** ⚙️
4. **Branch checkout** - Fork or same repo, automatic setup
5. **Dependency verification** - Install if necessary
6. **State backup** - For complete reversibility

### **Phase 3: Technical Validations** 🔧
7. **Complete optimized technical suite**:
   - Use of `/check` command for parallel validations
   - `/check --fast` for quick validations (without build)
   - `/check` for complete validation including build
   - Automatic corrections when possible
   - Regeneration if necessary (e.g., Prisma, code generation)

### **Phase 4: Optional Functional Validations** 🧪
8. **If functional tests configured**:
   - Read configuration from `.claude/details/commands/review-pr.md`
   - Start local server if needed
   - Execute configured functional tests
   - Validate affected areas
   - Capture evidence and screenshots

### **Phase 5: Analysis and Report** 📊
9. **Result consolidation** - Technical + functional (if enabled)
10. **Problem classification** - Critical, high, medium, low
11. **Evidence generation** - Logs, screenshots (if applicable)
12. **Unified report** - Technical + QA with complete methodology

### **Phase 6: Final Actions** ✅
13. **User presentation** - Executive summary + options
14. **Actions based on decision** - Comment, approval, required changes
15. **Cleanup** - State restoration, cleanup

## 🚀 Common Use Cases

### Complete Technical Review (Standard)
```bash
/review-pr 123 --fix-issues
# ✅ Complete technical validations
# 🔧 Automatic corrections applied
# 📊 Consolidated technical report
```

### Quick Review with Auto-approval
```bash
/review-pr 123 --auto-approve
# ⚡ Technical validations
# ✅ Automatic approval if no critical errors
```

### Review with Functional Tests (Optional)
```bash
/review-pr 123 --functional-tests --fix-issues
# ✅ Complete technical validations
# 🧪 Automated functional tests (if configured)
# 🔧 Automatic corrections applied
# 📊 Consolidated technical + QA report
```

## 🎯 Quality Criteria

### ✅ Mandatory Technical Validations
- **Successful /check command**: All parallel validations passing
- Linting without critical errors (acceptable warnings)
- Type checking without errors
- Unit tests passing (>90%)
- Successful build without critical warnings
- Consistent code format
- **Performance**: Validations in <5min thanks to parallelization

### 🧪 Optional: Functional Validations
- **Critical flows working** (if configured)
- **No detected regressions** in existing functionalities
- **Responsive interfaces** and accessible (if applicable)
- **Acceptable performance** (if configured)
- **Errors properly handled** (if applicable)

### 🔒 Security Validations
- No exposed secrets
- Implemented input validation
- Protected queries
- Verified auth/authz

## 📋 Optional Configuration

### Functional Tests (Optional)

If the project requires functional tests, configure in:
`.claude/details/commands/review-pr.md`

Example configuration:
```json
{
  "functional_tests": {
    "enabled": true,
    "server": {
      "command": "npm run dev",
      "port": 3000,
      "wait_time": 5000
    },
    "test_suites": {
      "authentication": true,
      "main_flows": true,
      "critical_paths": true
    }
  }
}
```

## 🔗 Integration with Development Flow

**Complete Flow**: `/feat` → `/dev` → `/check` → `/review-pr` ← **HERE**

1. **`/feat`**: Generate technical specification and issue
2. **`/dev issue#X`**: Implement functionality (uses `/check`) → PR
3. **`/check`**: Validate implementation quality
4. **`/review-pr pr#Y`**: Review technically (uses `/check`) + optionally functionally → Approval/Merge

**Consolidated Output**:
```
📋 COMPLETE REVIEW - PR #123

🔗 Implemented issue: #456 ✅
🔧 Technical validations (/check): ✅ 4/4 passing in 2.3min
📊 Coverage: 94% (+2% vs baseline)
⚡ Performance: Optimized parallel validation

✅ Complete flow:
   /feat → Issue #456 ✅
   /dev issue#456 → PR #123 ✅
   /review-pr 123 → Approved ✅

🚀 READY FOR MERGE
```

## 🆘 Quick Troubleshooting

- **GitHub auth error**: `gh auth login`
- **Merge conflicts**: Resolve manually or ask user
- **Failing tests**: Review with `--verbose` to see details
- **Failing build**: Check dependencies and configuration

## Project Customization

**REQUIRED**: Each project should configure review details in:
`.claude/details/commands/review-pr.md`

This file should include:
- Project-specific validation criteria
- Functional test configuration (optional)
- Server startup commands (if applicable)
- Additional validation requirements
- Review checklist
- Approval criteria

**Projects must configure this file during `/devflow-setup`**

---

**📖 For complete technical implementation**: See `.claude/details/commands/review-pr.md`
