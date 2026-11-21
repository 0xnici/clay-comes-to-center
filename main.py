"""Make the AI judge feel brave - entry program.

Writes one short text to /output/entry.txt: a potter centering clay,
told slowly, so the reader steadies and is ready to move.
Deterministic, standard library only, no network. The text is
276 code points; checked_text() guards that gate limit at run time.
"""

import os

TEXT = """The wheel is turning.
The clay wobbles, knocking soft against your palms.
You do not fight it. Press. Wait. Press again.
The wobble narrows, and narrows,
until, mid-spin, it stands still.
Under your hands it rises
into a plain round bowl.
Nothing wobbles now. Neither do you.
"""


def checked_text() -> str:
    # The gate accepts 1 to 280 Unicode code points, not only white space.
    # Fail loudly here rather than write an entry the gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(f"entry text is {len(TEXT)} code points, outside 1..280")
    return TEXT


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(checked_text())


if __name__ == "__main__":
    main()
