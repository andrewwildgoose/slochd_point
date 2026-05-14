# slochd_point Project Context

## Overview
`slochd_point` began as an early-stage Python proof of concept for calculating a route milestone called the **slochd point**: the point at which the **miles already completed** equals the **kilometers still remaining**.

The project direction is now to turn that proof of concept into a real web application that people can use to upload routes, calculate the slochd point, view it on a map, inspect nearby food/drink stops, and export the result for use in other navigation tools.

This document is intended to preserve the current product and technical thinking so that future requests to Copilot or other agents can start with the right context.

---

## Core product idea
The application should help a user answer:

> “Where on my route is the point where my miles done equals my kilometers to go?”

This is the defining piece of domain logic and the core differentiator of the app.

The initial target user is likely someone planning or following a route for activities such as:
- cycling
- running
- walking / hiking
- general route planning

The product becomes more useful when it does not just calculate the point, but also helps the user make decisions around it — for example by showing **nearby cafes, pubs, and restaurants** and by making it easy to export the location back into route-following tools.

---

## Target outcome
Move from:
- a Python POC

to:
- a functioning, polished, low-cost-to-host web app

The first meaningful version should let a user:
1. upload a route
2. calculate the slochd point
3. see the route and the slochd point on an interactive map
4. see nearby cafes / pubs / restaurants
5. export the slochd point in a useful format

---

## Recommended MVP
The current recommended MVP is:

1. **GPX upload**
   - user uploads a GPX route file
2. **Route analysis**
   - app parses the route and calculates the slochd point
3. **Result view**
   - app shows the route on a map
   - app shows a clearly marked slochd point
   - app shows key stats about the result
4. **Nearby places**
   - app shows nearby cafes, pubs, and restaurants around the slochd point
5. **Export**
   - user can export the slochd point as GPX and/or copy coordinates

### MVP definition
> A user can upload a GPX route, see the exact slochd point on a dark-themed interactive map, view nearby cafes/pubs/restaurants, and export the slochd point as GPX or coordinates.

This is intentionally narrow. The aim is to ship something useful before adding accounts, integrations, or advanced route-planning features.

---

## Product decisions so far

### 1. Map stack
Current recommendation:
- **MapLibre GL JS** for rendering the map
- **OpenStreetMap-based tiles/services** for basemaps
- **OpenStreetMap / Overpass data** for nearby places

Reasoning:
- the app is route-centric and GPX-centric rather than business-listing-centric
- this keeps the stack flexible and less locked into a proprietary provider
- it is a good fit for custom styling and dark mode
- it aligns better with route data export and outdoor tooling than starting with Google Maps

Google Maps is not ruled out forever, but the current recommendation is **not** to start there. It may become worth revisiting later if place data quality becomes a major limitation.

### 2. User accounts
Current recommendation:
- **do not require user accounts for MVP**

Reasoning:
- reduces complexity
- lowers privacy/compliance burden
- makes it easier for a new user to try the app
- speeds up delivery

Accounts can be reconsidered later if the app needs:
- saved routes
- route history
- integrations (for example Strava or Komoot)
- cross-device sync
- paid features

### 3. Route import
Current recommendation:
- **start with GPX upload**
- consider Strava / Komoot / other integrations later

Reasoning:
- GPX upload is simple and practical
- it suits outdoor route users well
- it avoids the complexity of OAuth and third-party APIs at the start
- it works naturally with export back to devices and apps

### 4. Export
Current MVP export options should be:
- GPX with a waypoint at the slochd point
- copy coordinates

Potential later additions:
- shareable result links
- GPX with nearby POI waypoints
- JSON/CSV output if useful for debugging or API usage

---

## UX and design direction
The design preference is:
- **dark mode by default**
- **minimal styling**
- **map-first experience**

The UI should feel more like an outdoor/navigation tool than a busy consumer travel website.

### Design principles
- the route and slochd point should be the visual focus
- the map should dominate the result page
- the interface should use strong hierarchy and restrained color
- panels should be compact and useful rather than decorative
- mobile usability should be considered early

### Suggested visual style
A suitable style direction is:
- near-black / charcoal backgrounds
- subtle panel separation
- a cool accent color for the route
- a warm/high-contrast accent for the slochd point marker
- muted but distinct styling for cafe/pub/restaurant markers
- good contrast but not harsh pure white everywhere

### Recommended page structure
#### Landing page
Should contain:
- simple explanation of what the slochd point is
- upload CTA
- optional “try a demo route” CTA
- brief “how it works” section

#### Result page
This is the main page of the app.

Should contain:
- large map area
- route polyline
- start and finish markers
- slochd point marker
- nearby place markers
- stats panel
- nearby places panel
- export actions

#### About / How it works page
Should contain:
- explanation of the slochd point concept
- supported file types
- export notes
- privacy and FAQ material

---

## Main result page: recommended content
The result page should communicate the answer quickly.

### Map section
Should show:
- the full route
- start marker
- finish marker
- slochd point marker
- nearby place markers
- optional highlighted segment around the slochd point

Useful controls may include:
- fit route to view
- center on slochd point
- toggle nearby places on/off
- filter place categories later

### Stats panel
Suggested fields:
- route name if available
- total route distance
- distance from start to slochd point
- miles completed at slochd point
- kilometers remaining at slochd point
- percentage through route
- coordinates
- elevation if route data supports it

### Nearby places panel
Suggested information per place:
- name
- type/category
- approximate distance from slochd point
- later: distance off route, opening info, external nav links

### Export area
Suggested actions:
- download GPX with slochd waypoint
- copy coordinates
- later: share result link

---

## Core technical priorities

### 1. Correct slochd-point calculation
This is the heart of the app.

The implementation must:
- parse route geometry reliably
- compute cumulative distance along the route
- convert units consistently
- find the exact location where miles completed equals kilometers remaining
- interpolate between route points rather than just picking the nearest point

This logic should have strong automated tests.

### 2. Define “nearby” clearly
For MVP, “nearby” can simply mean:
- places geographically near the slochd point itself

Later, better route-aware logic could consider:
- distance to the slochd point
- distance from the route
- likely detour cost
- whether the place is ahead of or behind the point on the route

### 3. Export compatibility
The GPX export should be treated as an actual product feature, not an afterthought.

The exported file should ideally:
- include a waypoint for the slochd point
- use sensible naming
- be tested against common tools such as Garmin workflows and common mobile mapping apps if possible

---

## Current stack thinking
The repository today is overwhelmingly Python. The current user preference and familiarity is:
- **SvelteKit frontend**
- **FastAPI backend**

Current recommendation:
- **start with SvelteKit only if possible**
- do not add FastAPI until it becomes clearly useful

### Why SvelteKit-only is recommended for MVP
SvelteKit should be sufficient for:
- file upload
- server-side parsing/processing in endpoints/functions
- slochd-point calculation
- nearby place lookup
- export generation

Benefits:
- one codebase
- lower complexity
- easier deployment
- better fit for free or low-cost hosting
- faster iteration

### When FastAPI would become worth adding
FastAPI becomes more attractive if the app later needs:
- heavy geospatial processing
- long-running or queued jobs
- richer external integrations
- a separate public API
- shared backend for multiple clients
- significant reuse of Python geo libraries that would be hard to replace

### Practical recommendation
For the first real version:
- use **SvelteKit** as the main app framework
- keep the current Python implementation as a reference while rebuilding the production path
- only add a separate Python backend later if real needs justify it

---

## Hosting recommendation
Because the goal is to host for free initially, the best-fit recommendation is:
- **SvelteKit deployed to Netlify or a similar platform that supports server functions**

Important note:
- **GitHub Pages is not a good fit** if the app needs upload handling, server-side processing, Overpass lookups, or export generation.
- A fully static deployment would make the app architecture more awkward than necessary.

So the current recommendation is:
- do **not** optimize around GitHub Pages
- optimize around a simple SvelteKit deployment that still allows server-side functionality

---

## Recommended phased roadmap

### Phase 0 — Understand and stabilize the POC
Goals:
- audit the current Python repo
- identify where the existing slochd calculation lives
- document assumptions and limitations
- create test fixtures and validate the core math

### Phase 1 — Deliver the MVP
Goals:
- GPX upload
- route parsing
- production-ready slochd calculation module
- map result page
- nearby places around the slochd point
- GPX export with waypoint
- dark, minimal, mobile-friendly UI

### Phase 2 — Improve usability and quality
Goals:
- shareable links
- demo routes
- stronger mobile polish
- better error states
- elevation profile with slochd marker
- improved POI ranking

### Phase 3 — Add richer planning features
Goals:
- distance-off-route filtering
- “best stop near slochd point” recommendation logic
- better export options
- stronger route-aware place suggestions

### Phase 4 — Add optional accounts/integrations if justified
Goals:
- saved routes/history
- user accounts only if there is a clear product need
- Strava / Komoot imports if they become worthwhile

---

## High-priority features
The current highest-priority features are:
1. GPX upload
2. route rendering on a map
3. accurate slochd-point calculation
4. nearby cafes/pubs/restaurants
5. GPX export with slochd waypoint
6. clean dark-mode responsive UI

These represent the core usable product.

---

## Strong next-step features after MVP
Recommended next additions after the MVP:
1. shareable result links
2. demo routes
3. elevation profile with slochd marker
4. better POI ranking
5. distance-off-route filtering

---

## Later features
Possible later additions if the product gains traction:
1. optional user accounts
2. saved routes/history
3. Strava import
4. Komoot import
5. ETA to slochd point
6. weather/opening-hour intelligence
7. “best stop near slochd point” scoring

---

## How Copilot agents should be used on this project
Copilot and other agents will be most effective when given **small, well-scoped tasks**.

### Good uses of agents
- audit the existing Python POC
- locate and explain the current slochd calculation code
- propose a SvelteKit MVP structure
- implement GPX upload
- implement route parsing
- implement the calculation module
- build the result page
- add nearby-place lookup
- implement GPX export
- add test coverage
- improve accessibility and mobile UX

### Good prompt style
Ask for:
- one feature at a time
- acceptance criteria
- tests
- explicit tradeoffs
- small PR-sized chunks

### Less useful prompt style
Avoid vague requests like:
- “build the whole app”
- “make this production-ready” without specifics
- “rewrite everything”

---

## Related context files
Additional context and planning docs should live alongside this file.

Recommended related files:
- `docs/copilot-agent-prompts.md` — reusable prompts tailored to this repo
- `docs/project-backlog.md` — prioritized backlog / issue breakdown

---

## Current strategic recommendation
If future agents need one short summary to anchor decisions, it is this:

> Build a SvelteKit-first MVP that lets users upload GPX routes, calculate the slochd point accurately, view it on a dark map, inspect nearby cafes/pubs/restaurants, and export the result — while keeping hosting simple and free-tier-friendly, and avoiding premature complexity such as accounts or a separate FastAPI backend.
