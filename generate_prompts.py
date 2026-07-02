#!/usr/bin/env python3
"""Generate 100 prompts for keyword 'think' - modern flat editorial illustration style."""
import os

keyword = "think"
style_name = "flat_editorial_light"

# Analyzed from reference: light bg, multi-color pastel flat illustration,
# simplified characters with minimal features, flat vector objects,
# modern editorial/magazine infographic style, clean and friendly
style_tail = (
    "modern flat editorial illustration, "
    "light off-white cream clean background, "
    "vibrant muted pastel color palette with coral teal purple green and blue tones, "
    "simplified cartoon character with minimal facial features, "
    "flat 2D vector style with solid color fills, "
    "very minimal shading no heavy shadows no gradients, "
    "clean rounded friendly shapes, "
    "modern magazine infographic aesthetic like Notion or Slack illustrations, "
    "single isolated scene element, "
    "no background clutter, no ground plane, "
    "no text, no labels, no audio, "
    "centered composition with generous padding, "
    "high resolution production-ready vector asset"
)

subjects = [
    # THINKING POSES & STATES (20)
    "A person sitting at a desk with hand on chin deep in thought staring at a laptop screen",
    "A person standing with one finger on temple looking upward thinking",
    "A person sitting cross-legged on the floor with eyes closed meditating deeply",
    "A person lying on a couch staring at the ceiling lost in thought",
    "A person walking alone with hands behind back in contemplative pose",
    "A person sitting on a bench with a notebook thinking and jotting notes",
    "A person leaning against a wall with arms crossed thinking seriously",
    "A person sitting at a cafe table with coffee cup paused mid-thought",
    "A person pacing back and forth with hand on forehead thinking hard",
    "A person sitting in an armchair with a book open on lap gazing into distance",
    "A person standing at a whiteboard with marker paused mid-thought",
    "A person sitting on stairs with elbows on knees head in hands thinking",
    "A person lying in bed at night staring at the ceiling unable to sleep from overthinking",
    "A person sitting under a tree with eyes closed thinking peacefully",
    "A person standing in front of a mirror reflecting on themselves",
    "A person riding a train looking out the window deep in thought",
    "A person showering with a lightbulb appearing above their head",
    "A person gardening while thinking with thought bubbles floating up",
    "A person jogging with a focused thinking expression",
    "A person sitting alone in an empty room thinking in silence",
    # TYPES OF THINKING (20)
    "A person surrounded by floating gears and cogs representing logical analytical thinking",
    "A person with colorful paint splashes and brushes around them representing creative thinking",
    "A person with a magnifying glass examining small details representing critical thinking",
    "A person with abstract shapes and patterns floating around representing abstract thinking",
    "A person with a crystal ball and stars representing visionary thinking",
    "A person with multiple branching arrows representing divergent thinking",
    "A person with arrows converging to one point representing convergent thinking",
    "A person with a balance scale weighing two options representing rational thinking",
    "A person with a heart and a brain floating side by side representing emotional thinking",
    "A person surrounded by interconnected web of nodes representing systems thinking",
    "A person with a map and compass representing strategic thinking",
    "A person looking backwards at a timeline representing reflective thinking",
    "A person with futuristic elements and forward arrows representing forward thinking",
    "A person connecting different colored dots with lines representing lateral thinking",
    "A person with a question mark cloud and exclamation answer representing inquiry thinking",
    "A person assembling a large jigsaw puzzle representing integrative thinking",
    "A person with thought bubbles containing different perspectives representing empathetic thinking",
    "A person with mathematical formulas floating around representing mathematical thinking",
    "A person with musical notes and sound waves representing musical thinking",
    "A person with nature elements and earth representing ecological thinking",
    # PROBLEM SOLVING & DECISIONS (15)
    "A person standing at a fork in the road choosing between two paths",
    "A person untangling a complex knot of ropes patiently",
    "A person stacking building blocks to create a tall stable tower",
    "A person looking at a maze from above finding the solution path",
    "A person connecting puzzle pieces to complete a bigger picture",
    "A person climbing a ladder to reach a lightbulb at the top",
    "A person opening locked doors with different keys trying each one",
    "A person sorting scattered papers into organized neat piles",
    "A person drawing a flowchart on a large board mapping out steps",
    "A person weighing pros and cons on a balance scale",
    "A person with binoculars looking at a distant goal on a mountain",
    "A person swimming upstream against a current with determination",
    "A person debugging code on a screen finding and fixing errors",
    "A person rearranging chess pieces on a board planning strategy",
    "A person fitting the last piece into a complex machine making it work",
    # LEARNING & KNOWLEDGE (15)
    "A person reading a thick book with knowledge particles rising from the pages",
    "A person attending an online class on a laptop taking notes",
    "A person teaching a small group pointing at a presentation board",
    "A person surrounded by floating books absorbing information",
    "A person watching a tutorial video on a screen with notepad beside them",
    "A person in a library reaching for a book on a high shelf",
    "A person having an aha moment with a bright lightbulb appearing",
    "A person comparing two documents side by side analyzing differences",
    "A person asking questions with question marks floating around them",
    "A person brain mapping on a large paper with branches and topics",
    "A person mentoring another person at a desk explaining a concept",
    "A person practicing a skill repeatedly with improvement arrows",
    "A person exploring a globe with a magnifying glass discovering facts",
    "A person writing in a journal reflecting on daily learnings",
    "A person connecting real world objects to scientific diagrams",
    # IDEA GENERATION (15)
    "A person with multiple lightbulbs floating above their head representing many ideas",
    "A person planting a small seed that grows into a big tree representing growing an idea",
    "A person sculpting a rough clay block into a refined shape representing idea refinement",
    "A person catching floating stars in a net representing capturing inspiration",
    "A person mixing different color liquids in beakers creating something new",
    "A person building a bridge between two cliffs representing connecting ideas",
    "A person launching a paper airplane that transforms into a real plane",
    "A person sketching rapidly on paper with crumpled papers around them",
    "A person brainstorming with sticky notes covering an entire wall",
    "A person looking through a kaleidoscope seeing new patterns",
    "A person opening a box with bright light and ideas pouring out",
    "A person combining a wrench and a paintbrush together as innovation",
    "A person standing in rain with an umbrella catching idea raindrops",
    "A person blowing bubbles that contain small idea icons inside them",
    "A person assembling a rocket from scattered parts about to launch",
    # PHILOSOPHY & WISDOM (15)
    "A person sitting on a mountain top in lotus pose contemplating the universe",
    "A person looking at a vast starry night sky pondering existence",
    "A person holding a small globe in their hands examining it thoughtfully",
    "A person standing before a giant clock thinking about time and mortality",
    "A person walking a spiral path inward toward a glowing center representing self-discovery",
    "A person holding up a lantern in darkness searching for truth",
    "A person reading ancient scrolls by candlelight seeking wisdom",
    "A person standing between a sunrise and sunset representing perspective",
    "A person looking at their own shadow which has a different shape representing identity",
    "A person planting a tree knowing they may never sit in its shade representing legacy",
    "A person carrying a small flame carefully through wind protecting an idea",
    "A person standing on an hourglass watching sand fall representing patience",
    "A person peeling layers off an onion revealing a glowing core representing truth",
    "A person looking at a still lake reflection that shows a different version of themselves",
    "A person sitting with an old wise figure under a large tree sharing stories",
]

lines = [f"{s}, {style_tail}" for s in subjects]

folder = os.path.join(r"D:\Kho infografic", f"{keyword}-{style_name}")
os.makedirs(folder, exist_ok=True)
output_path = os.path.join(folder, "prompts.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Done! Generated {len(lines)} prompts")
print(f"Saved to: {output_path}")
