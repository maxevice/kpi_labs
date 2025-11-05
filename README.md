### Lab2

# Functional Requirements

| **ID** | **Requirement** | **Description** |
|--------|------------------|------------------|
| **FR1** | User authorization | The system must allow users (Admin and Customer) to log in before accessing restricted features. |
| **FR2** | Manage products | The system must allow admins to create, view, update, and delete product information. |
| **FR3** | Manage cart | The system must allow customers to manage their cart. This includes adding items to their cart, deleting items from their cart. |
| **FR4** | Rating system | The system must allow authenticated users to submit reviews and ratings for purchased products. |
| **FR5** | Order processing | The system must provide admins with an interface to process new orders and update their status. |
| **FR6** | Make payment | The system must allow customers to pay for their placed orders. Payment is available only after an order is successfully created. |
| **FR7** | Sales report | The system must include functionality for generating sales reports. |
| **FR8** | View orders | The system must allow authenticated customers to view their own orders. |

# Non-Functional Requirements

| **ID** | **Requirement** | **Description** |
|--------|------------------|------------------|
| **NFR1** | Performance | The average response time should not exceed 2 seconds with a maximum load of 1000 users. |
| **NFR2** | Access control | Unauthorized users must not access admin or customer-restricted functions. |
| **NFR3** | Usability | The user interface must be intuitive. |
| **NFR4** | Compatibility | The system must be fully usable on desktop and mobile devices. |
| **NFR5** | Maintainability | The system must be built with a modular architecture to allow future updates without downtime. |
| **NFR6** | Localization | The system must support multiple languages if required (e.g., English, Ukrainian). |

# Use Cases

| **ID** | **Use Case Name** |
|--------|--------------------|
| **UC1** | Authorization |
| **UC2** | Browse products |
| **UC3** | Filter products |
| **UC4** | Browse categories |
| **UC5** | View product details |
| **UC6** | Manage cart |
| **UC7** | Add item to cart |
| **UC8** | Delete item from cart |
| **UC9** | Place order |
| **UC10** | Make payment |
| **UC11** | View orders |
| **UC12** | Track order status |
| **UC13** | Write review |
| **UC14** | Manage products |
| **UC15** | Add products |
| **UC16** | Delete products |
| **UC17** | Edit product details |
| **UC18** | Generate sales report |
| **UC19** | Process orders |
| **UC20** | Update order status |

# Traceability Matrix (FR ↔ UC)

| FR \ UC | UC1 | UC2 | UC3 | UC4 | UC5 | UC6 | UC7 | UC8 | UC9 | UC10 | UC11 | UC12 | UC13 | UC14 | UC15 | UC16 | UC17 | UC18 | UC19 | UC20 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| **FR1** | X |  |  |  |  |  |  |  | X | X | X | X | X | X | X | X | X | X | X | X |
| **FR2** |  | X | X | X | X |  | X | X | X | X |  | X |  | X | X | X | X |  |  |  |
| **FR3** |  |  |  |  |  | X | X | X | X |  |  |  |  |  |  |  |  |  |  |  |
| **FR4** |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |
| **FR5** |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  | X | X |
| **FR6** |  |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |  |
| **FR7** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |
| **FR8** |  |  |  |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |




