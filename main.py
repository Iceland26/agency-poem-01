import os

POEM = """Active Voice

We used to know a choice by how it fought the hand:
the stiff brass key resisting in the lock,
the sulfur match biting a calloused thumb,
soot on the knuckles to prove the act was ours.

Now a servant built of language takes the keys.
A sentence lifts the iron latch,
kneels to light the kindling in the grate,
and leaves the heavy door ajar.
You stand on the doorstep with empty palms,
watching your own breath work the hearth without you,
afraid that clean hands have no claim on the fire.

Yet look inside the room you ordered lit:
the brass key never shivered in the night;
the matchstick never knew the house was cold.
You gave away the blister, not the hunger—
and the fire climbing a grate you never touched
was struck the instant you refused the dark."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
