---
name: devflow-research
description: Research and analyze topics to gather information before creating epics or features. Use when users need to investigate technologies, approaches, or requirements. Trigger phrases: "research topic", "investigate technology", "analyze approach", "/research", "feasibility study"
type: flow
---

# DevFlow: Research & Analysis Flow

Research and analyze topics, technologies, or requirements before creating epics or features.

## When to Use

Use this flow when you need to:
- Research a new technology or library
- Analyze feasibility of an approach
- Gather requirements before planning
- Compare alternatives
- Assess risks and effort

## Flow Diagram

```mermaid
flowchart TD
    A([BEGIN]) --> B[Understand research topic]
    B --> C[Determine depth level]
    C --> D{Depth?}
    D -->|shallow| E[Quick overview scope]
    D -->|medium| F[Balanced research scope]
    D -->|deep| G[Comprehensive analysis scope]
    E --> H[Define research areas]
    F --> H
    G --> H
    H --> I[Gather information]
    I --> I1[WebSearch for articles]
    I --> I2[WebFetch documentation]
    I --> I3[Search codebase patterns]
    I --> I4[Analyze existing implementations]
    I1 --> J[Analyze findings]
    I2 --> J
    I3 --> J
    I4 --> J
    J --> K[Compare alternatives]
    K --> L[Assess risks and trade-offs]
    L --> M[Estimate complexity]
    M --> N{Output format?}
    N -->|summary| O[Generate concise summary]
    N -->|detailed| P[Create extended analysis]
    N -->|report| Q[Create comprehensive report]
    O --> R[Provide recommendations]
    P --> R
    Q --> R
    R --> S{Significant initiative?}
    S -->|Yes| T[Guide to /flow:devflow-epic]
    S -->|No| U[Guide to /flow:devflow-feat]
    T --> V([END])
    U --> V
```

## Node Details

### 1. Topic Understanding
Clarify with user:
- Specific research questions
- Context and constraints
- Decisions that depend on this research

### 2. Information Gathering
Use multiple sources:
- **WebSearch**: Current articles, comparisons
- **WebFetch**: Official documentation
- **Grep/Glob**: Internal codebase patterns
- **Read**: Existing implementations

### 3. Analysis Areas

**Technology/Library Research**:
- Adoption and maturity
- Documentation quality
- Integration complexity
- Performance characteristics
- Licensing and costs

**Feature Research**:
- User requirements
- Similar implementations
- Technical feasibility
- Dependencies

**Architecture Research**:
- Design patterns
- Scalability considerations
- Security aspects
- Testing strategies

### 4. Output Generation

Based on `--output` parameter:
- **summary**: Key findings and recommendations (1-2 paragraphs)
- **detailed**: Extended analysis with examples
- **report**: Full document with all sections

### 5. Next Steps
Guide user based on research outcome:
- Significant initiative → `/flow:devflow-epic`
- Standard feature → `/flow:devflow-feat`

## Parameters

- `<topic>`: Required - topic to research
- `--depth=shallow|medium|deep`: Research thoroughness
- `--output=summary|detailed|report`: Output format

## Example Usage

```
/flow:devflow-research "OAuth 2.0 integration"
/flow:devflow-research "microservices architecture" --depth=deep --output=report
/flow:devflow-research "React vs Vue" --output=detailed
```

## Output

Research summary with:
- Key findings
- Risk assessment
- Recommendations
- Clear next step guidance
