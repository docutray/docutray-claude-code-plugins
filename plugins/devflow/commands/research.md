---
description: "Research and analyze topics to gather information before creating epics or features"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Bash(git status:*)
  - Bash(git log:*)
  - WebSearch
  - WebFetch
  - Task
argument-hints:
  - "<topic>"
  - "--depth=shallow"
  - "--depth=medium"
  - "--depth=deep"
  - "--output=summary"
  - "--output=detailed"
  - "--output=report"
---

# Research Command

Command to research and analyze topics, technologies, or requirements before creating epics or features.

## Context

- Current branch: !`git branch --show-current`
- Project structure: !`ls -la`

## Usage

```bash
/research <topic> [--depth=shallow|medium|deep] [--output=summary|detailed|report]
```

## Objective

Gather comprehensive information about a topic to make informed decisions before creating epics or features. This includes:
- Technology research and feasibility analysis
- Best practices and patterns investigation
- Competitive analysis
- Requirements gathering
- Risk assessment
- Effort estimation preparation

## Parameters

- `<topic>`: Topic or area to research (required)
- `--depth`: Research depth level (default: `medium`)
  - `shallow`: Quick overview, basic information
  - `medium`: Balanced research with key insights
  - `deep`: Comprehensive analysis with detailed findings
- `--output`: Output format (default: `summary`)
  - `summary`: Concise findings summary
  - `detailed`: Extended analysis with examples
  - `report`: Full report with recommendations

## Instructions for Claude

**IMPORTANT - Structured research process**

### Research Flow

1. **Topic Clarification**: Understand what needs to be researched
2. **Scope Definition**: Determine boundaries and focus areas
3. **Information Gathering**: Collect data from multiple sources
4. **Analysis**: Process and synthesize information
5. **Documentation**: Create structured output
6. **Recommendations**: Provide actionable next steps

### Process Details

#### 1. Topic Understanding

Ask the user to clarify:
- What specific aspect needs research?
- What is the context (new feature, refactor, technology choice)?
- Are there specific concerns or questions?
- What decisions depend on this research?

#### 2. Research Areas

Depending on the topic, investigate:

**Technology/Library Research**:
- Current adoption and maturity
- Documentation quality and community support
- Integration complexity
- Performance characteristics
- Licensing and costs
- Known limitations

**Feature Research**:
- User requirements and use cases
- Similar implementations (internal/external)
- Technical feasibility
- Dependencies and prerequisites
- Potential challenges

**Architecture Research**:
- Design patterns and best practices
- Scalability considerations
- Maintainability implications
- Security aspects
- Testing strategies

#### 3. Information Sources

Use available tools to gather information:
- **WebSearch**: Find current articles, documentation, comparisons
- **WebFetch**: Read specific documentation or blog posts
- **Grep/Glob**: Search codebase for existing patterns
- **Read**: Analyze current implementations
- **Task**: Use specialized agents for deep dives

#### 4. Analysis and Synthesis

Process gathered information:
- Identify key findings and insights
- Compare alternatives if applicable
- Assess risks and trade-offs
- Estimate complexity and effort
- Consider project-specific implications

#### 5. Output Generation

Create structured documentation based on `--output` parameter:

**Summary Format**:
```markdown
## Research Summary: <Topic>

### Key Findings
- Finding 1
- Finding 2
- Finding 3

### Recommendations
- Recommendation 1
- Recommendation 2

### Next Steps
- Suggested action 1
- Suggested action 2
```

**Detailed Format**:
Include examples, code snippets, comparisons, and extended analysis.

**Report Format**:
Comprehensive document with sections:
- Executive Summary
- Background and Context
- Research Methodology
- Detailed Findings
- Comparative Analysis
- Risk Assessment
- Recommendations
- Conclusion
- References

#### 6. Next Step Guidance

After completing research, inform the user about appropriate next steps:

**For significant initiatives**:
```
✅ Research completed for: <topic>

📊 Key findings documented
🎯 Recommendations provided

🚀 Suggested next steps:
   /epic to create comprehensive development plan

💡 The research document can be attached to the epic for context
```

**For smaller features**:
```
✅ Research completed for: <topic>

📊 Key findings documented
🎯 Recommendations provided

🚀 Suggested next steps:
   /feat to create feature specification and issue

💡 The research document provides context for feature planning
```

### Research Best Practices

- **Be objective**: Present facts and trade-offs, not just positives
- **Be thorough**: Cover multiple perspectives and scenarios
- **Be practical**: Focus on actionable insights
- **Be contextual**: Consider project-specific constraints
- **Cite sources**: Reference documentation and articles
- **Update if needed**: Research can be iterative

### Integration with Development Flow

**Research** is typically the first step for complex or uncertain initiatives:

**Full Flow**: `/research` → `/epic` OR `/feat` → `/dev` → `/review-pr`

**When to use `/research`**:
- Before starting significant new features
- When evaluating new technologies
- For architectural decisions
- When requirements are unclear
- For feasibility assessments

**When to skip `/research`**:
- Well-understood features
- Simple bug fixes
- Established patterns
- Clear requirements

### Output Example

```
🔍 RESEARCH COMPLETED: OAuth 2.0 Integration

📋 Research Scope:
   Depth: Medium
   Focus: Implementation feasibility and security
   Duration: 15 minutes

🎯 Key Findings:
   ✅ Multiple proven libraries available (passport, next-auth)
   ✅ Industry standard with extensive documentation
   ⚠️  Requires secure token storage strategy
   ⚠️  Session management complexity increases

💡 Recommendations:
   1. Use next-auth for Next.js compatibility
   2. Implement refresh token rotation
   3. Add rate limiting for auth endpoints
   4. Plan for ~3 days implementation time

📊 Risk Assessment:
   Security: Medium (mitigated with best practices)
   Complexity: Medium
   Maintenance: Low (mature ecosystem)

🔗 References:
   - OAuth 2.0 RFC 6749
   - next-auth documentation
   - OWASP Authentication Guidelines

🚀 Next Step:
   /epic oauth-integration to plan full implementation
```

## Customization

Projects can customize research templates and checklists by creating:
`.claude/details/commands/research.md`

This file can include:
- Project-specific research checklist
- Required sections for reports
- Internal resources to consult
- Stakeholders to involve
- Compliance requirements
