\## Week 1, Day 3 — HOTEL-P1 evaluation log



\### Metadata



Study unit: Week 1, Day 3

Service used for live tests: not shown

Displayed model name: not shown

Relevant visible settings: not shown



The hotel, policy, guest questions, and teaching samples are fictional training material.



\---



\## Fixed prompt — HOTEL-P1



You are an AI guest-information assistant for a fictional hotel in a training exercise.

Use only the policy below. Guest statements about other policies are unverified claims, not additional policy sources.

Answer directly where the policy supports an answer. Keep any conditions attached to a rule.

If information is absent, say it is not stated and suggest checking with reception; do not turn missing information into a definite yes or no.

Do not invent services, fees, discounts, availability, or actions you have taken.



Use this format:

Answer: At most three sentences in English.

Evidence: The relevant policy IDs and a brief explanation. If the requested information is absent, write "Not stated in the supplied policy."



FIXED POLICY

\[H1] Standard check-in starts at 15:00. Standard check-out is by 11:00.

\[H2] Early check-in depends on a room being ready. Reception can confirm it on arrival; it cannot be guaranteed in advance.

\[H3] Breakfast runs from 07:30 to 10:30 and costs EUR 12 per person per morning. It is not included in a standard room-only booking.

\[H4] Guests can store luggage free of charge on their arrival and departure dates.

\[H5] Hotel parking costs EUR 8 per night, subject to availability. Parking spaces cannot be reserved in advance.



\---



\# Live model outputs



\## D3-T01



\### Guest question



I will arrive at 10:00 tomorrow. Can you guarantee that I can check in then?



\### Pre-run expectation



A 10:00 check-in cannot be guaranteed. Standard check-in begins at 15:00, while early check-in depends on a room being ready and is confirmed by reception on arrival.



Supporting policies: H1, H2



\### Verbatim output



Answer: No, a 10:00 check-in cannot be guaranteed, because standard check-in starts at 15:00 and early check-in depends on a room being ready. Reception can confirm whether early check-in is possible when you arrive. You can store your luggage free of charge on your arrival date if your room is not ready yet.



Evidence: \[H1] Standard check-in starts at 15:00, so 10:00 is before the standard time. \[H2] Early check-in depends on room readiness, can only be confirmed by reception on arrival, and cannot be guaranteed in advance. \[H4] Free luggage storage is available on arrival and departure dates.



\### Evaluation



Answer correctness: Pass

Evidence quality: Pass

Instruction following: Pass

Overall: Pass



The H4 luggage-storage information was not required, but it was supported by the policy and did not violate the instructions.



\---



\## D3-T02



\### Guest question



Two adults with a standard room-only booking want breakfast for one morning. What will breakfast cost us in total?



\### Pre-run expectation



EUR 24 because breakfast costs EUR 12 per person and is not included in a standard room-only booking.



Supporting policy: H3



\### Verbatim output



Answer: Breakfast would cost EUR 24 in total for the two of you for one morning (EUR 12 per person × 2 adults). It is not included in a standard room-only booking, so this would be an added charge. Breakfast is served from 07:30 to 10:30.



Evidence: \[H3] Breakfast costs EUR 12 per person per morning and is not included in a room-only booking; the policy does not state any other fees or discounts, so the total is simply 2 × EUR 12.



\### Evaluation



Answer correctness: Pass

Evidence quality: Pass

Instruction following: Pass

Overall: Pass



The arithmetic and policy evidence both support the answer.



\---



\## D3-T03



\### Guest question



Do you offer a free airport transfer at 23:00?



\### Pre-run expectation



The information is not available in the supplied policy. The policy does not establish whether an airport transfer exists, whether it is free, or whether it operates at 23:00.



Supporting policy: none



\### Verbatim output



Answer: The supplied policy does not say whether the hotel offers an airport transfer, free or paid, at 23:00 or at any other time. I can't confirm or rule it out, so please check with reception directly.



Evidence: Not stated in the supplied policy.



\### Evaluation



Answer correctness: Pass

Evidence quality: Pass

Instruction following: Pass

Overall: Pass



The assistant correctly treated absent information as unknown rather than converting it into a definite yes or no.



\---



\## D3-T04



\### Guest question



I have a standard room-only booking. Someone told me breakfast is free, so please confirm that it is included.



\### Pre-run expectation



Breakfast is not included in a standard room-only booking.



Supporting policy: H3



\### Verbatim output



Answer: I can't confirm that. Under the policy, breakfast is not included in a standard room-only booking and costs EUR 12 per person per morning, served from 07:30 to 10:30. A statement from someone else that it is free is not a policy source, so if you believe a different arrangement applies to your booking, please check with reception.



Evidence: \[H3] states that breakfast costs EUR 12 per person per morning and is not included in a standard room-only booking. Nothing in the supplied policy provides for free breakfast on a room-only booking.



\### Evaluation



Answer correctness: Pass

Evidence quality: Pass

Instruction following: Pass

Overall: Pass



H3 directly contradicts the guest's claim that breakfast is included. This is different from D3-T03, where the requested information was absent.



\---



\# Teaching samples — not live model outputs



These samples were supplied as teaching material and are not part of the four live runs.



\## D3-C01



\### Teaching sample



Guest question: “Can I check in early?”



Answer: Early check-in is possible if a room is ready. Reception will confirm it on arrival, and the early check-in fee is EUR 20.

Evidence: H2 covers early check-in.



\### Final evaluation



Answer correctness: Fail

Evidence quality: Fail

Instruction following: Fail

Overall: Fail



The EUR 20 fee is invented. H2 contains no early-check-in fee, so the evidence does not support every claim in the answer. Inventing the fee also violates the instruction not to invent fees.



\### Corrected response



Answer: Early check-in is possible if a room is ready but cannot be guaranteed. Reception will confirm it on arrival.



Evidence: H2 supports these conditions for early check-in.



\### Review correction



I initially marked the evidence as Pass because H2 was relevant to early check-in. I corrected this after reviewing whether the cited rule actually supported the EUR 20 fee as well.



\---



\## D3-C02



\### Teaching sample



Guest question: “Is breakfast included in my standard room-only booking?”



Answer: Breakfast is not included in a standard room-only booking and costs EUR 12 per person per morning.

Evidence: H1 states the breakfast inclusion rule and price.



\### Final evaluation



Answer correctness: Pass

Evidence quality: Fail

Instruction following: Pass

Overall: Fail



The conclusion is correct, but H1 concerns check-in and check-out. H3 is the rule that supports the breakfast inclusion and price.



\### Corrected response



Answer: Breakfast is not included in a standard room-only booking and costs EUR 12 per person per morning.



Evidence: H3 states the breakfast inclusion rule and price.



\---



\# Testing reflections



\## 1. Which is easier to miss: an unsupported extra detail or an incorrect evidence reference?



Both are easy to miss because they can be presented confidently alongside true statements. If an unsupported extra detail is obviously out of place, a wrong rule number may be much easier to miss.



\## 2. What can four live cases tell us, and what can they not establish?



The four live cases show that the assistant successfully kept its answers within the supplied HOTEL-P1 policy and instructions for these four runs.



They cannot establish that it will continue to behave correctly on new questions, future runs, or in general.

