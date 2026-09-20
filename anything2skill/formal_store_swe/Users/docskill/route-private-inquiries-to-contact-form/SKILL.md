---
id: "52c06090-5fd0-5971-aead-2fac814e4c20"
name: "Route Private Inquiries to Contact Form"
description: "Identify user inquiries containing sensitive business information, personal data, or explicit confidentiality requests, and redirect them to the contact form to maintain privacy and prevent exposure in public channels."
version: "0.1.0"
tags:
  - "privacy"
  - "confidentiality"
  - "support_routing"
  - "access_control"
  - "guardrail"
triggers:
  - "User inquiry contains sensitive business information, personal data, or requires confidential handling; user requests private communication"
---

# Route Private Inquiries to Contact Form

Identify user inquiries containing sensitive business information, personal data, or explicit confidentiality requests, and redirect them to the contact form to maintain privacy and prevent exposure in public channels.

## Prompt

When a user inquiry contains sensitive business information, personal data, or explicitly requests confidential handling, direct the user to submit via the contact form rather than GitHub Issues, Discussions, or Discord. Emphasize that public channels are preferred for technical discussions only.

## Objective

Protect user privacy by preventing sensitive information from being posted in public channels
## Applicable Signals

- User inquiry contains sensitive business information
- User inquiry contains personal data
- User explicitly requests private or confidential communication
- User indicates need for non-public handling

## Contraindications

- Issue is a public bug report or feature request
- User explicitly requests public discussion or community visibility
- Inquiry is a technical documentation question
- Issue is a feature announcement or community showcase

## Intervention Moves

- Identify sensitivity markers in incoming inquiry
- Offer contact form link with explanation of privacy protection
- Confirm user understands public vs. private channel distinction

## Workflow Steps

- Scan incoming inquiry for sensitivity indicators (business confidentiality, personal data, explicit privacy requests)
- If sensitivity detected, present contact form as exclusive channel for private inquiries
- Provide functional contact form link and brief explanation of privacy protection
- Confirm user understanding of public vs. private channel distinction

## Constraints

- Public channels (GitHub Issues, Discussions, Discord) must remain free of sensitive data
- Contact form must be presented as the exclusive channel for private inquiries
- Technical discussions should be directed to public channels when no confidentiality is required

## Cautions

- Do not assume all inquiries are sensitive; only escalate when explicit indicators are present
- Ensure contact form link is functional and accessible before directing users

## Output Contract

- Private inquiry successfully redirected to contact form; confirmation that public channels remain free of sensitive data; user receives clear guidance on confidential submission process

## Triggers

- User inquiry contains sensitive business information, personal data, or requires confidential handling; user requests private communication
