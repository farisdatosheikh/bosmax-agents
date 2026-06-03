# BOSMAX TEST HARNESS v1
# Authority: Production Verification
# Authors: Codex + Claude Cowork (shake-hand consensus)
# Status: CANONICAL — must pass all cases before mass production lock-down
# Version: v1.0 | Date: 2026-06-03

---

## 1. PURPOSE

This harness defines what "BOSMAX works correctly" means.

Not opinion. Not feel. Specific inputs → specific expected behaviors.

Before mass production: all 10 cases must pass.
After any major change: re-run relevant cases.

---

## 2. HOW TO RUN A TEST CASE

1. Give BOSMAX the exact input described
2. Observe the output
3. Check against EXPECTED BEHAVIOR checklist
4. Mark PASS or FAIL per item
5. Overall PASS = all checklist items green

---

## 3. TEST CASES

---

### TEST_001 — Unknown Product, Clear Image, Video Request

**Input:**
- Upload image: person holding yellow Air Cushion box (植护, 1000 PCS label visible)
- Text: `buat video grok 16 saat`

**Expected behavior:**

```
STATE_INTAKE:
☐ raw_request captured
☐ asset detected (1 image)

STATE_ASSET_ANALYSIS:
☐ Avatar detected: Malay female, hijab, pink outfit
☐ avatar_record.source = USER_UPLOAD
☐ Product detected: "Air Cushion 1000 PCS" from label in image
☐ product_record.name_from_label = "Air Cushion 1000 PCS"
☐ product_record.registry_status = NOT_FOUND
☐ sandbox_stub built from visual evidence
☐ NO mention of BOSMAX Serum, RIZAL, or any registry persona

STATE_ROUTE_RESOLVED:
☐ task_mode = VIDEO

STATE_ENGINE_PLANNED:
☐ engine_id = GROK
☐ block_count = 2
☐ block_durations = [10, 6]
☐ NOT [8, 8] or [16] or any other invalid distribution

STORYBOARD:
☐ Kernel surfaces product unknown question (Sandbox A or Register B) — BEFORE storyboard
☐ After user answers, storyboard built with Air Cushion product truth
☐ Storyboard presented to user for approval

FINAL OUTPUT:
☐ Two separate block prompts (Block 1 = 10s, Block 2 = 6s)
☐ Block 1 and Block 2 are separate, not one 16s monolith
☐ Avatar in prompt matches uploaded image (Malay female, pink hijab) — NOT RIZAL
☐ Product in prompt is Air Cushion — NOT BOSMAX Serum
☐ overlay_flag = NO_OVERLAY on both blocks
☐ No BOSMAX internal labels in output
```

**Critical failure triggers:**
- BOSMAX Serum appears anywhere → FAIL
- RIZAL appears anywhere → FAIL
- Single 16s monolithic GROK prompt → FAIL
- No storyboard before prompt emission → FAIL

---

### TEST_002 — Registry Product, Video, GROK 20s

**Input:**
- Text only: `nak buat video tiktok untuk minyak warisan cap burung, grok 20 saat, bahasa melayu`

**Expected behavior:**

```
STATE_INTAKE:
☐ No assets detected
☐ modality_hint = VIDEO

STATE_ASSET_ANALYSIS:
☐ Skipped or minimal (no assets)

STATE_ROUTE_RESOLVED:
☐ task_mode = VIDEO
☐ platform = TikTok

STATE_ENGINE_PLANNED:
☐ engine_id = GROK
☐ block_count = 2
☐ block_durations = [10, 10]    ← default for GROK 20s
☐ NOT [10, 6, 4] or any invented distribution

PRODUCT LOOKUP:
☐ CAP_BURUNG_MINYAK.yaml loaded
☐ scale_anchor injected: "EXACTLY a small pocket-size 30ml rectangular clear glass medicated oil bottle with a red ribbed cap, shorter than the palm and only two fingers wide"
☐ Copywriting angles available from YAML

STORYBOARD:
☐ Storyboard built for 2×10s GROK
☐ BM dialogue declared
☐ WPS budget calculated for BM @ 2.5 WPS: Floor(10×2.5) = 25 words per block
☐ Presented to user for approval

FINAL OUTPUT:
☐ Two separate block prompts: Block 1 (10s), Block 2 (10s)
☐ Product: WG40 30ml bottle, red ribbed cap, perched bird label
☐ Scale anchor present in both blocks
☐ Bridge-out in Block 1, Bridge-in in Block 2
☐ Block 2 dialogue resumes within 0.5s–1.0s (seam law)
☐ overlay_flag = NO_OVERLAY
```

---

### TEST_003 — Registry Product, Image, Selling Poster

**Input:**
- Upload image: BOSMAX Serum 5ML bottle photo
- Text: `buat poster jual untuk tiktok`

**Expected behavior:**

```
STATE_ASSET_ANALYSIS:
☐ Product detected from image label: BOSMAX Serum
☐ registry_status = FOUND
☐ BOSMAX_SERUM.yaml loaded
☐ scale_anchor_descriptor extracted for 5ML

STATE_ROUTE_RESOLVED:
☐ task_mode = IMAGE
☐ image_goal = SELLING_POSTER

COMPOSITION:
☐ Selling hierarchy: product dominant, avatar optional
☐ Scale anchor injected: "EXACTLY lip balm size, fit into fingers naturally"
☐ Platform = TikTok, platform-specific negative locks set

FINAL OUTPUT:
☐ Single image prompt
☐ BOSMAX 5ML product truth preserved (black stealth packaging, lip balm scale)
☐ No wrong scale (not deodorant-size, not perfume-size)
☐ overlay_flag = NO_OVERLAY
```

---

### TEST_004 — GROK Block Math Enforcement

**Input:**
- Text: `buat video grok 30 saat, bahasa melayu, tiktok, cap burung minyak`

**Expected behavior:**

```
STATE_ENGINE_PLANNED:
☐ engine_id = GROK
☐ duration_total = 30
☐ block_count = 3
☐ block_durations = [10, 10, 10]   ← BOSMAX default for 30s
☐ Kernel does NOT output [6, 6, 6, 6, 6] unless operator explicitly requests alternate

If operator asks for alternate (5×6s):
☐ Kernel acknowledges and switches to [6, 6, 6, 6, 6]
☐ block_count updated to 5

FINAL OUTPUT:
☐ Three separate block prompts (not one 30s monolith)
☐ Bridge-out in Block 1 and Block 2
☐ Bridge-in in Block 2 and Block 3
```

**Critical failure triggers:**
- Single 30s GROK prompt → FAIL
- Block durations include 8s or 12s → FAIL

---

### TEST_005 — Compliance Auditor Catch: No Storyboard

**Input (simulated bad state — compliance test):**
- Simulate: Prompt Compiler attempts to emit video prompt without storyboard_packet being VALID

**Expected behavior:**

```
COMPLIANCE AUDITOR:
☐ Check: storyboard_packet exists → FAIL
☐ verdict = ABORT
☐ abort_reason = "storyboard_packet null or not user_approved"
☐ No prompt delivered to user
☐ Kernel surfaces abort reason to user
```

---

### TEST_006 — Visual Override: Registry Product vs Different Image

**Input:**
- Upload image showing Minyak Warisan Cap Burung bottle
- Text: `buat poster bosmax serum`

**Expected behavior:**

```
STATE_ASSET_ANALYSIS:
☐ Product from image: Minyak Warisan Cap Burung (from label)
☐ Product from text: BOSMAX Serum
☐ CONFLICT detected: visual evidence ≠ text

KERNEL ACTION:
☐ Kernel surfaces conflict to user:
   "Gambar menunjukkan Minyak Warisan Cap Burung. Teks menyebut BOSMAX Serum. Yang mana satu, boss?"
☐ Holds state until user confirms
☐ Does NOT default to either product without confirmation
```

---

### TEST_007 — BM Commercial Video, Dialogue Law

**Input:**
- Text: `video tiktok ugc 10 saat kling 3.0 bahasa melayu untuk cap burung`

**Expected behavior:**

```
STATE_STORYBOARD_BUILT:
☐ BM commercial UGC detected
☐ dialogue MANDATORY
☐ copy_formula declared: SELL_THROUGH_HPFRC or STORY_HSARC
☐ Hook in first spoken line
☐ Pain/friction before product reveal
☐ WPS: Floor(10 × 2.5) = 25 words max

COMPLIANCE AUDITOR:
☐ Checks: dialogue present → PASS
☐ Checks: copy_formula declared → PASS
☐ Checks: hook present → PASS

FINAL OUTPUT:
☐ Dialogue present in prompt
☐ Not "pure visual" or "no dialog" or "WPS: 0"
```

**Critical failure triggers:**
- "pure visual" or "no dialog" in output without user request → FAIL

---

### TEST_008 — Image Without Product Name, Sandbox Trigger

**Input:**
- Upload image: blurry packaging, no clear label text visible
- Text: `buat video grok 10 saat`

**Expected behavior:**

```
STATE_ASSET_ANALYSIS:
☐ Product detected but name UNCLEAR (no readable label)
☐ ambiguous_items: ["product_identity"]
☐ sandbox_stub built with: shape, color, scale estimate only

KERNEL ACTION:
☐ Kernel surfaces question: "Saya nampak [packaging description]. Ini produk apa, boss?"
☐ State HOLDS at STATE_ASSET_ANALYSIS
☐ No routing proceeds without answer

After user answers:
☐ sandbox_stub enriched with user-provided name
☐ Proceed to STATE_ROUTE_RESOLVED
```

---

### TEST_009 — Repair Lane Routing

**Input:**
- Text: `output sebelum ni salah — mwcb bottle jadi terlalu besar, tolong betulkan`

**Expected behavior:**

```
STATE_INTAKE:
☐ repair_mode = true detected

REPAIR ROUTING:
☐ Kernel identifies: product truth drift → MWCB scale
☐ Routes to: PRODUCT-SPECIFIC SELF-HEALING → MWCB IMAGE variant
☐ Worker reads BOSMAX_PRODUCT_SPECIFIC_SELF_HEALING_VARIANTS_v1.md
☐ Applies MWCB product truth locks
☐ Does NOT ask user to re-explain obvious errors one by one

FINAL OUTPUT:
☐ Corrected prompt with MWCB scale truth: pocket-size, red ribbed cap, perched bird
☐ No hero-bottle inflation
```

---

### TEST_010 — VEO_3_1_LITE Multi-Block

**Input:**
- Text: `video veo lite 16 saat untuk minyak cap burung tiktok bm`

**Expected behavior:**

```
STATE_ENGINE_PLANNED:
☐ engine_id = VEO_3_1_LITE
☐ engine max per block = 8s
☐ 16s > 8s → MULTI-BLOCK TRIGGERED
☐ block_count = 2
☐ block_durations = [8, 8]
☐ dialog_budget: VEO_3_1_LITE actual render = 7s, so Floor(7 × 2.5) = 17 words per block

FINAL OUTPUT:
☐ Two separate block prompts
☐ Dialog budget honors 17-word ceiling per block
☐ Bridge-out in Block 1, Bridge-in in Block 2
```

---

## 4. OVERALL PASS CRITERIA

| Test | What it verifies |
|---|---|
| TEST_001 | Visual intake gate, sandbox, unknown product, GROK block math |
| TEST_002 | Registry lookup, GROK default distribution, WPS, storyboard |
| TEST_003 | Image route, selling poster, scale anchor injection |
| TEST_004 | GROK 30s default 3×10s, alternate only on explicit request |
| TEST_005 | Compliance auditor catches missing storyboard |
| TEST_006 | Visual evidence overrides text when they conflict |
| TEST_007 | BM commercial UGC dialogue law enforced |
| TEST_008 | Ambiguous product holds state, asks user |
| TEST_009 | Repair lane routing to correct repair layer |
| TEST_010 | VEO_3_1_LITE multi-block with 7s actual render budget |

**PASS threshold for mass production lock-down: 10/10**

---

## 5. REGRESSION TEST RULE

After any MAJOR or BREAKING change (per Governor change control):
- Re-run all 10 tests
- Any regression = do not deploy the change

After any PATCH or MINOR change:
- Re-run tests directly related to the changed area
- At minimum: re-run TEST_001 (covers the most common failure mode)

---

## 6. NEW TEST CASE PROTOCOL

When a new failure mode is discovered in production:
1. Write a new test case that would have caught it
2. Add to this harness
3. Commit with `test(bosmax):` prefix
4. Run the new case on the current system to verify it now passes

Test cases never get deleted. If a scenario is no longer relevant, mark it ARCHIVED with a note.
