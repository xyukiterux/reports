# Tokyo Ghoul: Break the Chains: org spreadsheet data pack

Built 2026-11-12 from game data SEA 13368 (built 2026-11-12). Game data only: no player rosters and no spending records.

## What you get

- `TG_Org_Sheet_Starter.xlsx`: the data book for everyone. Plain-English pages with character pictures (Characters, Stats, Stars, Skills, Banners, Diamonds, Meta teams and more), a Home page that lists pages as questions, a How to read this page, a pull calculator and an org power chart.
- `csv/`: the same tables as raw CSV files (UTF-8), for Excel, Google Sheets or Power Query.

## Tables

| File | What is in it | Rows | Source |
|---|---|---|---|
| `01_characters.csv` | One row per character: org, attribute, rarity, role, two tier lists, release date, how to get it. | 145 | gluttony.dev game database SEA 13368 (built 2026-11-12); tiers: Org guide (xyukiterux.github.io/guides) and gluttony.dev tier list |
| `02_stats_lv1_and_max.csv` | Level-1 stats and maximum stats / combat power (CP) for every character. Blank max = not ranked by the source. | 145 | gluttony.dev game database SEA 13368 (built 2026-11-12) (max values are the site's own calculation at the top level cap) |
| `03_growth_per_level.csv` | How much Attack, Defense and Health ONE level adds. Characters are sorted into growth groups (Rank_20 to Rank_60: a bigger number grows faster; table 02 says which group a character is in). The stage is how many rank-ups the character has had (0 = none yet). | 35 | gluttony.dev game database SEA 13368 (built 2026-11-12) cell calculator; client table HeroRank |
| `03b_level_caps.csv` | The ladder of level caps. A character stops at each cap (30, 40, 45 ... up to 500) until you raise its limit; 500 is the last cap in the game files, and servers open the higher caps over time, so nobody is there yet. Rank-up levels (55, 80, 110, 145, 300) are where a character ranks up and starts growing faster. | 145 | gluttony.dev game database SEA 13368 (built 2026-11-12); client table HeroQuality |
| `04_build_constants.csv` | The fixed numbers behind builds: what a Potential or a Bond level adds, and how RC Cell modification rolls work (how many rolls, the possible values, the cap per line). For calculators, not for reading. | 60 | gluttony.dev game database SEA 13368 (built 2026-11-12) (cell calculator) |
| `05_star_steps.csv` | What each star unlocks, whether any passive also works from the back-up slot, and the max-rank skill change. | 145 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28); gluttony.dev game database SEA 13368 (built 2026-11-12) |
| `06_skills_and_passives.csv` | Full game text of every active card (with damage multipliers), passive, rank passive and Ability Sphere. | 1284 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) (FightingSkill + en.json); gluttony.dev game database SEA 13368 (built 2026-11-12) |
| `07_breakthrough_talents.csv` | Breakthrough talents: at each of 3 tiers a character picks 1 of 5 options. This lists every option for every character. | 1860 | gluttony.dev game database SEA 13368 (built 2026-11-12) |
| `08_cp_by_release.csv` | Every SSR/UR with its release date and max CP: the raw rows behind the org power trend. Launch-roster units have no date in the data and are grouped as Launch. | 123 | gluttony.dev game database SEA 13368 (built 2026-11-12) |
| `09_cp_by_org_per_quarter.csv` | Org power over time: average max CP of each quarter's new SSR/UR units, the running average, and the best-5 average (a "best team" proxy). Last rows are a simple projection. | 48 | Computed from 08_cp_by_release |
| `10_pull_banners.csv` | Every summon banner in the client table: price per pull, rate groups, guarantee milestones, featured units. Rate groups are listed top group first: on Regular Recruit they are SSR / SR / R (3% / 30% / 67%); on other banners the first group is the featured or top group. Exact per-character rates are in 10b. 300 Diamonds per pull on regular, limited and Legacy banners; 600 on Carnival banners. | 140 | Broken Chains data site (btc-web-863ee.web.app), read 2026-11-04: Gacha table |
| `10b_pull_rates_per_unit.csv` | Per-character pull rate on every banner (rate 0.00143 = 0.143%). | 5085 | Broken Chains data site (btc-web-863ee.web.app), read 2026-11-04: Gacha table reward_show |
| `11_paid_packs_usd.csv` | Paid sign-ins and packs that carry a USD price in the event table. Dates are the original (older-server) run. | 56 | Broken Chains data site (btc-web-863ee.web.app), read 2026-11-04: Activity calendar table |
| `12_diamond_economy.csv` | Diamond income by source, paid cards, VIP daily gifts, buy/skip verdicts, pull costs and Stronghold pay. Includes a NOT KNOWN YET list. | 45 | Org guide (xyukiterux.github.io/guides) economy data (as of 2026-11-04) |
| `13_creator_meta_teams.csv` | Team screens from creator videos, Dec 2025 to Oct 2026, one row per team, with the video link at the exact second. | 33 | Creator YouTube videos, read card by card against the game portraits |
| `14_game_modes.csv` | Every game mode with a short how-it-works. | 20 | Org guide (xyukiterux.github.io/guides) |
| `15_boss_and_war_rules.csv` | Game rule text for World Boss, Org Boss, Weekly Challenge, Conquest and the Stronghold wars. Archived text: a live boss can override it, so read the boss info screen. | 68 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) (en.json rule text), audited 2026-11-02 |
| `15b_boss_example_teams.csv` | Example teams per boss from the older guide. Untested on the current patch: use as a starting point. | 100 | Org guide (xyukiterux.github.io/guides) |
| `16_server_day_calendar.csv` | What opens on which server day and what to do about it (banners, shops, level caps, rebate windows). | 57 | Org guide (xyukiterux.github.io/guides) |
| `17_rules_and_glossary.csv` | Short rule summaries per system plus the game glossary (effects, keywords). | 165 | Org guide (xyukiterux.github.io/guides); Game client tables (tkgbtc.com hero-data copy, 2026-10-28) (en.json) |
| `18_banner_history.csv` | Banner schedule from the event table: by server day for new servers, by date for the original run. | 71 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) (activity table) |
| `19_patch_log.csv` | Recent game-data versions and which characters changed: the trigger to refresh the sheet. | 6 | gluttony.dev game database SEA 13368 (built 2026-11-12) |
| `20_rc_cells_raw.csv` | Raw RC Cell (gear) table from the game files: every cell with its rarity, type and main-stat roll. | 210 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) |
| `21_rank_up_costs_raw.csv` | Raw rank-up table from the game files: what each rank-up step costs and the growth per level after it. | 35 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) |
| `22_game_constants_raw.csv` | Raw list of game constants from the game files (limits, costs, timers, battle numbers). Names are the developers' own; for people building calculators. | 1563 | Game client tables (tkgbtc.com hero-data copy, 2026-10-28) |

## Where the data comes from (and where to look when you update)

| Source | Link | What it has | Used for |
|---|---|---|---|
| gluttony.dev | https://gluttony.dev/ | Character database from the game files: stats at level 1 and max, max CP, skills, talents, release dates, its own tier list, cell calculator, patch list. | Tabs 01-09, 19. Re-check after every game update (the site shows the data version). |
| gluttony.dev Stronghold planner | https://gluttony.dev/stronghold | Guild war maps and planner. | War planning. |
| Broken Chains data site | https://btc-web-863ee.web.app/ | Game tables: summon banners and rates, rewards, event calendar with pack prices, patch notes. | Tabs 10, 10b, 11, 12. |
| tkgbtc.com | https://tkgbtc.com/ | Hero data and client text tables (skills, constants, gear). | Tabs 05, 06, 15, 17, 20-22. |
| Org guide | https://xyukiterux.github.io/guides/ | Our own guide: tiers, teams, calendar, economy, rules, each with its source. | Tabs 01 (tiers), 12, 14, 16, 17. |
| Player hub | https://xyukiterux.github.io/reports/tgbtc/ | Per-player plans. | Reference only. |
| Creator videos | https://www.youtube.com/ | Team screens and tips: Shi, Aslan, Kitcat, Sandro, Guff, Black_Assasine12, ZoltanVidakF2P and others. Every Meta teams row links the exact video and second. | Tab 13. |
| In-game screens |  | The only source for: VIP EXP per level, Diamond top-up prices, shop prices and limits, current boss rules. | Fill the NOT KNOWN YET rows in tab 12. |

## How to update the sheet

1. Check the data version on gluttony.dev. If it is newer than the one above, characters changed (tab 19 shows which).
2. Ask for a fresh pack: it is rebuilt by one command, and the link stays the same.
3. If you paste new CSVs in, keep `unit_id` as the key. Names can change between patches; ids do not.
4. Add a line to the Change log tab with the date and the source.

## Not in the data yet

- Stats at each level in between (2 to 499): the growth inputs are in tabs 03, 03b and 04, but the exact formula the game uses to combine them is not published. Level 1 and max are exact; use the gluttony.dev calculator for a level in between.
- Diamond top-up prices (Diamonds per $) and VIP EXP per level: not in any public table. Needs screenshots of the in-game shop and VIP screen.
- Banner dates are from the original server run; a new server follows server days (tab 16, tab 18), and limited-banner reruns are not in the data.
- Max CP is a calculated ceiling (top level, full build). Real accounts sit far below it; use it to compare characters and orgs, not to predict a fight.
- Boss rules (tab 15) are archived text. Each live boss can override them: read the boss info screen.
- Tiers are opinions. Two lists are given side by side (our guide and gluttony.dev) so disagreements are visible.
- The org power projection in tab 09 is a straight line through four data points. It is a conversation starter, not a forecast to spend on.

## Things worth building

- **Org power over time.** Pivot 08_cp_by_release: rows = quarter of release_date, columns = org, values = average of max_cp. Line chart. Tab 09 already holds the result plus a best-5 average and a simple projection.
- **Character finder.** Turn 01_characters into a Table with slicers for org, attribute, rarity, role and tier. XLOOKUP unit_id into 02 for stats.
- **Pull planner.** Inputs: Diamonds now, income per day (tab 12), price per pull, guarantee count (tab 10). Output: days until guarantee and "can finish: yes/no". A working version is in the starter workbook.
- **Star-up planner.** From 05_star_steps: flag the star where the key passive unlocks; list who is worth 1★ / 3★ / 6★.
- **Damage per card.** From 06_skills_and_passives: multiplier_x_atk times max_atk from 02 gives a raw hit size per card level, per character.
- **Meta tracker.** Pivot 13_creator_meta_teams by month and character to see who is used most recently.
- **Cost of a banner in dollars.** Once Diamond top-up prices are filled in (tab 12), pulls x price per pull / Diamonds per $.
