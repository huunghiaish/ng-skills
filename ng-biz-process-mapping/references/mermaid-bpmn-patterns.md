# Mermaid BPMN Patterns for Business Processes

## Basic Process Flow

```mermaid
flowchart TD
    A([Bắt đầu: Trigger]) --> B[Bước 1: Action]
    B --> C{Điều kiện?}
    C -->|Có| D[Bước 2a]
    C -->|Không| E[Bước 2b]
    D --> F([Kết thúc])
    E --> F
```

## Multi-Department (Swimlanes)

```mermaid
flowchart TD
    subgraph Sales["🏢 Kinh doanh"]
        A([Nhận lead]) --> B[Phân loại]
        B --> C{Qualified?}
    end
    subgraph Ops["⚙️ Vận hành"]
        C -->|Có| D[Tạo đơn hàng]
        D --> E[Xử lý đơn]
    end
    subgraph Finance["💰 Tài chính"]
        E --> F[Xuất hóa đơn]
        F --> G([Hoàn tất])
    end
```

## Color Coding Convention

```
style manual_step fill:#FF9800,stroke:#E65100,color:#000
style digital_step fill:#4CAF50,stroke:#1B5E20,color:#fff
style pain_point fill:#F44336,stroke:#B71C1C,color:#fff
style decision fill:#2196F3,stroke:#0D47A1,color:#fff
style start_end fill:#9E9E9E,stroke:#424242,color:#fff
```

| Color | Meaning | Hex |
|-------|---------|-----|
| Orange | Manual step | #FF9800 |
| Green | Digital/automated step | #4CAF50 |
| Red | Pain point / bottleneck | #F44336 |
| Blue | Decision point | #2196F3 |
| Grey | Start / End | #9E9E9E |

## Parallel Tasks

```mermaid
flowchart TD
    A[Nhận đơn] --> B[Kiểm tra tồn kho]
    A --> C[Xác nhận thanh toán]
    B --> D{Cả hai OK?}
    C --> D
    D -->|Có| E[Đóng gói]
    D -->|Không| F[Thông báo KH]
```

## Loop / Retry Pattern

```mermaid
flowchart TD
    A[Gửi báo giá] --> B{KH đồng ý?}
    B -->|Không| C[Điều chỉnh giá]
    C --> A
    B -->|Có| D[Chốt đơn]
    B -->|Hủy| E([Kết thúc])
```

## Process Landscape (High-Level)

For the overall company view, use a left-to-right flow:

```mermaid
flowchart LR
    subgraph Core["Core Processes"]
        S[Sales] --> O[Operations] --> D[Delivery]
    end
    subgraph Support["Support Processes"]
        F[Finance] -.-> Core
        H[HR] -.-> Core
        I[IT] -.-> Core
    end
    subgraph Management["Management"]
        M[Strategy] ==> Core
    end
```

Use:
- `-->` solid arrow: direct flow
- `-.->` dotted arrow: supporting relationship
- `==>` thick arrow: governance/oversight

## Tips

- Keep diagrams under 15 nodes for readability
- Split complex processes into sub-diagrams
- Use Vietnamese labels inside nodes
- Add emoji prefix in subgraph titles for visual clarity
- Always apply color coding to distinguish manual vs digital
