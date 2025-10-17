# PRD & Pitch Update

**Pitch (1 paragraph):**
Explain the refined goal of your AI reflections blog and why it matters to your audience.

## Users & Roles
- Reader (anonymous): view published posts, search
- Author (authenticated): CRUD their posts, comment
- Editor (group permission): publish posts

## Functional Requirements
- Create/Edit/Delete Post with validation
- Comment on posts with moderation rule (future work)
- Search posts (HTMX)

## Non-Functional
- Accessibility (WCAG 2.2), privacy, logging

## Data Model (updated)
- Category, Tag, Post, Comment (see README)

## Acceptance Criteria
- Validation errors when body < 50 chars
- Duplicate titles rejected
- Only Editors can publish
