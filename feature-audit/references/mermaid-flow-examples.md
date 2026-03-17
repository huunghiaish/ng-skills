# Mermaid Flow Examples for Audit

## User Flow Diagram

```mermaid
flowchart TD
    A[User Action] --> B{Condition?}
    B -->|Yes| C[Happy Path]
    B -->|No| D[Alt Path]
    C --> E[Success State]
    D --> F[Error/Fallback]
    F --> G{Retry?}
    G -->|Yes| A
    G -->|No| H[Exit]
```

## Feature Dependency Map

```mermaid
flowchart LR
    subgraph Core
        Auth[Authentication]
        DB[(Database)]
    end
    subgraph Features
        F1[Feature 1]
        F2[Feature 2]
        F3[Feature 3]
    end
    Auth --> F1
    Auth --> F2
    DB --> F1
    DB --> F3
    F1 --> F2
```

## Requirement Traceability

```mermaid
flowchart TD
    REQ[Customer Requirement] --> PRD[PRD Item]
    PRD --> SPEC[Technical Spec]
    SPEC --> SRS[SRS Detail]
    SRS --> CODE[Implementation]
    CODE --> TEST[Test Case]

    style REQ fill:#e1f5fe
    style CODE fill:#e8f5e9
    style TEST fill:#fff3e0
```

## Risk Heat Map (as flowchart)

```mermaid
flowchart TD
    subgraph "Critical"
        R1[Security: No auth on /admin]
        R2[Data: No backup strategy]
    end
    subgraph "High"
        R3[Functional: Payment flow incomplete]
    end
    subgraph "Medium"
        R4[UX: No error states]
    end

    style R1 fill:#ff5252,color:#fff
    style R2 fill:#ff5252,color:#fff
    style R3 fill:#ff9800,color:#fff
    style R4 fill:#ffc107
```

## Data Flow

```mermaid
flowchart LR
    Client -->|Request| API
    API -->|Validate| Auth
    Auth -->|Token| API
    API -->|Query| DB[(Database)]
    DB -->|Result| API
    API -->|Response| Client
```

## State Machine (for feature states)

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review: Submit
    Review --> Approved: Approve
    Review --> Draft: Reject
    Approved --> Published: Publish
    Published --> Archived: Archive
    Archived --> [*]
```

## Tips
- Use `subgraph` to group related features
- Color-code by status: green=complete, yellow=partial, red=missing
- Keep diagrams focused - max 15-20 nodes per diagram
- Split complex flows into multiple diagrams
