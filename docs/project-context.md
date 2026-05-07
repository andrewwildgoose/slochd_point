# slochd_point Project Context

## Project goal
Turn the current early-stage Python proof of concept into a functioning web application that helps users find the **slochd point** on a route: the point at which the **miles completed** equals the **kilometers remaining**.

The application should allow users to:
- import a route
- calculate the slochd point
- view the route and slochd point on a map
- see nearby cafes, pubs, and restaurants
- export the result in a useful format such as GPX

## Recommended MVP
The recommended MVP is:
1. User uploads a GPX file
2. App parses the route and calculates the slochd point
3. App displays:
   - the route on a map
   - a marker for the slochd point
   - key route and distance stats
   - nearby cafes / pubs / restaurants
4. User can export or share the result

### MVP definition
> A user can upload a GPX route, see the exact slochd point on a dark-themed interactive map, view nearby cafes/pubs/restaurants, and export the slochd point as GPX or coordinates.

## Product recommendations

### Map service
Recommended starting approach:
- **MapLibre GL JS** for map rendering
- **OpenStreetMap-based tiles/services** for basemaps and geospatial data
- **OpenStreetMap POI data / Overpass** for nearby cafes, pubs, restaurants

Why:
- better fit than Google Maps for a route-centric, GPX-heavy application
- lower lock-in early on
- better control over styling and dark mode
- easier to align with route export workflows

Google Maps may still be worth considering later if POI quality becomes a major product requirement, but it is not recommended as the first choice for MVP.

### User accounts
Recommended approach:
- **No user accounts for MVP**
- Add optional sign-in later only if needed for saved routes, history, integrations, or paid features

Why:
- lower engineering complexity
- faster path to launch
- lower privacy/compliance burden
- easier onboarding for users

### Route import strategy
Recommended roadmap:
- **Phase 1:** GPX file upload
- **Phase 2:** optional integrations with Strava / Komoot
- **Later:** expanded route sync/import features if justified

Why GPX first:
- simplest to implement
- best fit for outdoor/cycling/hiking users
- avoids early dependency on third-party integrations
- aligns well with export to Garmin and mobile devices

### Export strategy
Recommended MVP export options:
- GPX with a waypoint at the slochd point
- copy coordinates
- shareable result link

Later options:
- GPX containing nearby POI waypoints
- additional export formats such as JSON or CSV

## Front-end and UX direction
The preferred design direction is:
- **dark mode by default**
- **minimal styling**
- **map-first layout**
- route geometry and slochd point are the visual focus

### Suggested pages
#### 1. Landing page
Should include:
- short explanation of the slochd point
- GPX upload CTA
- demo route CTA
- brief “how it works” section

#### 2. Route result page
This is the main application page.

Should include:
- large interactive map
- route polyline
- start and finish markers
- slochd point marker
- nearby POI markers
- route stats panel
- nearby places panel
- export/share controls

#### 3. About / How it works page
Should include:
- explanation of the slochd point concept
- supported input formats
- export notes
- privacy / FAQ content

### Main result page contents
Recommended sections:
- **Map area**
- **Stats panel**
- **Nearby places panel**
- **Export actions**

Suggested stats:
- total route distance
- distance from start to slochd point
- miles completed at slochd point
- kilometers remaining at slochd point
- percentage through route
- coordinates and elevation if available

## Technical recommendations

### Core domain logic
The core route-analysis logic should:
- parse GPX track points reliably
- compute cumulative route distance
- interpolate the exact location where miles completed equals kilometers remaining
- handle noisy data and edge cases carefully

This should be treated as the most important domain logic in the app and should have strong automated test coverage.

### Nearby places logic
For MVP, “nearby” can mean close to the slochd point itself.

Later, nearby-place ranking can be improved by considering:
- distance to the slochd point
- distance from the route
- detour cost
- whether the stop is ahead of or behind the slochd point

### Suggested stack direction
The repository is currently overwhelmingly Python-based. The user is most familiar with **SvelteKit** and **FastAPI**.

Recommended stack choice:
- **Start with SvelteKit only if possible**
- Keep the architecture simple enough for low-cost/free hosting
- Only introduce FastAPI if the backend requirements outgrow what SvelteKit endpoints can comfortably handle

Why SvelteKit-only may be a strong first choice:
- fewer moving parts
- easier deployment on free/low-cost platforms like Netlify
- simpler project structure
- can handle file upload, route parsing, calculation, and export for an MVP

When FastAPI becomes worthwhile:
- heavy geospatial processing
- long-running jobs
- background tasks
- richer integrations with external APIs
- separate API needed for mobile clients or multiple frontends

### Practical stack recommendation
#### MVP stack
- **Frontend + server endpoints:** SvelteKit
- **Map:** MapLibre GL JS
- **Styling:** minimalist CSS approach or Tailwind if desired
- **POI:** OpenStreetMap / Overpass-based lookup
- **Hosting:** Netlify or similar free-tier-friendly option

#### Future stack evolution
If the product grows:
- retain SvelteKit frontend
- add FastAPI backend when separate backend concerns become substantial

## Hosting recommendation
Because the initial goal is free hosting, a **SvelteKit-only MVP** is a sensible approach.

Important note:
- GitHub Pages is not a good fit if the app requires server-side logic for uploads, parsing, Overpass queries, or export generation.
- Netlify (or similar) is a better fit for a SvelteKit app with server endpoints/functions.

Recommended initial hosting path:
- build the MVP in SvelteKit
- host on Netlify or another free-tier platform that supports server functions

## Useful features to prioritize
### High-priority MVP features
1. GPX upload
2. route rendering on map
3. slochd point calculation and marker
4. nearby cafes/pubs/restaurants
5. GPX export with slochd waypoint
6. mobile-friendly dark UI

### Strong next-step features
1. shareable links
2. elevation profile with slochd marker
3. better POI ranking
4. demo routes
5. distance-off-route filtering

### Later features
1. optional user accounts
2. Strava / Komoot import
3. saved routes/history
4. ETA at slochd point
5. weather and opening-hours intelligence
6. “best stop near slochd point” recommendation

## Prioritized backlog themes
### Epic 1: Productionize the slochd calculation engine
- isolate core route math
- add robust tests
- define supported input assumptions
- ensure interpolation and unit conversion are correct

### Epic 2: Build the MVP user flow
- upload GPX
- calculate point
- render map and stats
- show nearby places
- export result

### Epic 3: Improve UX and reliability
- responsive dark-mode interface
- empty states / error states
- better route and POI presentation
- performance tuning

### Epic 4: Add sharing and richer planning features
- shareable links
- elevation profile
- improved POI ranking and route-aware filtering

### Epic 5: Add optional accounts and integrations later
- saved routes
- Strava / Komoot integrations
- user history and preferences

## Recommended use of Copilot agents
Copilot agents will work best if used on **small, clearly-scoped tasks** rather than asking for the entire app at once.

### Good categories of agent tasks
- repo audit and architecture analysis
- isolating and testing the slochd calculation logic
- implementing GPX upload flow
- building the map result page
- adding nearby POI lookup
- implementing GPX export
- refining dark-mode UI and responsive behavior
- generating issue breakdowns and acceptance criteria

### Example agent workflow
1. Ask the agent to explain the current repo and identify the slochd calculation code
2. Ask the agent to propose a minimal architecture for a SvelteKit MVP
3. Ask the agent to implement one feature slice at a time
4. Ask the agent to add tests and document assumptions
5. Ask the agent to polish UX, accessibility, and mobile layout

## Tailored Copilot agent prompts
See `docs/copilot-agent-prompts.md`.

## Backlog / issue plan
See `docs/project-backlog.md`.
