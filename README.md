# YUNG's Better Jungle Temples for Sunrise

Jungle temples redesigned as overgrown ruins with traps, puzzles and a treasure room.

A port of [YUNG's Better Jungle Temples](https://github.com/YUNG-GANG/YUNGs-Better-Jungle-Temples) by YUNGNICKYOUNG and Tera to [Sunrise](https://playsunrise.net) (Minecraft Java 26.3). It is a content mod: the original's structures, templates, loot tables and strings, upgraded to 26.3, with no code. The 26.3 carry is by AdLf0208 ([AdLf0208/yungs_better_jungle_temples](https://github.com/AdLf0208/yungs_better_jungle_temples)); this fork moves it to Sunrise.

## What it adds

- A new jungle temple: an overgrown ruin of 127 templates over several floors, with traps, a challenge room, a treasure room and a campsite outside.
- Its own placement with YUNG's rules: no oceans or rivers nearby, and an exclusion zone around other temples.
- Its palette, pillar, torch and vine processors, with the original's chances.
- Vanilla jungle temples no longer generate, as in the original (its "Disable Vanilla Jungle Temples" option is on by default).

## Differences from the original

- The pool elements for other mods (Create, Supplementaries, Alex's Mobs) are off, so a temple never names a block that isn't there.

## Building

With the Sunrise mod tool (`cargo sunrise-mod`, from the Sunrise SDK):

```sh
cargo sunrise-mod check
cargo sunrise-mod build    # target/sunrise-mod/betterjungletemples.smod
```

This version is made for the Sunrise Dev build `dev-2026-11-22-7cfdf81`.

## Licence and credits

YUNG's Better Jungle Temples is by YUNGNICKYOUNG and Tera (https://github.com/YUNG-GANG/YUNGs-Better-Jungle-Temples). Its structures, templates, loot tables and strings are theirs and are used here under the **GNU LGPL v3.0 only**, the original's licence; `LICENSE` holds the text.

Carried to Minecraft 26.3 by AdLf0208 ([AdLf0208/yungs_better_jungle_temples](https://github.com/AdLf0208/yungs_better_jungle_temples)), and ported to Sunrise by arismoko. This port is distributed under the same licence.
