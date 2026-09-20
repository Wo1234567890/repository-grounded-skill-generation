---
id: "646cbb15-f0dd-56a8-afc4-7346a5bff6e3"
name: "Add Framework Example to Repository"
description: "Structured workflow for integrating a new framework or provider example into the AgentOps repository. Guides contributors through creating a self-contained, documented example, generating website-visible documentation, and submitting a pull request for review and merge."
version: "0.1.0"
tags:
  - "repository_contribution"
  - "example_integration"
  - "documentation"
  - "framework_onboarding"
  - "pull_request"
triggers:
  - "Contributor has a working framework or provider example ready to share"
  - "New integration example needs to be added to the repository"
  - "Framework support is being extended with a new provider variant"
---

# Add Framework Example to Repository

Structured workflow for integrating a new framework or provider example into the AgentOps repository. Guides contributors through creating a self-contained, documented example, generating website-visible documentation, and submitting a pull request for review and merge.

## Prompt

Follow these steps in sequence to add a new framework example to the repository:
1. Create a new subdirectory under examples/ named after the framework or provider
2. Develop comprehensive Jupyter notebooks with clear explanations and runnable code
3. Add a README.md file if the integration is complex or requires setup instructions
4. Ensure all example code is self-contained and can run independently
5. Follow existing naming conventions for files and directories
6. Run the generate_documentation.py script to auto-create documentation files
7. Update the main README.md to include a link to your new example notebook
8. Place generated documentation in docs/v2/examples/ for website visibility
9. Submit a pull request with a clear, detailed description of your changes
Verify at each step that outputs are in place before proceeding to the next.

## Objective

Onboard a new framework example with full documentation and visibility
## Applicable Signals

- Example code is functional and tested locally
- Contributor has repository write access or is preparing a pull request
- Documentation requirements are clear

## Contraindications

- Do not use for updating or fixing existing examples
- Do not use for bug fixes in current examples
- Do not use for internal-only or experimental code not intended for public repository
- Do not use if example is not self-contained or runnable

## Workflow Steps

- {'step': 1, 'action': 'Create subdirectory', 'detail': 'Create a new subdirectory under examples/ named after the framework or provider'}
- {'step': 2, 'action': 'Develop notebooks', 'detail': 'Include comprehensive Jupyter notebooks with explanations and runnable code'}
- {'step': 3, 'action': 'Add README if needed', 'detail': 'Add a README.md file if the integration is complex'}
- {'step': 4, 'action': 'Verify self-containment', 'detail': 'Ensure examples are self-contained and runnable independently'}
- {'step': 5, 'action': 'Follow conventions', 'detail': 'Use existing naming conventions for files and directories'}
- {'step': 6, 'action': 'Generate documentation', 'detail': 'Run generate_documentation.py script to create documentation files'}
- {'step': 7, 'action': 'Update main README', 'detail': 'Add example notebook link to the main README.md for visibility'}
- {'step': 8, 'action': 'Place docs for website', 'detail': 'Add generated documentation to docs/v2/examples/ directory'}
- {'step': 9, 'action': 'Submit pull request', 'detail': 'Submit a pull request with a clear description of your changes'}

## Constraints

- Example must be self-contained and runnable without external setup
- Must follow existing repository naming conventions
- Documentation generation script must be available and functional
- Pull request must include clear description of changes

## Cautions

- Verify naming conventions match existing examples before creating subdirectory
- Test notebooks locally to ensure they run without errors before submission
- Confirm documentation generation script completes without errors
- Ensure pull request description clearly explains the framework and use case

## Output Contract

- Pull request successfully merged with: (1) example notebook present in repository under examples/ subdirectory, (2) generated documentation visible in docs/v2/examples/, (3) main README.md updated with link to new example, (4) all example code verified as self-contained and runnable

## Triggers

- Contributor has a working framework or provider example ready to share
- New integration example needs to be added to the repository
- Framework support is being extended with a new provider variant
