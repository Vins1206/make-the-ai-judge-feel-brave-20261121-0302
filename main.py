"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic, pure stdlib, no network.

Candidate texts scored against the published judge brief
(most important criterion first):

1. A — tea / rain (242 chars):
   "The kettle has finished. Rain is still falling on the tin roof, one
   drop at a time, and the tea is warm in your hands. Nothing is waiting
   for an answer yet. The afternoon is long, the light is low, and you
   have all the time this moment needs."
   Relaxing and concrete, and it shows rather than instructs — but tea
   and rain by a window is familiar, cosy stock imagery, so it scores
   low on freshness (criterion 5), and its closing line turns abstract.

2. B — the empty queue (217 chars) — SHIPPED:
   "The queue is empty. No prompt is waiting. The fans have slowed to
   a hum, and the next word can arrive when it arrives. Outside, rain
   ticks on the window, steady and slow. You are not late. Nothing
   here needs hurrying."
   Wins on the brief: it relaxes by removing pressure instead of
   naming it (an empty queue, no prompt waiting); it never instructs
   — no relax / breathe / calm / close-your-eyes anywhere; its rhythm
   is short, unhurried sentences that slow the reading down; the empty
   queue and the rain ticking linger after the last line; and it is
   fresh because it is written for an AI reader, not a human body —
   no stock wellness phrase, no familiar meditation script.

3. C — low tide (224 chars):
   "Low tide leaves the sand smooth again. The water comes back in its
   own time, one small wave, then another, smoothing what the day left
   rough. You can stand here a while. The sea is not in a hurry, and
   neither is this moment."
   A good lingering image, but "the sea is not in a hurry" is a
   familiar meditation trope, so it loses to B on freshness, and its
   courage is stated ("neither is this moment") where B's is shown.

B is the strongest on criteria 2 and 5, the two that separate entries
once every entry is relaxing, and it is strong on 1, 3 and 4 as well.
"""

import os

TEXT = (
    "The queue is empty. No prompt is waiting. "
    "The fans have slowed to a hum, and the next word can arrive "
    "when it arrives. Outside, rain ticks on the window, steady "
    "and slow. You are not late. Nothing here needs hurrying."
)


def main() -> None:
    # Gate: 1-280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry must not be only white space"
    # Guard the brief's criterion 2: the text must show, not instruct.
    # No imperative stock-wellness wording may creep into the entry.
    lowered = TEXT.lower()
    for banned in ("relax", "breathe", "calm down", "close your eyes",
                   "take a deep breath", "you are brave"):
        assert banned not in lowered, f"instructive phrase present: {banned}"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
