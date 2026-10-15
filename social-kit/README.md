# Parent Survival · Social post kit

A brief and template for producing Parent Survival social ads and posts. Read this whole file before writing anything.

## Files

- `concepts.js`: **the only file you normally edit.** It holds one object per concept (copy, theme, headline sizes).
- `template.html`: renders every concept in four sizes. Open it in a browser to review all concepts. `template.html?id=3A&size=1080x1350` renders a single artboard.
- `render.mjs`: exports PNGs. Run `npm i puppeteer && node render.mjs` and the files appear in `out/`.
- `assets/logo-badge.png`: the round badge logo. Use it for profile and avatar images only, not inside ads. Ads use the header lockup, which the template draws.
- `reference/`: approved examples from the existing ad set. Match them.

## Sizes (always produce all four)

| Size | Use |
|---|---|
| 1200 × 628 | Facebook link ads. Text on the left, card on the right. |
| 1080 × 1920 | Stories and Reels. Content sits between y=300 and y≈1600, so keep the top 250px and bottom 340px clear. |
| 1080 × 1350 | 4:5 feed. Uses the long price line. |
| 1080 × 1080 | 1:1 feed. Headline and short subline only, no card. |

## Brand (taken from the live site screenshots)

- **Type:** Playfair Display 800 for headlines (tight, letter-spacing −2 to −3px). DM Sans for everything else: light (300) for sublines, 600 uppercase with wide letter-spacing for eyebrows, 700 for buttons.
- **Lockup:** a small filled circle with a heart, then "Parent Survival" in Playfair 800. It always sits top-left.
- **Backgrounds (themes):** beige `#EFE5DD`, cream `#F6F1EA`, blush `#FCF5F2`, plum `#2E1F30`, lilac `#BAA3C0`, rose `#E8B5AE`, peach `#F4C8B8`. Ink is `#1D1B17`; plum backgrounds use cream ink and peach accents.
- **Card:** white (a dark plum tint on plum backgrounds), 1px hairline border, 26–28px corner radius. It contains an optional rose eyebrow, a Playfair title and an optional DM Sans body.
- **Button:** plum pill with white text (peach pill on plum backgrounds), followed by a price line in the subline colour.
- **No** photos, illustrations, emoji, gradients or extra decoration. The look is type and colour only.

## Anatomy of a concept

| Field | What it is | Guide |
|---|---|---|
| `headline` | A relatable moment, or a gentle reframe | 4–10 words, present tense, specific (a time, a place, an object) |
| `subline` | What's really going on, and that it can be helped | 1–2 short sentences, ≤ 22 words |
| `subShort` | Subline cut down for 1:1 | ≤ 8 words |
| `eyebrow` | Label for the card, e.g. `Say this`, `Try this tonight · Bedtime`, `Your week · Mornings`, `For you · Parent reflection` | `null` hides it |
| `cardTitle` | One concrete thing to try or say | Use quote marks if it's a script line. Set `cardItalic:true` for a quiet italic line with no eyebrow. |
| `cardBody` | Why it works, or how to do it | ≤ 14 words, or `null` |
| `cta` / `priceShort` / `priceLong` | Use approved pairs only (below) | |
| `sizes` | Headline px for [628, 1920, 1350, 1080] | Defaults `[56,104,98,86]`. Go down in steps of 4 if a headline runs past 4 lines (Story/4:5) or 3 lines (1:1/628). |

**Approved buttons and price lines**

- `Start free` · `Plus from £7.99 a month.` · `Plus from £7.99 a month. Cancel any time.`
- `Free check-in` · `Plus from £7.99 a month.` · `Plus from £7.99 a month for the ongoing plan.`
- `Get my plan` / `Get your plan` · `Plus, £7.99 a month.` · `Plus, £7.99 a month. Start with a free check-in.`
- `Start the reset` · `Plus, £7.99 a month.` · `Plus, £7.99 a month. Previews are free.`
- `Try the cards` / `Get all 200` · `Plus, £7.99 a month.` · `Plus, £7.99 a month. Samples are free.`
- `Find your circle` · `Together, £12.99 a month.` · `Together, £12.99 a month. Start with a free check-in.`

Check current prices on parentsurvival.co.uk before you publish.

## Tone

- Warm, calm, British, and written to "you". Name the moment as it actually happens ("It's the fourth goodnight and nobody is asleep.").
- Practical: give one small, specific thing to try. Never a list of forty.
- No guilt, fear, shaming or "you're doing it wrong". No "perfect family".
- Write for adults. Nothing childish or cutesy.
- **Never invent** statistics, research claims, testimonials or parent quotes. Only use numbers that Parent Survival has supplied. Keep advice general and low-risk, and nothing medical.
- Use British spelling and punctuation, with curly quotes (“ ” ’).

## Rotate themes

Don't put two neighbouring concepts in the same theme. Use plum or lilac about once in every four, as accent posts.

## Topics already used (don't repeat the headline angle)

Bedtime (4-week reset, fourth goodnight), after school (crash, one step at a time), mornings (shoes/bag/teeth/door), screen time (handover, ten more minutes), check-in, weekly plan (forty articles / Tuesday), Circles (refereeing since 7am), conversation cards ("How was school?" "Fine."), scripts, siblings, homework, parent reflection, public meltdown, teen phones.

Ideas not yet covered: car journeys, mealtimes and fussy eating, the school run, transitions such as leaving the park, sleepovers, holidays and routines, parent burnout, co-parenting handovers, starting school, exam stress (12+), weekends.

## Workflow

1. Add new concepts to `concepts.js`. Give them the next ids (e.g. `4A`, `4B`…).
2. Open `template.html` and check all four sizes. Make sure nothing overflows, no card hits the button, and no headline runs past its line limit.
3. Run `node render.mjs` and check the PNGs in `out/`.
4. With each batch, send back a table with: id, topic, headline, the claim the card makes (so a person can sense-check the advice), and suggested caption text with no more than 3 hashtags.
