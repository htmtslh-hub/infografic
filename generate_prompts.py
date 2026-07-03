import os

keyword = "house"
style_name = "isometric_tech_white"

style_tail = (
    "isometric 3D illustration, clean vector isometric perspective, "
    "isolated on pure white background, "
    "teal green and dark green as primary color tones with warm orange and earth accent colors, "
    "smooth matte surface finish, no heavy texture, no noise, no grain, "
    "minimal flat shading with very subtle shadows only under the object, "
    "moderate detail level with simplified geometric forms, "
    "small miniature scale feeling like a tiny model or diorama piece, "
    "clean sharp geometric edges, no sketchy lines, "
    "even ambient flat lighting with no dramatic shadows, "
    "isometric 3D depth and dimension, viewed from above at 30 degree angle, "
    "modern tech corporate infographic aesthetic, "
    "single isolated isometric element, "
    "no background elements, no ground plane extending beyond the object, "
    "no text, no labels, no audio, "
    "centered composition with generous padding, "
    "high resolution production-ready vector-style asset"
)

subjects = [
    # RESIDENTIAL HOUSES - Basic Types (15)
    "A small single-story suburban house with a front yard and a chimney",
    "A two-story modern family home with large glass windows and a flat roof",
    "A cozy cottage with a thatched roof surrounded by a small garden",
    "A traditional Japanese wooden house with sliding doors and a curved roof",
    "A Mediterranean villa with terracotta roof tiles and white stucco walls",
    "A Scandinavian minimalist house with timber cladding and a green roof",
    "A colonial-style house with columns and a wrap-around porch",
    "A tiny house on wheels parked in a small clearing",
    "A modern glass house with floor-to-ceiling windows and an open layout",
    "A Victorian-style house with ornate trim and a turret tower",
    "A log cabin in a forest clearing with a stone chimney",
    "A prefabricated modular house made of stacked container units",
    "A traditional Korean hanok house with a courtyard in the center",
    "A desert adobe house with flat roof and earth-tone mud walls",
    "A tropical stilted house raised above ground on wooden poles",

    # APARTMENTS & URBAN LIVING (15)
    "A tall modern apartment building with balconies and rooftop garden",
    "A low-rise apartment complex with a shared courtyard and playground",
    "A luxury penthouse suite on top of a high-rise tower",
    "A student dormitory building with many small windows in rows",
    "A co-living space building with shared kitchen and lounge areas visible",
    "A mixed-use building with shops on the ground floor and apartments above",
    "A social housing block with colorful painted facades",
    "A capsule apartment tower with tiny pod-like living units",
    "A renovated warehouse loft building converted into apartments",
    "A senior living community building with accessible ramps and gardens",
    "A townhouse row with each unit painted a different pastel color",
    "A duplex house split into two separate living units",
    "A micro apartment building designed for single occupants in a dense city",
    "A high-rise residential tower with a sky bridge connecting two buildings",
    "A courtyard apartment building with units arranged around a central garden",

    # SMART & FUTURE HOMES (15)
    "A smart home with solar panels on the roof and an electric car charging in the driveway",
    "A futuristic dome house with a transparent roof showing the interior",
    "A 3D-printed house being constructed by a robotic arm printer",
    "A net-zero energy house with wind turbine and rainwater collection system",
    "A smart home with visible IoT sensors on doors windows and appliances",
    "A house with a vertical garden covering the entire exterior facade",
    "A floating house on a platform above water in a flood-prone area",
    "A underground earth-sheltered house with only the entrance visible above ground",
    "A biophilic house with living walls and trees growing through the roof",
    "A self-sustaining off-grid house with greenhouse and water recycling",
    "A house with drone delivery pad on the roof and automated garage",
    "A climate-adaptive house with movable walls and retractable roof sections",
    "A house made entirely of recycled materials and reclaimed wood",
    "A pod-style modular smart home that can be expanded by adding more pods",
    "A house with an integrated home office pod in the backyard",

    # HOUSE COMPONENTS & FEATURES (15)
    "A cross-section cutaway of a house showing all rooms and floors inside",
    "A house rooftop with solar panels a satellite dish and an HVAC unit",
    "A house front door with a smart lock doorbell camera and package shelf",
    "A house garage with an electric vehicle charger and tool storage",
    "A backyard swimming pool with a pool house and lounging area",
    "A house kitchen interior with modern appliances island and dining area",
    "A house living room interior with sofa TV bookshelf and fireplace",
    "A house bedroom interior with bed desk wardrobe and window view",
    "A house bathroom interior with bathtub shower vanity and tiled walls",
    "A house basement converted into a home theater with projector and seats",
    "A house attic converted into a cozy reading room with skylight",
    "A house front porch with rocking chairs potted plants and a welcome mat",
    "A house balcony with outdoor furniture plants and a city view",
    "A home garden with raised vegetable beds compost bin and tool shed",
    "A house staircase interior with modern railing and under-stair storage",

    # CONSTRUCTION & RENOVATION (10)
    "A house under construction with scaffolding exposed framing and workers",
    "A house being demolished with a wrecking ball and debris",
    "A house blueprint plan viewed from above showing room layout",
    "A house renovation in progress with half old half new visible",
    "A house foundation being poured with concrete mixer truck nearby",
    "A house with roof being repaired by workers with tools and materials",
    "A house being painted by workers on ladders with paint buckets",
    "A house with new windows being installed replacing old ones",
    "A house with plumbing pipes and electrical wiring exposed during renovation",
    "A house with landscaping being done around it with new trees and pathways",

    # HOUSE STATES & CONDITIONS (10)
    "A brand new house with a sold sign and moving boxes at the door",
    "An old abandoned house with broken windows overgrown weeds and peeling paint",
    "A house decorated for Christmas with lights wreath and snow on the roof",
    "A house during a rainstorm with water flowing off the roof and puddles",
    "A house at night with warm glowing windows and a moonlit sky",
    "A house covered in thick snow with icicles hanging from the eaves",
    "A house during autumn with fallen leaves covering the yard and roof",
    "A house during spring with blooming flowers in the garden and birds",
    "A house being flooded with water rising around the ground floor",
    "A house withstanding a strong wind storm with debris flying around",

    # HOUSE TYPES BY PURPOSE (10)
    "A farmhouse with a barn silo and tractor parked beside it",
    "A beach house on stilts overlooking the ocean with a surfboard outside",
    "A mountain chalet with steep roof large windows and firewood stacked outside",
    "A treehouse built high in a large tree with a rope ladder",
    "A houseboat floating on calm water with a small deck and plants",
    "A greenhouse attached to a house filled with plants and growing lights",
    "A guard house at the entrance of a gated community with a barrier",
    "A dollhouse miniature showing detailed rooms and tiny furniture inside",
    "A birdhouse mounted on a pole in a garden with birds nearby",
    "A dog house in a backyard with a food bowl and a small fence",

    # HOUSE & COMMUNITY (10)
    "A suburban neighborhood with identical houses lined along a curved street",
    "A gated community entrance with a guard booth fountain and manicured lawns",
    "A cul-de-sac with houses arranged in a circle and children playing",
    "A row of houses along a canal with bridges and boats in the water",
    "A hillside village with houses stacked on terraced slopes",
    "A housing development under construction with multiple houses in progress",
    "A mobile home park with trailers arranged in neat rows",
    "A historic district with preserved heritage houses and cobblestone streets",
    "An eco-village with sustainable houses sharing communal green spaces",
    "A floating village with houses on rafts connected by wooden walkways",
]

# Generate prompts
prompts = []
for subject in subjects:
    prompt = f"{subject}, {style_tail}"
    prompts.append(prompt)

# Create output directory
output_dir = os.path.join("D:\\Kho infografic", f"{keyword}-{style_name}")
os.makedirs(output_dir, exist_ok=True)

# Write prompts file
output_file = os.path.join(output_dir, "prompts.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(prompts))

print(f"Done! Generated {len(prompts)} prompts")
print(f"Saved to: {output_file}")
