---
Task ID: 1
Agent: Main Agent
Task: Port ORION-Health frontend from Vite/React to Next.js 16 with significant UI/UX improvements

Work Log:
- Extracted and analyzed the entire orion-frontend.zip codebase (Vite + React 19 + Tailwind v4 + Framer Motion)
- Mapped all 7 routes, 10 API endpoints, WebSocket service, and localStorage hook
- Identified code issues: unused imports, duplicate PatientRegister/PatientInput, build-breaking `glass` utility class, stale App.css
- Designed a new premium dark theme design system with deep navy backgrounds, teal/cyan accents, refined glassmorphism
- Converted architecture from React Router to Next.js App Router with state-based client routing (single `/` route)
- Routed all API calls through Caddy gateway using `XTransformPort=8000`
- Routed WebSocket through gateway with proper protocol detection
- Created 18 new/updated files preserving all original functionality
- Fixed all TypeScript errors (framer-motion Variants typing, checkbox event handling, generic filterPatients, getUrgencyColor return type)
- Verified all pages render correctly via Agent Browser (landing, pre-register, admin layout with all 4 sub-pages)
- Verified responsive behavior on mobile (375x812) and desktop (1440x900)
- Verified sidebar toggle works on mobile

Stage Summary:
- **New files created:** globals.css (design system), orion-config.ts, orion-api.ts, orion-ws.ts, orion-hooks.ts, OrionApp.tsx, LoadingSpinner.tsx, UrgencyBadge.tsx, LandingPage.tsx, PreRegister.tsx, PatientRegister.tsx, AdminLayout.tsx, PatientInput.tsx, DoctorPanel.tsx, EmergencyPanel.tsx, DoctorHistory.tsx, PatientDetailModal.tsx, page.tsx
- **All original API calls preserved** (10 endpoints: preregister, search, fetch, submit, history, patients, emergency, override, logs, health)
- **WebSocket functionality preserved** with gateway routing
- **Shared PatientDetailModal component** eliminates duplicate modal code between DoctorPanel and EmergencyPanel
- **Professional UI/UX**: Lucide icons replace emojis, proper form fields with labels/icons, loading/empty/error states, responsive mobile sidebar, refined animations
- **Zero console errors** during browser verification
