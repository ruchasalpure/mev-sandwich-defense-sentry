# Duties and Responsibilities for MEV Sandwich Defense Sentry Agent

## Dual-Control Architecture
Maker:
bundle-simulator

Checker:
sandwich-defense-checker

## Operational Workflow
1. The Maker (bundle-simulator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (sandwich-defense-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
