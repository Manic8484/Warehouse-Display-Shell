Warehouse Display Shell
=======================

Purpose
-------
A single-site touchscreen shell for a locked Edge kiosk.
The browser only needs one permitted URL. The shell provides large right-hand
touch tabs and embeds the individual warehouse webapps inside iframes.

Default behaviour
-----------------
- Four tab slots.
- Right-hand rail approx 112 px wide.
- Tabs approx 200 px high.
- Reload / restart ALWAYS returns to Tab 1.
- No localStorage or remembered selected tab.
- Unassigned tabs are disabled.

Environment variables
---------------------
TAB1_LABEL   Warehouse
TAB1_URL     https://warehouse-reporting-263201611680.europe-west2.run.app/

TAB2_LABEL   Movements
TAB2_URL     https://warehouse-movements-263201611680.europe-west2.run.app/board

TAB3_LABEL   Tab 3
TAB3_URL     <optional>

TAB4_LABEL   Tab 4
TAB4_URL     <optional>

Example initial assignment
--------------------------
TAB1_LABEL=Warehouse
TAB1_URL=https://YOUR-WAREHOUSE-REPORTING-URL
TAB2_LABEL=Movements
TAB2_URL=https://warehouse-movements-263201611680.europe-west2.run.app/board

Important: iframe framing
-------------------------
The embedded applications must permit themselves to be framed by the display
shell. If an app sends X-Frame-Options: DENY/SAMEORIGIN or a restrictive
Content-Security-Policy frame-ancestors directive, it will need a small header
change. If that happens, the shell itself is still fine; adjust the embedded
app's response headers.

Endpoints
---------
GET /
GET /health

Kiosk concept
-------------
Edge can remain in the restrictive single-site kiosk mode and open only the
warehouse-display URL. Operators change between apps using the large on-screen
tabs rather than browser tabs.
