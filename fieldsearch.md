# PawHelp — Field Search Sheet

Use this sheet during the real 20-minute walk. It helps you decide what to observe and what to ask; it is not pre-filled evidence.

## Suggested public-area route

Check only places you can safely and legitimately access. Choose a manageable route and record the actual areas visited.

- [ ] Nescafe / café surroundings
- [ ] Cafeteria entrance or designated public area
- [ ] Hostel public/common area
- [ ] College road / campus road
- [ ] School or college surroundings (from a public place)
- [ ] Street lane / market-side lane
- [ ] Park or public green area
- [ ] Garbage / waste collection point (observe from a safe distance)

## What to record

For each actual check, note:
- Date and time
- Public-area label (avoid private addresses)
- Animal type (dog / cat / cow / calf / other)
- Count only if you actually counted; otherwise write "not recorded"
- Visible behaviour/context, without guessing the animal's condition
- Whether the entry is direct observation or something a person told you

## Ask one person

1. How do you currently coordinate animal feeding or care?
2. What is the most difficult part of that process?
3. Would a shared list of feeding points, food offers and volunteer timings help? Why or why not?

Record their real name and role only with permission. Capture three specific statements and one surprise.

## CSV capture template

Copy this header into a separate working sheet and add only real entries:

    entry_id,date,time,area_label,animal_type,count,behaviour_or_context,source,verification_status,notes

Set source to direct_observation or participant_report. Use "not recorded" for unknown date/time/count only if the actual collection record genuinely lacks that value. Never make up timestamps or counts.

## Important separation

- backend/data.csv: real assignment records only.
- backend/demo-data.csv: synthetic examples for testing the interface; never count these as fieldwork.
- Photographs and interview notes must be personally collected with appropriate permission.
