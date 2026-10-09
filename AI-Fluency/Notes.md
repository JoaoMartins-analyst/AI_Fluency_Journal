\# AI Fluency Notes



\## Week 1, Day 1



\*\*Date:\*\* 2026-10-02

\*\*Status:\*\* Completed and reviewed



\### Topics studied



\- Anthropic’s 4D framework.

\- Collaborating with AI on creative work.

\- Exploring familiar and unfamiliar subjects with AI.

\- Evaluating an assistant against an approved information source.

\- Understanding what a small set of tests can establish.



\### The 4D framework



\*\*Delegation:\*\* Decide which tasks to handle myself and which to assign to AI. Keep responsibility for goals and final decisions.



\*\*Description:\*\* Communicate the task, context, constraints and expected output clearly.



\*\*Discernment:\*\* Evaluate whether the response is accurate, useful and supported by the available information.



\*\*Diligence:\*\* Use AI responsibly, acknowledge its contribution and take responsibility for the work I share.



\### What I learned



\- My existing knowledge helps me evaluate AI responses on familiar subjects.

\- When learning an unfamiliar subject, a clear explanation can be useful while still containing claims worth checking.

\- A typical numerical range should not automatically be treated as a definition or rule.

\- Related statements in a source can resolve an apparent ambiguity.

\- An assistant can express unnecessary uncertainty even when the source supports a clear answer.

\- A correct main answer does not automatically make every additional detail correct.

\- Five tests provide evidence about five cases, rather than proof of general reliability.



\### Things I struggled with



After completing the FAQ exercise, I initially did not know what remained untested.



My first conclusion about the assistant’s ability to follow instructions was too broad. I learned to distinguish observed results from claims about its behaviour in other situations.



\### AI explanation and feedback



ChatGPT reviewed my written exercise answers and test summaries.



The feedback helped me understand the ticket-age failure, the limitations of a small test sample and the importance of preserving exact responses.



The review assessed my summaries; the original assistant responses were not included.



\### Habits to carry forward



\- Define the expected behaviour before judging the response.

\- Compare the answer with the complete relevant source.

\- Record the exact response whenever possible.

\- Explain why each test passes or fails.

\- Identify what remains uncertain or untested.



\### Related work



The three Anthropic exercises and the Oceanário FAQ testing exercise are recorded in exercises.md.



\### Sources



\- \[Anthropic — The 4D Framework](https://academy.claude.com/courses/ai-fluency-framework-foundations/the-4d-framework)

\- \[Oceanário de Lisboa — FAQs](https://oceanario.pt/en/faqs/)

\- \[MLB — Four-Seam Fastball](https://www.mlb.com/glossary/pitch-types/four-seam-fastball)

## Week 1, Day 2 — Generative AI Fundamentals and Evidence-Based Testing



\### Resource

Anthropic AI Fluency — Lesson 4: Generative AI Fundamentals



\### Key Lessons

\- A traditional FAQ system can return a prewritten answer, while generative AI creates a response using learned patterns and the information available in its current context.

\- Training changes the model's learned parameters. Giving an already-trained model a FAQ or other information in a chat gives it context to use, but does not by itself retrain those parameters.

\- A context window is the limited information available to the model while generating a response. Long conversations or documents can test that limit and affect access to earlier information.

\- A fluent and confident answer is not evidence that it is correct. Important factual claims should be checked against the authoritative source.



\### Correction

I initially described model training too similarly to giving a trained model context. I corrected this distinction: training changes the model's parameters, while information supplied during a chat is used as context for the current interaction.



\### Reflection

Today's testing reinforced that an answer can be mostly correct while still failing because of one unsupported claim. I need to evaluate the whole response rather than stopping once the main answer looks correct.

## Week 1, Day 3 — Capabilities, limitations, and evidence



\### Resource

Anthropic AI Fluency — Lesson 5: Capabilities \& limitations



\### Key ideas



\- A model's previous training is different from information supplied to it during use. If a restaurant or hotel changes a policy, I can give the assistant the current policy or provide access to a current source rather than relying on its memory.

\- Having access to current information does not guarantee that the assistant will use it correctly, so important answers still need checking.

\- When using AI with guests, the assistant should not invent rules or services that are absent from the supplied policy and should refer the guest to human support when the information is unavailable.

\- "Not stated in the policy" is not the same thing as "No."

\- If an AI answer contradicts the supplied policy, the answer should be corrected to match the policy.

\- If the policy does not contain the answer, the assistant should say that the information is not stated and refer the guest to reception or customer service rather than guessing.



\### Correction I made



I initially answered the contradiction-versus-missing-information question by focusing on how the system could be improved later, such as changing instructions or test coverage.



The immediate response is simpler:



\- contradiction → follow the supplied policy;

\- missing information → say it is not stated and refer to human support.

## Week 1, Day 4 — Delegation and verification



\### Resource

Anthropic AI Fluency — Lesson 6: A Closer Look at Delegation  

https://academy.claude.com/courses/ai-fluency-framework-foundations/a-closer-look-at-delegation



\### Delegation concepts



The three concepts studied were:



\- Problem Awareness — understand what a useful result actually requires.

\- Platform Awareness — understand what the AI can and cannot do.

\- Task Delegation — decide which parts should be handled by AI and which require human involvement.



For the testing task, a useful result required more than simply getting an answer from an AI. I needed the number of tests passed, failed and needing review, plus evidence that each judgement matched the supplied policy.



The AI can help:

\- generate or review guest questions;

\- analyse responses against a supplied policy;

\- calculate results;

\- draft or review Python code;

\- help summarise work.



The human still needs to:

\- check whether claims are actually supported by the policy;

\- notice unsupported extra claims;

\- decide whether evidence is sufficient;

\- run local Python code;

\- compare actual execution against expected results;

\- make the final judgement.



An important correction was that AI can draft and review Python code, but it cannot prove that the code actually executed correctly on my computer. Local execution still has to be verified by me.



Another lesson was that responsibilities can be shared. Modifying Python code and writing a portfolio summary do not have to be exclusively AI or exclusively human tasks: AI can assist, while the human checks and approves the result.

