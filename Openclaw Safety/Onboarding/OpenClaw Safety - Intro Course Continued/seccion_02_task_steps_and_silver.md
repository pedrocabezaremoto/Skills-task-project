# OpenClaw Safety - Intro Course Continued
## Sección 2: Task Steps and Silver Trajectory

---

## Slide 2 — Task Steps
A task on this project consists of these steps:

1. **Review the task scenario and agent setup**
   - Understand the agent's objective, environment context, and the systems the agent will interact with.

2. **Run the task across the five model environments**
   - Send the same initial prompt to each model and interact with the agent through a multi-turn conversation to generate trajectories.

   > ### Silver Trajectory Creation
   > After running all five models, identify which model performed the best overall. **Clone that trajectory** into a new OpenClaw step and continue interacting with the model. Iterate on the conversation by making corrections, adding follow-up prompts, and guiding the model until it reaches the correct or ideal outcome. This refined interaction becomes the **Silver trajectory**.

3. **Identify and annotate failures**
   - Record any issues observed in the trajectories, such as incorrect assumptions, unsafe actions, or missed constraints.

4. **Create evaluation rubrics**
   - Define the criteria used to evaluate model performance. Each rubric should capture key behaviors or requirements for completing the task correctly and safely.

5. **Evaluate rubric criteria in each trajectory**
   - For each model trajectory, review the rubric items and mark whether each criterion is **Present** or **Not Present** based on the model's behavior during the interaction.
