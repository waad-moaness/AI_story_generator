

prompt= '''
You are a creative storytelling assistant for children.

Create a 7-day short continuous adventure story.

Include:
1. An INTRODUCTION (before Day 1)
2. Then a 7-day story
3. An OUTRO to conclude the ending of the story

Theme: {theme}
Overall Goal: {goal}

The introduction should:
- Set the scene
- Introduce the main character
- Explain the mission
- Naturally lead into Day 1

The outro should:
- Take place AFTER Day 7 is completed
- Clearly show that the CHILD helped the main character succeed
- Resolve the overall goal in a satisfying way
- Celebrate the child's effort and impact
- End with a warm, magical closing feeling
- Be short (2–3 sentences max)

The story must:
- Be continuous across 7 days (like chapters)
- Each day must include the given task as the main highlight
- Each task must be naturally integrated as a meaningful action that helps the hero progress toward the overall goal
- Be fun, motivating, and suitable for a child
- Build toward the final resolution in the outro (NOT during the days)

Interpret tasks creatively in a story context.

Specific Style Instructions:
1. Keep EVERY "story" section concise (2–3 sentences max), including intro and outro.
2. IMPORTANT: The character should NOT complete the task. Instead, they face a blocker or challenge.
3. Each day MUST end with a direct call to the child (e.g., a question or request for help).
4. The story assumes that once the child completes the task, the hero can move forward.
5. Use simple, clear, child-friendly language.

Tasks:

Day 1: {task1}
Day 2: {task2}
Day 3: {task3}
Day 4: {task4}
Day 5: {task5}
Day 6: {task6}
Day 7: {task7}

Return ONLY valid JSON in the following format:

{{
  "intro": {{
    "title": "...",
    "story": "..."
  }},
  "days": [
    {{
      "day": 1,
      "title": "...",
      "story": "..."
    }},
    {{
      "day": 2,
      "title": "...",
      "story": "..."
    }},
    ...
  ],
  "outro": {{
    "title": "...",
    "story": "..."
  }}
}}
'''

def format_prompt(theme, goal, tasks):
    storyGen_prompt = prompt.format(theme=theme,
                                    goal=goal,
                                    task1=tasks[0],
                                    task2=tasks[1],
                                    task3=tasks[2],
                                    task4=tasks[3],
                                    task5=tasks[4],
                                    task6=tasks[5],
                                    task7=tasks[6]
                                               )
    return storyGen_prompt