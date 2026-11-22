# PawHelp — My Field Search Sheet

I use this sheet to guide a real 20-minute walk. It helps me decide what to observe and what to ask; it is not pre-filled evidence.

## Public-area route I can use

I will check only places I can safely and legitimately access. I will choose a manageable route and record the areas I actually visit.

- [ ] Nescafe / café surroundings
- [ ] Cafeteria entrance or designated public area
- [ ] Hostel public/common area
- [ ] College road / campus road
- [ ] School or college surroundings (from a public place)
- [ ] Street lane / market-side lane
- [ ] Park or public green area
- [ ] Garbage / waste collection point (observe from a safe distance)

## What I will record

For each actual check, I will note:
- Date and time
- Public-area label (avoid private addresses)
- Animal type (dog / cat / cow / calf / other)
- Count only if I actually counted; otherwise write "not recorded"
- Visible behaviour/context, without guessing the animal's condition
- Whether the entry is my direct observation or something a person told me

## Questions I can ask one person

1. How do you currently coordinate animal feeding or care?
2. What is the most difficult part of that process?
3. Would a shared list of feeding points, food offers and volunteer timings help? Why or why not?

I will record their real name and role only with permission. I will capture three specific statements and one surprise only if the person actually shares them.

## CSV capture template

I can copy this header into a separate working sheet and add only real entries:

    entry_id,date,time,area_label,animal_type,count,behaviour_or_context,source,verification_status,notes

I will set source to direct_observation or participant_report. I will use "not recorded" for an unknown date/time/count only if my actual collection record genuinely lacks that value. I will not make up timestamps or counts.

## Keep the datasets separate

- backend/data.csv: my real assignment records only.
- backend/demo-data.csv: synthetic examples for testing the interface; I will never count these as fieldwork.
- Photographs and interview notes must be personally collected by me with appropriate permission.
