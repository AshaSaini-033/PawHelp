# AI discussion 01 — PawHelp idea, pros, cons and problem selection

**Purpose:** Record the planning discussion used to evaluate PawHelp before implementation.

**Important note:** This is a structured summary of the assistance discussed in ChatGPT, not a word-for-word transcript. The questions below are reconstructed topic prompts, not exact quotations.

## 1. What problem were we trying to solve?

The project direction was narrowed to a local community-dog feeding coordination tool. A regular feeder may know which feeding point needs attention, a donor may have suitable food, and another person may have time to help. These details can remain separated across conversations, so coordination becomes difficult.

The idea was not to build an emergency animal-rescue dispatch system. Rescue response would require trained responders, transport, veterinary support and reliable funding—things a student MVP cannot guarantee.

## 2. What are the possible benefits?

- **Local and understandable problem:** It focuses on a real activity—people caring for community dogs—rather than an artificial app idea.
- **Several ways to participate:** A person can report a confirmed feeding point, offer suitable food, or share a time window when they can volunteer.
- **Better visibility:** A feeder can see recorded needs and offers in one place instead of relying only on separate messages.
- **Coordination support:** The app can show candidate combinations of a feeding point, a compatible food offer and a volunteer who says they are available.
- **Continuity:** A last-confirmed-visit time and a check interval can highlight points that may need a follow-up.
- **Measurable project output:** The system can count recorded points, offers, volunteers, overdue reminders and suggested matches.

## 3. What are the risks or disadvantages?

| Risk / limitation | Why it matters | MVP response |
|---|---|---|
| No volunteer is available | Software cannot make a person appear or transport food | Keep the need visible as unresolved; do not label it completed |
| Fake or outdated reports | People may travel based on incorrect information | Record who confirmed the information and when; verify before acting |
| Food may be unsuitable | Incorrect food can harm animals | Only record food categories approved by an experienced local feeder; the app gives no diet advice |
| Duplicate reports or visits | Two people may act on the same need | Use record IDs and ask a local coordinator to verify before a visit |
| Trust and delivery confirmation | A match does not prove food was collected or delivered | Separate a suggested match from a real-world confirmation |
| Volunteer availability changes | A person may become busy after submitting availability | Use short availability windows and reconfirm outside the app |
| Location privacy | Exact feeding spots or personal details may be sensitive | Use broad area labels; avoid publishing home addresses or phone numbers |
| Volunteers stop participating | A one-time contribution may not create a reliable routine | Keep the MVP small and let a local feeder coordinate repeat visits |

## 4. How did we decide to address the risks?

We chose a conservative workflow:

1. A feeder confirms the feeding point and the need.
2. A donor records a real food offer, its quantity and when it is valid.
3. A volunteer records when they are genuinely available.
4. PawHelp checks compatibility and displays a **suggestion**, not an assignment.
5. People contact each other using an already agreed local channel.
6. The feeder/coordinator confirms the outcome before anyone records a visit as completed.

No payment gateway, public chat, live tracking, automatic dispatch or AI animal recognition was included. Those features would add complexity without solving the first coordination question.

## 5. What is the main product decision?

A basic donation listing app would be generic. The more specific project angle is **making local feeding-point check-ins and food/volunteer availability visible together**, then highlighting possibly overdue points and suggesting compatible help.

This is only a useful solution if a real local feeder confirms that coordination is a problem. If fieldwork reveals a different bottleneck, the product should change to match that person's needs.

## 6. What should not be claimed?

- A suggested match is not a confirmed delivery.
- An overdue reminder does not prove that dogs have not been fed.
- The app cannot assess hunger, health, diet or urgency.
- The app does not guarantee that a volunteer will accept a task.
- A recorded food quantity is not proof that an animal consumed it.

## Outcome

The discussion supported building a small, explainable coordination MVP and testing it with one real feeder. It did not establish that the problem exists at every location or that the system will automatically improve animal welfare.
