# BOSMAX GROK EXTENSION SEAM TEMPLATES v1

Authority file for reducing early Block 2 lag, dead air, and lipsync mismatch
in GROK multi-block commercial UGC video.

Use this after Block 1 already ends with spoken dialogue near the final frame.

---

## Core Seam Law

For `GROK` BM commercial UGC extension:
- Block 2 must resume speech within `0.5s–1.0s`
- opening action must be micro-continuation only
- do not spend the first `2s–3s` on silent repositioning
- first spoken clause must continue the same semantic thread from Block 1
- Block 1 should end with a bridge-out phrase when possible
- Block 2 should resolve or develop that bridge immediately

Good opening actions:
- slight tilt
- small nod
- tiny hand adjustment
- gentle return-to-camera motion

Bad opening actions:
- long silent hold
- slow product setup
- new presentational pose
- delayed speech after multiple seconds

---

## Template A — Soft Household UGC

Use this when the tone is:
- warm
- practical
- family or home-use friendly

### Block 2 opener rule

```text
Continue the next clip from the previous clip's exact carried-over ending motion.
Resume speech within the first 0.5s–1.0s of the clip.
Use only a slight natural hand adjustment or a small tilt of the product before the next spoken phrase begins.
Do not create a long silent action setup.
The feeling should be like one continuous home recommendation, not a reset.
If the previous clip ended with a lead-in phrase, the next clip must complete that same thought immediately.
```

### Spoken style target

```text
The first spoken clause should sound like a practical continuation, for example:
- "...jadi memang senang nak simpan."
- "...sebab tu aku suka stok yang macam ni."
- "...jadi rumah pun nampak lebih teratur."
```

### Bridge-out examples for Block 1

```text
Use endings like:
- "...sebab yang paling senang,"
- "...yang aku suka tentang benda ni,"
- "...sebab bila nak guna cepat,"
```

---

## Template B — Direct Recommendation UGC

Use this when the tone is:
- direct
- useful
- product-forward

### Block 2 opener rule

```text
Continue the next clip immediately from the previous clip's final product-facing motion and carry-over hold.
Speech resumes almost immediately in the first second.
The product may tilt slightly, but the motion must support the sentence, not delay it.
No dead air and no second introduction.
If the previous clip ended with a selling lead-in, finish that selling thought straight away.
```

### Spoken style target

```text
The first spoken clause should sound like a direct continuation, for example:
- "...dan paling penting, memang mudah capai."
- "...jadi tak payah fikir stok selalu habis."
- "...itu yang buat dia rasa lebih praktikal."
```

### Bridge-out examples for Block 1

```text
Use endings like:
- "...sebab yang bezakan dia,"
- "...yang buat aku terus pilih ni,"
- "...sebab dekat situ nampak,"
```

---

## Template C — Savage Sell-Through UGC

Use this when the tone is:
- harder sell-through
- higher conviction
- stronger CTA energy

### Block 2 opener rule

```text
Continue the next clip from the previous clip's carried-over ending motion, then continue the line with near-zero hesitation.
Speech should resume within 0.5s–0.8s.
Use only a small nod, small push, or micro-tilt while speaking.
Do not stage a silent beauty moment before the CTA continuation.
If the previous clip already pressured the viewer, the next clip must land the payoff immediately instead of cooling down.
```

### Spoken style target

```text
The first spoken clause should sound like momentum carrying forward, for example:
- "...sebab tu ramai terus repeat order."
- "...jadi kalau nak yang lebih mudah, ambil yang ni."
- "...memang ini yang paling senang untuk jalan cepat."
```

### Bridge-out examples for Block 1

```text
Use endings like:
- "...sebab yang orang cari sebenarnya,"
- "...yang buat ramai terus ambil,"
- "...sebab kalau lambat fikir,"
```

---

## Copy-Paste Seam Injection Block

Use this block directly inside GROK Block 2 prompt construction:

```text
Continue seamlessly from the previous clip's exact ending motion and carried-over state. Resume spoken dialogue within the first 0.5s–1.0s. Opening motion is micro-continuation only: a slight tilt, small nod, or tiny hand adjustment while the sentence continues. Do not spend the early part of the clip on silent setup, long product repositioning, or a reset pose. The seam must feel like one continuous spoken recommendation.
```

Interpretation note:
- in final operator-facing prompts, prefer `previous clip` language rather than `Block 1`
- `exact ending motion and carried-over state` means seamless motion continuity from the previous clip
- it does **not** mean a static pose reference or a frozen image-style end pose

---

## When To Use

Use this file when:
- Block 2 feels late
- lipsync mismatch appears near the seam
- dialogue continuation feels detached
- GROK extension looks like it pauses before talking again
