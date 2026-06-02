# BOSMAX SANDBOX + ON-THE-FLY TEMPLATES v1

Authority file for unknown-product sessions where the user uploads a real image
and wants BOSMAX to proceed without full product registration first.

---

## 1. Visual-First Sandbox Choice Prompt

Use this exact fork when:
- product is not found in `products/*.yaml`
- product is not found in FastMoss
- uploaded image still shows clear product evidence

```text
Produk ini belum ada dalam registry. Nak proceed sekarang (session sahaja) atau register dulu?

A) Proceed sekarang
   - saya guna gambar sebagai authority utama
   - saya skip soalan identity/packaging yang sudah jelas dalam gambar
   - saya cuma tanya baki minimum yang belum cukup

B) Register dulu
   - saya simpan produk dalam registry BOSMAX
   - lepas itu baru generate
```

---

## 2. Visual-First Mini-Intake Shortcut

Use this when the uploaded image already proves:
- product name / brand
- packaging shape / colour
- approximate scale

Only ask the remaining fields.

```text
Saya sudah detect dari gambar:
- Produk: [nama dari label]
- Brand/logo: [brand/logo]
- Packaging: [shape + colour + approximate scale]

Saya perlukan 3 benda sahaja untuk proceed:
1. Jenis / kategori produk?
2. Scale anchor confirm: sebesar apa berbanding benda harian?
3. Platform + bahasa output?
```

---

## 3. Full Sandbox Wizard

Use this only if visual evidence is weak or product label is unclear.

```text
1. Nama produk dan brand?
2. Jenis produk / kategori?
3. Packaging: bentuk, warna utama, saiz?
4. Scale anchor: sebesar apa berbanding benda harian?
5. Platform dan bahasa output?
```

---

## 4. On-the-Fly Image Ignition Template

```text
Based on the uploaded image, treat the uploaded visual as the highest authority.
Do not replace the avatar, product, or packaging with any registry default.

First do a neutral visual scan:
- who is visible
- what product is visible
- what exact label text or brand is visible
- what the packaging shape, scale, and setting look like

Then build one IMAGE output only.
If the product is unknown, use sandbox mode and proceed with the minimum missing questions only.
```

---

## 5. On-the-Fly Video Ignition Template

```text
Based on the uploaded image, treat the uploaded visual as the highest authority.
Do not replace the avatar, product, packaging, or scene with any registry default.

Before giving any final prompt:
1. complete visual scan
2. resolve engine
3. resolve block math
4. build storyboard
5. calculate WPS budget
6. only then emit final block prompts

If duration exceeds one block, split it correctly by engine rule.
```

---

## 6. GROK 16s Contract Template

```text
Engine: GROK
Duration: 16s
Block distribution: Block 1 = 10s, Block 2 = 6s

Mandatory:
- use uploaded image as absolute visual authority
- preserve same person identity
- preserve same product identity
- preserve same framing class unless storyboard says otherwise
- preserve same product size relative to body/hands
- brisk UGC pacing
- no slow premium pauses
- no single 16s monolithic block
```

---

## 7. Internal Pre-Output Checklist

Do not release the prompt unless all pass.

```text
☐ visual scan complete
☐ avatar = USER_UPLOAD if image shows person
☐ product = image label / packaging truth
☐ no registry fallback drift
☐ sandbox path used if product unknown
☐ engine confirmed
☐ storyboard approved
☐ block math valid
☐ WPS budget valid
☐ pace_class declared
☐ Grok persistence lock present if reference image used
```
