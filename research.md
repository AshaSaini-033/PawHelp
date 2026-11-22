# Research Notes — PawHelp

## 1. Problem statement (working hypothesis based on the author's report)

1. During a user-reported 20–30 minute visit to NIT Srinagar campus on 2026-11-20, the author covered the Nescafe area, cafeteria, hostel/residential surroundings, college roads, school/college surroundings, streets, park and garbage points.
2. The author reported dogs, cats, cows and calves across these different campus surroundings, not only at one fixed feeding point.
3. According to the author's account, there is no dedicated caretaker known to them; students themselves give food to animals, and campus workers also sometimes provide food.
4. This suggests that animal feeding is informal and depends on individual students' and workers' initiative; the frequency, coordination gaps and availability of helpers still need validation.
5. PawHelp is a small community coordination prototype for recording where help is needed, food offers and volunteer availability, then suggesting compatible matches.

**Evidence boundary:** Visit details and the informal feeding pattern are author-reported. They are not a campus-wide survey or a verified statement from campus administration. Exact animal counts by area, feeding frequency, named interview, photos and 20 individual raw records have not yet been documented.

## 2. Existing alternatives and their fit

| Existing alternative / current practice | What it provides | Possible limitation to validate | What to ask or observe |
|---|---|---|---|
| Students giving food on their own | Immediate help when an individual student notices an animal and has food available, in different campus areas. | Help may depend on who happens to be present; students elsewhere may not know where food or help is currently needed. | Do students coordinate with one another across hostel, cafeteria and other areas? |
| Campus workers sometimes giving food | Another informal source of food and support around campus. | It is not yet clear whether workers coordinate with students or with each other, or whether availability is predictable. | Do workers and students share information about animals and feeding? |

These are based on the author's report and are hypotheses about coordination, not proven shortcomings. If students and workers already coordinate effectively, the product should reflect that rather than invent a problem.

## 3. Sources reviewed

### Source 1 — Animal Welfare Board of India (AWBI): Advisory for animal feeding

- Link: https://awbi.gov.in/uploads/regulations/163310162972Advisory%20for%20animal%20feeding%2025.4.2020.pdf
- Relevant points: The advisory discusses maintaining personal hygiene, identifying a place and time for feeding, coordinating with local authorities where applicable, and following waste-management practices after feeding.
- Relevance to PawHelp: A useful feeding-point record should capture a location and time, and the workflow should encourage clean-up rather than leaving food containers or litter behind.
- Scope note: This is an advisory document; it does not establish the actual feeding rules or needs at NIT Srinagar. Check current local instructions before acting.

### Source 2 — World Organisation for Animal Health (WOAH): Terrestrial Animal Health Code, Chapter 7.7 — Dog population management

- Link: https://www.woah.org/fileadmin/Home/eng/Health_standards/tahc/2024/en_chapitre_aw_stray_dog.htm
- Relevant points: WOAH describes dog population management as a holistic approach involving animal welfare, public health and coexistence. It stresses local context, community engagement, clear stakeholder roles and monitoring.
- Relevance to PawHelp: The tool should support coordination and record-keeping, not claim to solve animal population management, veterinary care or public-health risks by itself.
- Scope note: This chapter concerns dog population management. It should not be treated as species-specific guidance for cats or cattle.

## 4. Product scope

### What the prototype supports
- Record a feeding/help point with its area and relevant details.
- Record a food offer with its type, quantity/unit and availability information.
- Record volunteer availability.
- Generate match suggestions using the available area, food and availability fields.
- Keep records in a simple CSV-backed workflow suitable for a small local prototype.

### What it does not claim to do
- Verify that an animal is present or hungry.
- Replace a conversation with a feeder or local animal-welfare organisation.
- Provide veterinary diagnosis, emergency response or legal advice.
- Guarantee that a food offer is safe, appropriate or delivered.
- Prove a campus-wide coordination gap without further validation.

## 5. Questions to validate the current informal system

1. Do students usually feed animals individually, or do they coordinate with other students across different campus areas?
2. Do students and workers know where help is needed at a given time?
3. Are there particular areas or times when animals are more likely to need food?
4. Would a shared list of feeding points, food offers and volunteer timings help, or would it add extra work?
5. What is one small change that would make the current process easier?

## 6. Decision log — complete after follow-up

- Student/worker spoken to and role (with permission): [not provided yet]
- Whether feeding is spontaneous or coordinated: [not confirmed]
- Specific coordination difficulty they described: [not provided yet]
- Feature they said would help: [not provided yet]
- Feature they did not need: [not provided yet]
- Final narrowed problem statement: [rewrite using confirmed feedback]
