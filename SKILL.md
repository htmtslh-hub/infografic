---
name: agency-infographic-generator
description: "Tạo kho ảnh infographic hàng loạt cho video documentary. Nhận ảnh mẫu + từ khóa → phân tích phong cách 12 chiều → tạo 100 prompt + ảnh template → lưu thành thư mục sẵn dùng. Gọi skill này kèm ảnh mẫu + từ khóa để bắt đầu."
risk: low
source: custom
date_added: '2026-07-02'
---

# 🎨 Infographic Batch Prompt Generator

Skill chuyên tạo **kho prompt ảnh infographic** cho video documentary. Mỗi lần gọi, bạn cung cấp **1 ảnh mẫu phong cách** + **1 từ khóa**, skill sẽ tự động:

1. Phân tích phong cách ảnh mẫu (12 chiều)
2. Tạo 100 prompt biến thể từ từ khóa
3. Tạo 1 ảnh template nhận diện phong cách
4. Lưu tất cả vào thư mục riêng

## Cách sử dụng

User chỉ cần gửi:
```
[ảnh mẫu phong cách] + [từ khóa]
```

Ví dụ:
- Gửi ảnh dark premium + "brain" → tạo `brain-dark_premium/`
- Gửi ảnh flat pictogram + "human" → tạo `human-flat_pictogram_dark/`
- Gửi ảnh editorial + "think" → tạo `think-flat_editorial_light/`

Nếu user đã gửi ảnh mẫu trước đó trong cùng cuộc hội thoại, có thể chỉ gửi từ khóa mới và dùng lại style cũ.

---

## Thư mục gốc

```
D:\Kho infografic\
```

Mọi output đều lưu tại đây. Cấu trúc mỗi từ khóa:

```
D:\Kho infografic\{keyword}-{style_name}\
├── prompts.txt          ← 100 prompt, mỗi dòng 1 prompt
└── style_template.png   ← 1 ảnh mẫu nhận diện phong cách
```

---

## QUY TRÌNH TỰ ĐỘNG (6 Bước)

### Bước 1: Nhận Input

Nhận từ user:
- **Ảnh mẫu phong cách** (bắt buộc lần đầu, có thể tái sử dụng từ ảnh trước)
- **Từ khóa** (bắt buộc): ví dụ `human`, `brain`, `think`, `tree`, `weapon`

### Bước 2: Phân tích phong cách — 12-Point Deep Analysis

Phân tích ảnh mẫu theo **ĐỦ 12 chiều**, không bỏ sót:

| # | Chiều phân tích | Cần xác định | Ví dụ |
|---|---|---|---|
| 1 | **Background** | Màu nền, texture, gradient? | Pure black matte / off-white cream / transparent |
| 2 | **Rendering type** | 2D flat / 3D render / hand-drawn? | Flat vector 2D / smooth matte 3D / watercolor |
| 3 | **Surface finish** | Matte / glossy / textured? | Smooth matte no shine / glossy reflective / rough paper |
| 4 | **Color palette** | Bao nhiêu màu? Warm/cool? | Monochrome gold / pastel multi-color / duotone |
| 5 | **Accent color** | Màu nhấn chính | Golden amber / coral teal / neon green |
| 6 | **Shading style** | Flat / gradient / soft shadow? | Zero shadow flat / soft ambient / hard drop shadow |
| 7 | **Detail level** | Minimal icon / moderate / realistic? | Pictogram minimal / editorial moderate / detailed |
| 8 | **Figure style** | Faceless / minimal features / detailed? | Circle head no face / simple cartoon face / realistic |
| 9 | **Lighting** | Ambient / rim / dramatic? | Soft even ambient / warm golden glow / harsh spot |
| 10 | **Depth** | Flat / subtle depth / full 3D? | Pure flat 2D / floating with depth / photorealistic 3D |
| 11 | **Edge treatment** | Hard edges / rounded / soft? | Sharp geometric / rounded friendly / organic |
| 12 | **Overall vibe** | Corporate / playful / editorial? | Dark premium corporate / friendly editorial / retro |

#### QUY TẮC VÀNG khi phân tích:

- ❌ KHÔNG nói "glossy" nếu ảnh mẫu mịn matte
- ❌ KHÔNG nói "3D render" nếu ảnh mẫu là flat vector
- ❌ KHÔNG thêm thuộc tính KHÔNG CÓ trong ảnh mẫu
- ✅ CHỈ mô tả những gì THỰC SỰ THẤY trong ảnh mẫu
- ✅ Dùng negative prompt để NGĂN thuộc tính không mong muốn (ví dụ: "no gloss, no shine, no reflection")
- ✅ So sánh bề mặt: mịn như nhung ≠ bóng như gương, phải phân biệt rõ

### Bước 3: Xây dựng Style Tail

Chuyển 12 chiều phân tích thành chuỗi `style_tail` theo cấu trúc:

```
[rendering type], [background description],
[color palette], [accent color],
[surface finish + negative surface props],
[shading style],
[figure/object style], [lighting description],
[depth description], [edge treatment],
[overall vibe],
[isolation rules: no background elements, no ground plane],
[negative prompts: no text, no labels, no audio],
[composition: centered with generous padding],
[quality: render engine style reference],
[output: high resolution production-ready asset]
```

**Ví dụ style_tail đã tạo:**

**Dark Premium Matte (từ ảnh infographic vàng-đen):**
```
3D rendered dark premium infographic icon, deep black matte background,
golden yellow and amber as the only accent color,
smooth matte surface finish, no gloss, no shine, no reflection,
soft flat shading with smooth edges,
floating 3D object with depth and dimension,
dark charcoal and black matte base tones on the object body,
warm golden ambient glow softly illuminating the object edges,
clean simplified geometric form,
modern corporate business infographic aesthetic,
high contrast dark studio scene with soft even lighting,
single isolated 3D element floating in darkness,
no specular highlights, no reflections, no metallic texture,
no background elements, no ground plane,
no text, no labels, no audio,
centered composition with generous padding,
smooth clean 3D render, cinema 4D matte style,
high resolution production-ready asset
```

**Flat Pictogram Dark (từ ảnh biểu đồ người cam-xanh):**
```
flat vector pictogram human figure,
simple geometric body silhouette,
perfect circle head with no face no eyes no features,
solid flat color fill with no gradient no shading,
orange amber or teal turquoise or neutral gray color tone,
dark navy charcoal slate background,
completely flat 2D vector style, no 3D no depth no shadow,
clean minimalist infographic people icon,
simplified body proportions like a restroom sign pictogram,
no outlines no strokes, pure solid shape,
single isolated figure, no background elements,
no text, no labels, no audio,
centered composition with generous padding,
high resolution production-ready vector asset
```

**Flat Editorial Light (từ ảnh minh họa magazine):**
```
modern flat editorial illustration,
light off-white cream clean background,
vibrant muted pastel color palette with coral teal purple green and blue tones,
simplified cartoon character with minimal facial features,
flat 2D vector style with solid color fills,
very minimal shading no heavy shadows no gradients,
clean rounded friendly shapes,
modern magazine infographic aesthetic like Notion or Slack illustrations,
single isolated scene element,
no background clutter, no ground plane,
no text, no labels, no audio,
centered composition with generous padding,
high resolution production-ready vector asset
```

**Flat Isometric Pastel (từ ảnh isometric người):**
```
flat vector isometric illustration, faceless minimal human figure,
no facial details, simple body silhouette,
vibrant pastel color palette with pink coral green and blue tones,
clean flat shading, no gradients, geometric simplified forms,
small scale miniature character style, modern infographic aesthetic,
isolated on pure white background, no background elements,
no ground shadow, no text, no audio, clean cutout style,
centered with padding, high resolution, production-ready asset
```

### Bước 4: Mở rộng từ khóa → 100 biến thể

Phát triển 1 từ khóa thành **chính xác 100 biến thể** đa dạng:

#### Chiến lược mở rộng theo loại từ khóa:

**NGƯỜI (human, worker, leader, etc.):**
| Nhóm | SL | Ví dụ biến thể |
|---|---|---|
| Emotions | 20 | Joy, sadness, anger, fear, surprise, hope, shame, anxiety |
| Actions | 20 | Running, reading, cooking, swimming, typing, dancing |
| Professions | 20 | Doctor, soldier, farmer, teacher, chef, astronaut |
| Ages & Gender | 10 | Baby, toddler, teenager, adult, pregnant, elderly |
| Groups | 15 | Couple, family, team, crowd, leader, mentor |
| Situations | 15 | Climbing stairs, crossroads, trophy, pushing boulder |

**VẬT THỂ (brain, gear, book, etc.):**
| Nhóm | SL | Ví dụ biến thể |
|---|---|---|
| Anatomy/Structure | 15 | Parts, cross-section, views, internal components |
| Functions/Abilities | 20 | What it does, integrated metaphors, symbolic meanings |
| States/Conditions | 15 | Active, damaged, glowing, frozen, overloaded |
| Technology/Digital | 15 | Circuit version, hologram, AI version, binary code |
| Metaphors/Symbols | 20 | Tree-shaped, maze, treasure chest, volcano |
| Health/Science | 15 | Under microscope, with DNA, bandaged, exercising |

**KHÁI NIỆM (think, grow, connect, etc.):**
| Nhóm | SL | Ví dụ biến thể |
|---|---|---|
| Poses/States | 20 | Physical manifestations of the concept |
| Types/Variations | 20 | Subcategories (creative thinking, critical thinking...) |
| Problem Solving | 15 | Decision-making, maze solving, key finding |
| Learning | 15 | Reading, teaching, aha moment, brain mapping |
| Idea Generation | 15 | Lightbulbs, planting seeds, brainstorming |
| Philosophy | 15 | Mountain contemplation, mirror, hourglass |

**ĐỘNG VẬT (bird, fish, horse, etc.):**
| Nhóm | SL | Ví dụ biến thể |
|---|---|---|
| Species | 20 | Different species in the category |
| Actions | 20 | Hunting, flying, sleeping, feeding, fighting |
| Environments | 15 | Arctic, desert, jungle, ocean, forest |
| States | 15 | Baby, adult, aggressive, peaceful, injured |
| Groups | 15 | Flock, pack, herd, pair, mother-baby |
| Symbolic | 15 | Mythical, cultural symbol, metaphor |

**THIÊN NHIÊN (tree, mountain, water, etc.):**
| Nhóm | SL | Ví dụ biến thể |
|---|---|---|
| Species/Types | 20 | Different varieties |
| Seasons | 15 | Spring, summer, autumn, winter states |
| Weather | 15 | Sunny, rainy, stormy, snowy |
| Ages/States | 15 | Seedling, young, mature, dying, dead |
| Interactions | 15 | With animals, with people, with elements |
| Symbolic | 20 | Metaphors, cultural meanings |

### Bước 5: Tạo file prompt + thư mục

Với mỗi biến thể: `[mô tả subject], [style_tail]`

**Quy tắc file prompt:**
- Mỗi prompt trên 1 dòng riêng
- KHÔNG đánh số thứ tự
- KHÔNG cách dòng giữa các prompt
- Tiếng Anh chuẩn
- Mỗi prompt hoàn chỉnh, độc lập

Lưu vào:
```
D:\Kho infografic\{keyword}-{style_name}\prompts.txt
```

### Bước 6: Tạo ảnh template

**BẮT BUỘC** — Chọn prompt ĐẦU TIÊN trong danh sách, dùng `generate_image` tool để tạo ảnh.

Copy ảnh vào thư mục:
```
D:\Kho infografic\{keyword}-{style_name}\style_template.png
```

Ảnh template này giúp user nhìn nhanh phong cách của thư mục mà không cần mở file prompt.

### Bước 7: Báo cáo kết quả

Hiển thị:
- ✅ Đường dẫn thư mục
- ✅ Số lượng prompt đã tạo
- ✅ Bảng phân loại các nhóm biến thể
- ✅ Ảnh template
- ✅ Gợi ý từ khóa tiếp theo

---

## QUY TẮC CHUNG

### Output Rules
- Mọi ảnh là **1 element đơn lẻ trên nền** — KHÔNG BAO GIỜ tạo layout đầy đủ
- User tự ghép ảnh vào video editor (DaVinci Resolve, Premiere Pro, etc.)
- Prompt phải có negative keywords phù hợp: `no text, no labels, no audio`

### Style Naming Convention
Tên style phải ngắn gọn, mô tả rõ, dùng underscore:
- `flat_isometric` — flat vector góc isometric
- `dark_premium` — nền tối, premium corporate
- `flat_pictogram_dark` — pictogram phẳng nền tối
- `flat_editorial_light` — minh họa editorial nền sáng

### Directory Naming Convention
```
{keyword}-{style_name}
```
Ví dụ: `brain-dark_premium`, `human-flat_pictogram_dark`, `think-flat_editorial_light`

---

## CẤU TRÚC THƯ MỤC TỔNG THỂ

```
D:\Kho infografic\
├── brain-dark_premium\
│   ├── prompts.txt
│   └── style_template.png
├── human-flat_isometric\
│   ├── prompts.txt
│   └── style_template.png
├── human-flat_pictogram_dark\
│   ├── prompts.txt
│   └── style_template.png
├── think-flat_editorial_light\
│   ├── prompts.txt
│   └── style_template.png
├── {keyword}-{style}\              ← Thêm bao nhiêu tùy ý
│   ├── prompts.txt
│   └── style_template.png
└── generate_prompts.py             ← Script hỗ trợ (optional)
```

---

## LƯU Ý KỸ THUẬT

### Tách nền ảnh sau khi generate
AI có thể tạo shadow hoặc noise không mong muốn. User nên dùng:

| Tool | Cách dùng |
|---|---|
| **Remove.bg** | Upload ảnh → auto remove background |
| **Adobe Firefly** | Generative fill để clean up |
| **DaVinci Resolve** | Fusion → Delta Keyer / Magic Mask |
| **Premiere Pro** | Ultra Key / Luma Key effect |
| **CapCut** | Auto Remove Background |

### Style tái sử dụng
Khi user đã gửi ảnh mẫu và tạo style trong cuộc hội thoại, các từ khóa tiếp theo có thể dùng lại style đó mà không cần gửi ảnh lại. Chỉ cần gửi từ khóa mới.

### Prompt chất lượng
- Subject description phải cụ thể, hành động rõ ràng
- Tránh mô tả mơ hồ ("a nice person") → phải cụ thể ("a person sitting cross-legged with palms on knees in meditation pose")
- Mỗi prompt phải khác biệt đáng kể so với prompt khác

---

## QUICK REFERENCE — Tóm tắt 1 dòng

```
User gửi: [ảnh mẫu] + [từ khóa]
→ Phân tích 12 chiều → Tạo style_tail
→ Mở rộng 100 biến thể → Tạo prompts.txt
→ Generate 1 ảnh template → Lưu style_template.png
→ Báo cáo kết quả
```
