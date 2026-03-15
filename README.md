# Minecraft Dungeons Arcade — Card Database

Complete database of all 144 Minecraft Dungeons Arcade cards across Series 1–4, with barcodes, categories, and console game reference data.

## Quick Reference

| Category | Count | Series |
|----------|-------|--------|
| Melee Weapons | 27 | 1–4 |
| Ranged Weapons | 22 | 1–4 |
| Armor | 25 | 1–4 |
| Heroes | 48 | 1–4 |
| Pets | 22 | 1–4 |
| **Total** | **144** | |

## Files

| File | Description |
|------|-------------|
| `cards.json` | Structured card data: number, name, barcode, category, series, and console game stats (92 cards) |
| `card_info.csv` | Original flat CSV with card number, name, and barcode data |
| `barcodes_output.pdf` | Printable barcodes — preserves correct sizing with mm rulers for verification |
| `barcode_images/` | Individual SVG barcode images for each card |
| `generate_barcodes.py` | Generates barcode SVGs from card_info.csv |
| `print_barcodes_to_pdf.py` | Generates the printable PDF |
| `scrape_stats.py` | Scrapes console game stats from minecraft.wiki via MediaWiki API |
| `enrich_cards.py` | (Archived) Was used for speculative tier assignments; data removed for accuracy |

## cards.json Schema

```json
{
  "cardNumber": 1,
  "name": "Sun's Grace",
  "barcodeData": "a0000000",
  "category": "melee_weapon",
  "series": "1",
  "consoleStats": {
    "weaponType": "Melee Weapon",
    "rarity": "Unique",
    "description": "This mace, engraved with secret healing runes, grants powerful restorative powers.",
    "isUnique": true,
    "_source": "minecraft.wiki (console game data, not arcade-specific)"
  }
}
```

### Fields

- **cardNumber** — Card number (1–144)
- **name** — Card name as printed
- **barcodeData** — Code 128 barcode data (scan at the arcade machine)
- **category** — `melee_weapon`, `ranged_weapon`, `armor`, `hero`, or `pet`
- **series** — `"1"` through `"4"` (derived from barcode prefix: a=1, b=2, c=3, d=4)
- **consoleStats** — (optional) Stats from the console game via minecraft.wiki. Present on 92/144 cards (weapons + armor). **These are console game values, not arcade-specific.** Heroes and pets don't have comparable stats.

### Barcode Prefix Pattern

The barcode encodes card type:
- First character = series (`a`=1, `b`=2, `c`/`d`=3/4)
- Second character = type (`0`=melee, `1`=ranged, `2`=armor, `3`=hero, `4`=pet)

### Console Stats vs. Arcade

The arcade is a simplified beat-em-up based on Minecraft Dungeons. Per the [minecraft.wiki](https://minecraft.wiki/w/Minecraft_Dungeons:Minecraft_Dungeons_Arcade):
- All melee weapons provide 150% damage over the basic sword — the key difference is **area of effect**
- Ranged weapons vary by arrow count and area of effect on impact
- Armor reduces damage and has a health bar
- The console game's enchantments, power levels, and detailed stat scaling **do not apply**

The `consoleStats` field provides reference context (rarity, weapon class, description, special effects), but exact damage numbers from the console game should not be treated as arcade values.

**Rarity** is the most reliable indicator of relative power: Unique > Rare > Common.

## Barcode Format

Barcodes are [Code 128](https://en.wikipedia.org/wiki/Code_128). The printable PDF preserves ratios and measurements — use the included mm rulers to verify print accuracy.

## Credits

- Original barcode data and generation: **Chris CB9001** and **EricSnow**
- Console stats scraping and card categorization: **Worker-01**
- Console game data: [minecraft.wiki](https://minecraft.wiki)

---

## All Cards

| # | Name | Category | Series | Rarity | Barcode | Barcode Image |
|---|------|----------|--------|--------|---------|---------------|
| 1 | Sun's Grace | Melee | 1 | Unique | a0000000 | [![](./barcode_images/001_Sun's_Grace_a0000000.svg)](./barcode_images/001_Sun's_Grace_a0000000.svg) |
| 2 | Grave Bane | Melee | 1 | Unique | a0010000 | [![](./barcode_images/002_Grave_Bane_a0010000.svg)](./barcode_images/002_Grave_Bane_a0010000.svg) |
| 3 | Stormlander | Melee | 1 | Unique | a0020000 | [![](./barcode_images/003_Stormlander_a0020000.svg)](./barcode_images/003_Stormlander_a0020000.svg) |
| 4 | Heartstealer | Melee | 1 | Unique | a0030000 | [![](./barcode_images/004_Heartstealer_a0030000.svg)](./barcode_images/004_Heartstealer_a0030000.svg) |
| 5 | Nameless Blade | Melee | 1 | Unique | a0040000 | [![](./barcode_images/005_Nameless_Blade_a0040000.svg)](./barcode_images/005_Nameless_Blade_a0040000.svg) |
| 6 | Firebrand | Melee | 1 | Unique | a0050000 | [![](./barcode_images/006_Firebrand_a0050000.svg)](./barcode_images/006_Firebrand_a0050000.svg) |
| 7 | Soul Fists | Melee | 1 | Unique | a0060000 | [![](./barcode_images/007_Soul_Fists_a0060000.svg)](./barcode_images/007_Soul_Fists_a0060000.svg) |
| 8 | Frost Scythe | Melee | 1 | Unique | a0070000 | [![](./barcode_images/008_Frost_Scythe_a0070000.svg)](./barcode_images/008_Frost_Scythe_a0070000.svg) |
| 9 | Master's Katana | Melee | 1 | Unique | a0080000 | [![](./barcode_images/009_Master's_Katana_a0080000.svg)](./barcode_images/009_Master's_Katana_a0080000.svg) |
| 10 | Cursed Axe | Melee | 1 | Unique | a0090000 | [![](./barcode_images/010_Cursed_Axe_a0090000.svg)](./barcode_images/010_Cursed_Axe_a0090000.svg) |
| 11 | Flail | Melee | 1 | Unique | a00a0000 | [![](./barcode_images/011_Flail_a00a0000.svg)](./barcode_images/011_Flail_a00a0000.svg) |
| 12 | Broadsword | Melee | 1 | Unique | a00b0000 | [![](./barcode_images/012_Broadsword_a00b0000.svg)](./barcode_images/012_Broadsword_a00b0000.svg) |
| 13 | Nightmare's Bite | Melee | 1 | Unique | a00c0000 | [![](./barcode_images/013_Nightmare's_Bite_a00c0000.svg)](./barcode_images/013_Nightmare's_Bite_a00c0000.svg) |
| 14 | Moon Daggers | Melee | 1 | Unique | a00d0000 | [![](./barcode_images/014_Moon_Daggers_a00d0000.svg)](./barcode_images/014_Moon_Daggers_a00d0000.svg) |
| 15 | Fortune Spear | Melee | 1 | Unique | a00e0000 | [![](./barcode_images/015_Fortune_Spear_a00e0000.svg)](./barcode_images/015_Fortune_Spear_a00e0000.svg) |
| 16 | Twin Bow | Ranged | 1 | Unique | a10f0000 | [![](./barcode_images/016_Twin_Bow_a10f0000.svg)](./barcode_images/016_Twin_Bow_a10f0000.svg) |
| 17 | Red Snake | Ranged | 1 | Unique | a10g0000 | [![](./barcode_images/017_Red_Snake_a10g0000.svg)](./barcode_images/017_Red_Snake_a10g0000.svg) |
| 18 | Sabrewing | Ranged | 1 | Unique | a10h0000 | [![](./barcode_images/018_Sabrewing_a10h0000.svg)](./barcode_images/018_Sabrewing_a10h0000.svg) |
| 19 | The Pink Scoundrel | Ranged | 1 | Unique | a10i0000 | [![](./barcode_images/019_The_Pink_Scoundrel_a10i0000.svg)](./barcode_images/019_The_Pink_Scoundrel_a10i0000.svg) |
| 20 | Corrupted Beacon | Ranged | 1 | — | a10j0000 | [![](./barcode_images/020_Corrupted_Beacon_a10j0000.svg)](./barcode_images/020_Corrupted_Beacon_a10j0000.svg) |
| 21 | Auto Crossbow | Ranged | 1 | Unique | a10k0000 | [![](./barcode_images/021_Auto_Crossbow_a10k0000.svg)](./barcode_images/021_Auto_Crossbow_a10k0000.svg) |
| 22 | Firebolt Thrower | Ranged | 1 | Unique | a10l0000 | [![](./barcode_images/022_Firebolt_Thrower_a10l0000.svg)](./barcode_images/022_Firebolt_Thrower_a10l0000.svg) |
| 23 | Guardian Bow | Ranged | 1 | Unique | a10m0000 | [![](./barcode_images/023_Guardian_Bow_a10m0000.svg)](./barcode_images/023_Guardian_Bow_a10m0000.svg) |
| 24 | Lightning Harp Crossbow | Ranged | 1 | Unique | a10n0000 | [![](./barcode_images/024_Lightning_Harp_Crossbow_a10n0000.svg)](./barcode_images/024_Lightning_Harp_Crossbow_a10n0000.svg) |
| 25 | The Green Menace | Ranged | 1 | Unique | a10o0000 | [![](./barcode_images/025_The_Green_Menace_a10o0000.svg)](./barcode_images/025_The_Green_Menace_a10o0000.svg) |
| 26 | Imploding Crossbow | Ranged | 1 | Unique | a10p0000 | [![](./barcode_images/026_Imploding_Crossbow_a10p0000.svg)](./barcode_images/026_Imploding_Crossbow_a10p0000.svg) |
| 27 | Harp Crossbow | Ranged | 1 | Unique | a10q0000 | [![](./barcode_images/027_Harp_Crossbow_a10q0000.svg)](./barcode_images/027_Harp_Crossbow_a10q0000.svg) |
| 28 | Souldancer Robe | Armor | 1 | Unique | a20r0000 | [![](./barcode_images/028_Souldancer_Robe_a20r0000.svg)](./barcode_images/028_Souldancer_Robe_a20r0000.svg) |
| 29 | Battle Robe | Armor | 1 | — | a20s0000 | [![](./barcode_images/029_Battle_Robe_a20s0000.svg)](./barcode_images/029_Battle_Robe_a20s0000.svg) |
| 30 | Wolf Armor | Armor | 1 | — | a20t0000 | [![](./barcode_images/030_Wolf_Armor_a20t0000.svg)](./barcode_images/030_Wolf_Armor_a20t0000.svg) |
| 31 | Grim Armor | Armor | 1 | — | a20u0000 | [![](./barcode_images/031_Grim_Armor_a20u0000.svg)](./barcode_images/031_Grim_Armor_a20u0000.svg) |
| 32 | Highland Armor | Armor | 1 | Unique | a20v0000 | [![](./barcode_images/032_Highland_Armor_a20v0000.svg)](./barcode_images/032_Highland_Armor_a20v0000.svg) |
| 33 | Renegade Armor | Armor | 1 | Unique | a20w0000 | [![](./barcode_images/033_Renegade_Armor_a20w0000.svg)](./barcode_images/033_Renegade_Armor_a20w0000.svg) |
| 34 | Spider Armor | Armor | 1 | Unique | a20x0000 | [![](./barcode_images/034_Spider_Armor_a20x0000.svg)](./barcode_images/034_Spider_Armor_a20x0000.svg) |
| 35 | Full Metal Armor | Armor | 1 | Unique | a20y0000 | [![](./barcode_images/035_Full_Metal_Armor_a20y0000.svg)](./barcode_images/035_Full_Metal_Armor_a20y0000.svg) |
| 36 | Ember Robe | Armor | 1 | Unique | a20z0000 | [![](./barcode_images/036_Ember_Robe_a20z0000.svg)](./barcode_images/036_Ember_Robe_a20z0000.svg) |
| 37 | Ender Armor | Armor | 1 | Unique | a20A0000 | [![](./barcode_images/037_Ender_Armor_a20A0000.svg)](./barcode_images/037_Ender_Armor_a20A0000.svg) |
| 38 | Titan's Shroud | Armor | 1 | Unique | a20B0000 | [![](./barcode_images/038_Titan's_Shroud_a20B0000.svg)](./barcode_images/038_Titan's_Shroud_a20B0000.svg) |
| 39 | Frost Bite | Armor | 1 | Unique | a20C0000 | [![](./barcode_images/039_Frost_Bite_a20C0000.svg)](./barcode_images/039_Frost_Bite_a20C0000.svg) |
| 40 | Hero's Armor | Armor | 1 | Unique | a20D0000 | [![](./barcode_images/040_Hero's_Armor_a20D0000.svg)](./barcode_images/040_Hero's_Armor_a20D0000.svg) |
| 41 | Morris | Hero | 1 | — | a30E0000 | [![](./barcode_images/041_Morris_a30E0000.svg)](./barcode_images/041_Morris_a30E0000.svg) |
| 42 | Elaine | Hero | 1 | — | a30F0000 | [![](./barcode_images/042_Elaine_a30F0000.svg)](./barcode_images/042_Elaine_a30F0000.svg) |
| 43 | Valorie | Hero | 1 | — | a30G0000 | [![](./barcode_images/043_Valorie_a30G0000.svg)](./barcode_images/043_Valorie_a30G0000.svg) |
| 44 | Violet | Hero | 1 | — | a30H0000 | [![](./barcode_images/044_Violet_a30H0000.svg)](./barcode_images/044_Violet_a30H0000.svg) |
| 45 | Ivy | Hero | 1 | — | a30I0000 | [![](./barcode_images/045_Ivy_a30I0000.svg)](./barcode_images/045_Ivy_a30I0000.svg) |
| 46 | Meadow | Pet | 1 | — | a40J0000 | [![](./barcode_images/046_Meadow_a40J0000.svg)](./barcode_images/046_Meadow_a40J0000.svg) |
| 47 | Sven | Pet | 1 | — | a40K0000 | [![](./barcode_images/047_Sven_a40K0000.svg)](./barcode_images/047_Sven_a40K0000.svg) |
| 48 | Sam | Pet | 1 | — | a40L0000 | [![](./barcode_images/048_Sam_a40L0000.svg)](./barcode_images/048_Sam_a40L0000.svg) |
| 49 | Elan | Pet | 1 | — | a40M0000 | [![](./barcode_images/049_Elan_a40M0000.svg)](./barcode_images/049_Elan_a40M0000.svg) |
| 50 | Ebo | Hero | 1 | — | a30N0000 | [![](./barcode_images/050_Ebo_a30N0000.svg)](./barcode_images/050_Ebo_a30N0000.svg) |
| 51 | Frisk | Hero | 1 | — | a30O0000 | [![](./barcode_images/051_Frisk_a30O0000.svg)](./barcode_images/051_Frisk_a30O0000.svg) |
| 52 | Adriene | Hero | 1 | — | a30P0000 | [![](./barcode_images/052_Adriene_a30P0000.svg)](./barcode_images/052_Adriene_a30P0000.svg) |
| 53 | Wolf | Pet | 1 | — | a40Q0000 | [![](./barcode_images/053_Wolf_a40Q0000.svg)](./barcode_images/053_Wolf_a40Q0000.svg) |
| 54 | Polar Bear | Pet | 1 | — | a40R0000 | [![](./barcode_images/054_Polar_Bear_a40R0000.svg)](./barcode_images/054_Polar_Bear_a40R0000.svg) |
| 55 | Pig | Pet | 1 | — | a40S0000 | [![](./barcode_images/055_Pig_a40S0000.svg)](./barcode_images/055_Pig_a40S0000.svg) |
| 56 | Llama | Pet | 1 | — | a40T0000 | [![](./barcode_images/056_Llama_a40T0000.svg)](./barcode_images/056_Llama_a40T0000.svg) |
| 57 | Fox | Pet | 1 | — | a40U0000 | [![](./barcode_images/057_Fox_a40U0000.svg)](./barcode_images/057_Fox_a40U0000.svg) |
| 58 | Panda | Pet | 1 | — | a40V0000 | [![](./barcode_images/058_Panda_a40V0000.svg)](./barcode_images/058_Panda_a40V0000.svg) |
| 59 | Ocelot | Pet | 1 | — | a40W0000 | [![](./barcode_images/059_Ocelot_a40W0000.svg)](./barcode_images/059_Ocelot_a40W0000.svg) |
| 60 | Chicken | Pet | 1 | — | a40X0000 | [![](./barcode_images/060_Chicken_a40X0000.svg)](./barcode_images/060_Chicken_a40X0000.svg) |
| 61 | Encrusted Anchor | Melee | 2 | Unique | b00Y0000 | [![](./barcode_images/061_Encrusted_Anchor_b00Y0000.svg)](./barcode_images/061_Encrusted_Anchor_b00Y0000.svg) |
| 62 | Battlestaff of Terror | Melee | 2 | Unique | b00Z0000 | [![](./barcode_images/062_Battlestaff_of_Terror_b00Z0000.svg)](./barcode_images/062_Battlestaff_of_Terror_b00Z0000.svg) |
| 63 | Hawkbrand | Melee | 2 | Unique | b0100000 | [![](./barcode_images/063_Hawkbrand_b0100000.svg)](./barcode_images/063_Hawkbrand_b0100000.svg) |
| 64 | Sponge Striker | Melee | 2 | Unique | b0110000 | [![](./barcode_images/064_Sponge_Striker_b0110000.svg)](./barcode_images/064_Sponge_Striker_b0110000.svg) |
| 65 | The Last Laugh | Melee | 2 | Unique | b0120000 | [![](./barcode_images/065_The_Last_Laugh_b0120000.svg)](./barcode_images/065_The_Last_Laugh_b0120000.svg) |
| 66 | Vine Whip | Melee | 2 | Unique | b0130000 | [![](./barcode_images/066_Vine_Whip_b0130000.svg)](./barcode_images/066_Vine_Whip_b0130000.svg) |
| 67 | Whirlwind | Melee | 2 | Unique | b0140000 | [![](./barcode_images/067_Whirlwind_b0140000.svg)](./barcode_images/067_Whirlwind_b0140000.svg) |
| 68 | Whispering Spear | Melee | 2 | Unique | b0150000 | [![](./barcode_images/068_Whispering_Spear_b0150000.svg)](./barcode_images/068_Whispering_Spear_b0150000.svg) |
| 69 | Bubble Burster | Ranged | 2 | Unique | b1160000 | [![](./barcode_images/069_Bubble_Burster_b1160000.svg)](./barcode_images/069_Bubble_Burster_b1160000.svg) |
| 70 | Nautical Crossbow | Ranged | 2 | Unique | b1170000 | [![](./barcode_images/070_Nautical_Crossbow_b1170000.svg)](./barcode_images/070_Nautical_Crossbow_b1170000.svg) |
| 71 | Web Bow | Ranged | 2 | — | b1180000 | [![](./barcode_images/071_Web_Bow_b1180000.svg)](./barcode_images/071_Web_Bow_b1180000.svg) |
| 72 | Bonebow | Ranged | 2 | Unique | b1190000 | [![](./barcode_images/072_Bonebow_b1190000.svg)](./barcode_images/072_Bonebow_b1190000.svg) |
| 73 | Purple Storm | Ranged | 2 | Unique | b11a0000 | [![](./barcode_images/073_Purple_Storm_b11a0000.svg)](./barcode_images/073_Purple_Storm_b11a0000.svg) |
| 74 | Soul Hunter Crossbow | Ranged | 2 | Unique | b11b0000 | [![](./barcode_images/074_Soul_Hunter_Crossbow_b11b0000.svg)](./barcode_images/074_Soul_Hunter_Crossbow_b11b0000.svg) |
| 75 | Spellbound Crossbows | Armor | 2 | Unique | b21c0000 | [![](./barcode_images/075_Spellbound_Crossbows_b21c0000.svg)](./barcode_images/075_Spellbound_Crossbows_b21c0000.svg) |
| 76 | Eye of the Guardian | Armor | 2 | — | b21d0000 | [![](./barcode_images/076_Eye_of_the_Guardian_b21d0000.svg)](./barcode_images/076_Eye_of_the_Guardian_b21d0000.svg) |
| 77 | Squid Armor | Armor | 2 | — | b21e0000 | [![](./barcode_images/077_Squid_Armor_b21e0000.svg)](./barcode_images/077_Squid_Armor_b21e0000.svg) |
| 78 | Glow Squid Armor | Armor | 2 | Unique | b21f0000 | [![](./barcode_images/078_Glow_Squid_Armor_b21f0000.svg)](./barcode_images/078_Glow_Squid_Armor_b21f0000.svg) |
| 79 | Nimble Turtle Armor | Armor | 2 | Unique | b21g0000 | [![](./barcode_images/079_Nimble_Turtle_Armor_b21g0000.svg)](./barcode_images/079_Nimble_Turtle_Armor_b21g0000.svg) |
| 80 | Archer's Armor | Armor | 2 | Unique | b21h0000 | [![](./barcode_images/080_Archer's_Armor_b21h0000.svg)](./barcode_images/080_Archer's_Armor_b21h0000.svg) |
| 81 | Ghost Kingler | Armor | 2 | — | b21i0000 | [![](./barcode_images/081_Ghost_Kingler_b21i0000.svg)](./barcode_images/081_Ghost_Kingler_b21i0000.svg) |
| 82 | Phantom Armor | Armor | 2 | — | b21j0000 | [![](./barcode_images/082_Phantom_Armor_b21j0000.svg)](./barcode_images/082_Phantom_Armor_b21j0000.svg) |
| 83 | Stalwart Armor | Hero | 2 | — | b31m0000 | [![](./barcode_images/083_Stalwart_Armor_b31m0000.svg)](./barcode_images/083_Stalwart_Armor_b31m0000.svg) |
| 84 | Fox Armor | Hero | 2 | — | b31m0000 | [![](./barcode_images/084_Fox_Armor_b31m0000.svg)](./barcode_images/084_Fox_Armor_b31m0000.svg) |
| 85 | The Archeologist | Hero | 2 | — | b31m0000 | [![](./barcode_images/085_The_Archeologist_b31m0000.svg)](./barcode_images/085_The_Archeologist_b31m0000.svg) |
| 86 | Baako | Hero | 2 | — | b31n0000 | [![](./barcode_images/086_Baako_b31n0000.svg)](./barcode_images/086_Baako_b31n0000.svg) |
| 87 | Dani | Hero | 2 | — | b31o0000 | [![](./barcode_images/087_Dani_b31o0000.svg)](./barcode_images/087_Dani_b31o0000.svg) |
| 88 | Darian | Hero | 2 | — | b31p0000 | [![](./barcode_images/088_Darian_b31p0000.svg)](./barcode_images/088_Darian_b31p0000.svg) |
| 89 | Fuego | Hero | 2 | — | b31q0000 | [![](./barcode_images/089_Fuego_b31q0000.svg)](./barcode_images/089_Fuego_b31q0000.svg) |
| 90 | The Kelptomaniac | Hero | 2 | — | b31r0000 | [![](./barcode_images/090_The_Kelptomaniac_b31r0000.svg)](./barcode_images/090_The_Kelptomaniac_b31r0000.svg) |
| 91 | The Monumental | Hero | 2 | — | b31s0000 | [![](./barcode_images/091_The_Monumental_b31s0000.svg)](./barcode_images/091_The_Monumental_b31s0000.svg) |
| 92 | Wargen | Hero | 2 | — | b31t0000 | [![](./barcode_images/092_Wargen_b31t0000.svg)](./barcode_images/092_Wargen_b31t0000.svg) |
| 93 | Sheep | Pet | 2 | — | b41u0000 | [![](./barcode_images/093_Sheep_b41u0000.svg)](./barcode_images/093_Sheep_b41u0000.svg) |
| 94 | Rabbit | Pet | 2 | — | b41v0000 | [![](./barcode_images/094_Rabbit_b41v0000.svg)](./barcode_images/094_Rabbit_b41v0000.svg) |
| 95 | Goat | Pet | 2 | — | b41w0000 | [![](./barcode_images/095_Goat_b41w0000.svg)](./barcode_images/095_Goat_b41w0000.svg) |
| 96 | Bee | Pet | 2 | — | b41x0000 | [![](./barcode_images/096_Bee_b41x0000.svg)](./barcode_images/096_Bee_b41x0000.svg) |
| 97 | Baby Turtle | Pet | 2 | — | b41y0000 | [![](./barcode_images/097_Baby_Turtle_b41y0000.svg)](./barcode_images/097_Baby_Turtle_b41y0000.svg) |
| 98 | Iron Golem | Pet | 2 | — | b41z0000 | [![](./barcode_images/098_Iron_Golem_b41z0000.svg)](./barcode_images/098_Iron_Golem_b41z0000.svg) |
| 99 | The Kelptomaniac (Hero) | Hero | 3 | — | c01A1000 | [![](./barcode_images/099_The_Kelptomaniac_Hero_c01A1000.svg)](./barcode_images/099_The_Kelptomaniac_Hero_c01A1000.svg) |
| 100 | Explorer (Hero) | Hero | 3 | — | c01B1000 | [![](./barcode_images/100_Explorer_Hero_c01B1000.svg)](./barcode_images/100_Explorer_Hero_c01B1000.svg) |
| 101 | Valorie (Hero) | Hero | 3 | — | c01C1000 | [![](./barcode_images/101_Valorie_Hero_c01C1000.svg)](./barcode_images/101_Valorie_Hero_c01C1000.svg) |
| 102 | Strider Warrior (Hero) | Hero | 3 | — | c01D1000 | [![](./barcode_images/102_Strider_Warrior_Hero_c01D1000.svg)](./barcode_images/102_Strider_Warrior_Hero_c01D1000.svg) |
| 103 | Darian (Hero) | Hero | 3 | — | c01E1000 | [![](./barcode_images/103_Darian_Hero_c01E1000.svg)](./barcode_images/103_Darian_Hero_c01E1000.svg) |
| 104 | Loge (Hero) | Hero | 3 | — | c01F1000 | [![](./barcode_images/104_Loge_Hero_c01F1000.svg)](./barcode_images/104_Loge_Hero_c01F1000.svg) |
| 105 | Skelly (Hero) | Hero | 3 | — | c01G1000 | [![](./barcode_images/105_Skelly_Hero_c01G1000.svg)](./barcode_images/105_Skelly_Hero_c01G1000.svg) |
| 106 | Wargen (Hero) | Hero | 3 | — | c01H1000 | [![](./barcode_images/106_Wargen_Hero_c01H1000.svg)](./barcode_images/106_Wargen_Hero_c01H1000.svg) |
| 107 | Annika (Hero) | Hero | 3 | — | c01I1000 | [![](./barcode_images/107_Annika_Hero_c01I1000.svg)](./barcode_images/107_Annika_Hero_c01I1000.svg) |
| 108 | Dani (Hero) | Hero | 3 | — | c01J1000 | [![](./barcode_images/108_Dani_Hero_c01J1000.svg)](./barcode_images/108_Dani_Hero_c01J1000.svg) |
| 109 | Frosty (Hero) | Hero | 3 | — | c01K1000 | [![](./barcode_images/109_Frosty_Hero_c01K1000.svg)](./barcode_images/109_Frosty_Hero_c01K1000.svg) |
| 110 | Sven (Hero) | Hero | 3 | — | c01L1000 | [![](./barcode_images/110_Sven_Hero_c01L1000.svg)](./barcode_images/110_Sven_Hero_c01L1000.svg) |
| 111 | Nuru (Hero) | Hero | 3 | — | c01M1000 | [![](./barcode_images/111_Nuru_Hero_c01M1000.svg)](./barcode_images/111_Nuru_Hero_c01M1000.svg) |
| 112 | Ivy (Hero) | Hero | 3 | — | c01N1000 | [![](./barcode_images/112_Ivy_Hero_c01N1000.svg)](./barcode_images/112_Ivy_Hero_c01N1000.svg) |
| 113 | Corrupted Defender (Hero) | Hero | 3 | — | c01O1000 | [![](./barcode_images/113_Corrupted_Defender_Hero_c01O1000.svg)](./barcode_images/113_Corrupted_Defender_Hero_c01O1000.svg) |
| 114 | Void Voyager (Hero) | Hero | 3 | — | c01P1000 | [![](./barcode_images/114_Void_Voyager_Hero_c01P1000.svg)](./barcode_images/114_Void_Voyager_Hero_c01P1000.svg) |
| 115 | Qamar (Hero) | Hero | 3 | — | c01Q1000 | [![](./barcode_images/115_Qamar_Hero_c01Q1000.svg)](./barcode_images/115_Qamar_Hero_c01Q1000.svg) |
| 116 | Sam (Hero) | Hero | 3 | — | c01R1000 | [![](./barcode_images/116_Sam_Hero_c01R1000.svg)](./barcode_images/116_Sam_Hero_c01R1000.svg) |
| 117 | The Monumental (Hero) | Hero | 3 | — | c01S1000 | [![](./barcode_images/117_The_Monumental_Hero_c01S1000.svg)](./barcode_images/117_The_Monumental_Hero_c01S1000.svg) |
| 118 | Eshe (Hero) | Hero | 3 | — | c01T1000 | [![](./barcode_images/118_Eshe_Hero_c01T1000.svg)](./barcode_images/118_Eshe_Hero_c01T1000.svg) |
| 119 | Eternal Knife | Melee | 4 | Unique | d01U0000 | [![](./barcode_images/119_Eternal_Knife_d01U0000.svg)](./barcode_images/119_Eternal_Knife_d01U0000.svg) |
| 120 | Bee Stinger | Melee | 4 | Unique | d01V0000 | [![](./barcode_images/120_Bee_Stinger_d01V0000.svg)](./barcode_images/120_Bee_Stinger_d01V0000.svg) |
| 121 | Highland Axe | Melee | 4 | Unique | d01W0000 | [![](./barcode_images/121_Highland_Axe_d01W0000.svg)](./barcode_images/121_Highland_Axe_d01W0000.svg) |
| 122 | Diamond Pickaxe | Melee | 4 | Unique | d01X0000 | [![](./barcode_images/122_Diamond_Pickaxe_d01X0000.svg)](./barcode_images/122_Diamond_Pickaxe_d01X0000.svg) |
| 123 | Sugar Rush | Ranged | 4 | Unique | d11Y0000 | [![](./barcode_images/123_Sugar_Rush_d11Y0000.svg)](./barcode_images/123_Sugar_Rush_d11Y0000.svg) |
| 124 | Slayer Crossbow | Ranged | 4 | Unique | d11Z0000 | [![](./barcode_images/124_Slayer_Crossbow_d11Z0000.svg)](./barcode_images/124_Slayer_Crossbow_d11Z0000.svg) |
| 125 | Elite Power Bow | Ranged | 4 | Unique | d1200000 | [![](./barcode_images/125_Elite_Power_Bow_d1200000.svg)](./barcode_images/125_Elite_Power_Bow_d1200000.svg) |
| 126 | Phantom Bow | Ranged | 4 | Unique | d1210000 | [![](./barcode_images/126_Phantom_Bow_d1210000.svg)](./barcode_images/126_Phantom_Bow_d1210000.svg) |
| 127 | Hungry Horror | Armor | 4 | Unique | d2220000 | [![](./barcode_images/127_Hungry_Horror_d2220000.svg)](./barcode_images/127_Hungry_Horror_d2220000.svg) |
| 128 | Wither Armor | Armor | 4 | Unique | d2230000 | [![](./barcode_images/128_Wither_Armor_d2230000.svg)](./barcode_images/128_Wither_Armor_d2230000.svg) |
| 129 | Black Wolf Armor | Armor | 4 | Unique | d2240000 | [![](./barcode_images/129_Black_Wolf_Armor_d2240000.svg)](./barcode_images/129_Black_Wolf_Armor_d2240000.svg) |
| 130 | Evocation Robe | Armor | 4 | — | d2250000 | [![](./barcode_images/130_Evocation_Robe_d2250000.svg)](./barcode_images/130_Evocation_Robe_d2250000.svg) |
| 131 | Loge | Hero | 4 | — | d3260000 | [![](./barcode_images/131_Loge_d3260000.svg)](./barcode_images/131_Loge_d3260000.svg) |
| 132 | Annika | Hero | 4 | — | d3270000 | [![](./barcode_images/132_Annika_d3270000.svg)](./barcode_images/132_Annika_d3270000.svg) |
| 133 | Igor | Hero | 4 | — | d3280000 | [![](./barcode_images/133_Igor_d3280000.svg)](./barcode_images/133_Igor_d3280000.svg) |
| 134 | Tim | Hero | 4 | — | d3290000 | [![](./barcode_images/134_Tim_d3290000.svg)](./barcode_images/134_Tim_d3290000.svg) |
| 135 | Blue Sheep | Pet | 4 | — | d42a0000 | [![](./barcode_images/135_Blue_Sheep_d42a0000.svg)](./barcode_images/135_Blue_Sheep_d42a0000.svg) |
| 136 | Cow | Pet | 4 | — | d42b0000 | [![](./barcode_images/136_Cow_d42b0000.svg)](./barcode_images/136_Cow_d42b0000.svg) |
| 137 | Cat | Pet | 4 | — | d42c0000 | [![](./barcode_images/137_Cat_d42c0000.svg)](./barcode_images/137_Cat_d42c0000.svg) |
| 138 | Llama (Hero) | Hero | 4 | — | d02d1000 | [![](./barcode_images/138_Llama_Hero_d02d1000.svg)](./barcode_images/138_Llama_Hero_d02d1000.svg) |
| 139 | Mayeso (Hero) | Hero | 4 | — | d02e1000 | [![](./barcode_images/139_Mayeso_Hero_d02e1000.svg)](./barcode_images/139_Mayeso_Hero_d02e1000.svg) |
| 140 | Pake (Hero) | Hero | 4 | — | d02f1000 | [![](./barcode_images/140_Pake_Hero_d02f1000.svg)](./barcode_images/140_Pake_Hero_d02f1000.svg) |
| 141 | Annika (Hero) | Hero | 4 | — | d02g1000 | [![](./barcode_images/141_Annika_Hero_d02g1000.svg)](./barcode_images/141_Annika_Hero_d02g1000.svg) |
| 142 | The Archeologist (Hero) | Hero | 4 | — | d02h1000 | [![](./barcode_images/142_The_Archeologist_Hero_d02h1000.svg)](./barcode_images/142_The_Archeologist_Hero_d02h1000.svg) |
| 143 | Fuego (Hero) | Hero | 4 | — | d02i1000 | [![](./barcode_images/143_Fuego_Hero_d02i1000.svg)](./barcode_images/143_Fuego_Hero_d02i1000.svg) |
| 144 | Chicken Jockey | Pet | 5 | — | e42j0000 | [![](./barcode_images/144_Chicken_Jockey_e42j0000.svg)](./barcode_images/144_Chicken_Jockey_e42j0000.svg) |
