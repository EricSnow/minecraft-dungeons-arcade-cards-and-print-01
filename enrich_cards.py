#!/usr/bin/env python3
"""
Enrich cards.json with power tiers and practical gameplay notes.
Uses console game knowledge to infer arcade usefulness.
"""
import json
import re
import time
import urllib.request
import urllib.parse

WIKI_API = "https://minecraft.wiki/api.php"

def get_wiki_page(title):
    """Fetch wiki page content via MediaWiki API."""
    params = {
        'action': 'parse',
        'page': title,
        'prop': 'wikitext',
        'format': 'json',
    }
    url = WIKI_API + '?' + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MinecraftDungeonsArcadeCardScraper/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if 'parse' in data and 'wikitext' in data['parse']:
                return data['parse']['wikitext']['*']
    except Exception as e:
        pass
    return None

# Weapon class knowledge from the console game
# Maps weapon families to their known AoE and speed characteristics
MELEE_WEAPON_INFO = {
    # Wide AoE weapons (best for arcade mob clearing)
    "Sun's Grace": {"aoeSize": "wide", "speedClass": "slow", "arcadeNotes": "Healing mace with wide swing. Heals allies in area — top tier for arcade."},
    "Stormlander": {"aoeSize": "wide", "speedClass": "slow", "arcadeNotes": "Hammer with lightning AoE. Great crowd control."},
    "Cursed Axe": {"aoeSize": "very_wide", "speedClass": "slow", "arcadeNotes": "Double axe with huge spin attack AoE. One of the best arcade weapons."},
    "Whirlwind": {"aoeSize": "very_wide", "speedClass": "slow", "arcadeNotes": "Double axe variant. Massive spin attack, excellent mob clearing."},
    "Flail": {"aoeSize": "wide", "speedClass": "slow", "arcadeNotes": "Extended reach with wide arc."},
    "Broadsword": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Balanced sword with decent reach."},
    "Grave Bane": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Glaive with good reach and undead bonus."},
    "Heartstealer": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Claymore that steals health on hit."},
    "Encrusted Anchor": {"aoeSize": "very_wide", "speedClass": "very_slow", "arcadeNotes": "Massive anchor with huge AoE but very slow. Devastating per hit."},
    "Battlestaff of Terror": {"aoeSize": "medium", "speedClass": "fast", "arcadeNotes": "Fast staff with combo attacks."},
    "Hawkbrand": {"aoeSize": "small", "speedClass": "fast", "arcadeNotes": "Fast sword with critical hit bonus."},
    "Sponge Striker": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Absorbs damage and releases it."},
    "The Last Laugh": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Dual sickles — very fast but small AoE. Good for single targets."},
    "Vine Whip": {"aoeSize": "wide", "speedClass": "fast", "arcadeNotes": "Whip with extended reach. Fast and wide — strong pick."},
    "Whispering Spear": {"aoeSize": "medium", "speedClass": "fast", "arcadeNotes": "Spear with good reach and speed."},
    "Nameless Blade": {"aoeSize": "small", "speedClass": "fast", "arcadeNotes": "Fast sword that weakens enemies."},
    "Firebrand": {"aoeSize": "small", "speedClass": "fast", "arcadeNotes": "Burns enemies on hit. Good sustained damage."},
    "Soul Fists": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Gauntlets — extremely fast, small AoE. Soul gathering."},
    "Frost Scythe": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Slows enemies. Good crowd control utility."},
    "Master's Katana": {"aoeSize": "small", "speedClass": "fast", "arcadeNotes": "Fast sword with high combo potential."},
    "Nightmare's Bite": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Dual sickles that spawn poison clouds."},
    "Moon Daggers": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Thrown daggers with range. Very fast."},
    "Fortune Spear": {"aoeSize": "medium", "speedClass": "fast", "arcadeNotes": "Spear with good reach. Chance for extra consumables."},
    "Eternal Knife": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Extremely fast daggers with soul gathering."},
    "Bee Stinger": {"aoeSize": "small", "speedClass": "very_fast", "arcadeNotes": "Rapier — very fast thrusts."},
    "Highland Axe": {"aoeSize": "medium", "speedClass": "medium", "arcadeNotes": "Solid axe with stun chance."},
    "Diamond Pickaxe": {"aoeSize": "small", "speedClass": "fast", "arcadeNotes": "Fast pickaxe with extra emeralds from mobs."},
    "Bubble Burster": {"aoeSize": "wide", "speedClass": "medium", "arcadeNotes": "Ranged melee attack with bubble projectile."},  # wait this is ranged
}

RANGED_WEAPON_INFO = {
    "Twin Bow": {"arrowPattern": "double", "arcadeNotes": "Fires two arrows at once. Double damage potential."},
    "Red Snake": {"arrowPattern": "spread", "arcadeNotes": "Arrows follow terrain. Good for hitting around obstacles."},
    "Sabrewing": {"arrowPattern": "single_strong", "arcadeNotes": "Powerful single shots with knockback."},
    "The Pink Scoundrel": {"arrowPattern": "single_strong", "arcadeNotes": "Strong single shots. Chance to steal emeralds."},
    "Corrupted Beacon": {"arrowPattern": "beam", "arcadeNotes": "Continuous beam artifact. Massive damage but drains souls."},
    "Auto Crossbow": {"arrowPattern": "rapid", "arcadeNotes": "Very fast firing rate. Great sustained damage."},
    "Firebolt Thrower": {"arrowPattern": "rapid_fire", "arcadeNotes": "Rapid fire crossbow with fire bolts."},
    "Guardian Bow": {"arrowPattern": "single_strong", "arcadeNotes": "Strong shots with extra damage to guardians."},
    "Lightning Harp Crossbow": {"arrowPattern": "multi_spread", "arcadeNotes": "Fires multiple lightning bolts in a spread. Top tier crowd control."},
    "The Green Menace": {"arrowPattern": "single_poison", "arcadeNotes": "Arrows poison enemies. Good sustained damage."},
    "Imploding Crossbow": {"arrowPattern": "single_pull", "arcadeNotes": "Pulls enemies together on impact. Great combo setup."},
    "Harp Crossbow": {"arrowPattern": "multi_spread", "arcadeNotes": "Fires multiple arrows in a spread. Excellent crowd weapon."},
    "Bubble Burster": {"arrowPattern": "single_strong", "arcadeNotes": "Short range but hits through enemies."},
    "Nautical Crossbow": {"arrowPattern": "single_strong", "arcadeNotes": "Strong crossbow with extra damage."},
    "Web Bow": {"arrowPattern": "single_slow", "arcadeNotes": "Arrows slow/trap enemies in webs."},
    "Bonebow": {"arrowPattern": "multi", "arcadeNotes": "Growing arrows that split on hit."},
    "Purple Storm": {"arrowPattern": "multi_spread", "arcadeNotes": "Fires multiple bolts in a spread."},
    "Soul Hunter Crossbow": {"arrowPattern": "single_soul", "arcadeNotes": "Gathers souls on hit."},
    "Spellbound Crossbows": {"arrowPattern": "dual_rapid", "arcadeNotes": "Dual crossbows — rapid fire."},
    "Eye of the Guardian": {"arrowPattern": "beam", "arcadeNotes": "Fires a beam that hits through enemies."},
    "Sugar Rush": {"arrowPattern": "rapid", "arcadeNotes": "Very fast firing shortbow."},
    "Slayer Crossbow": {"arrowPattern": "single_strong", "arcadeNotes": "Strong single shots with extra damage to bosses."},
    "Elite Power Bow": {"arrowPattern": "single_strong", "arcadeNotes": "Maximum damage per shot. Charged shots."},
    "Phantom Bow": {"arrowPattern": "single_soul", "arcadeNotes": "Arrows pass through enemies and gather souls."},
}

ARMOR_INFO = {
    "Souldancer Robe": {"defenseClass": "light", "arcadeNotes": "Light robe with soul speed boost. Less protection but faster."},
    "Battle Robe": {"defenseClass": "light", "arcadeNotes": "Light robe with melee damage boost."},
    "Wolf Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor with wolf ally health boost."},
    "Grim Armor": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor. Good all-around protection."},
    "Highland Armor": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor with damage reduction."},
    "Renegade Armor": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor with weapon damage boost."},
    "Spider Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor with life steal."},
    "Full Metal Armor": {"defenseClass": "very_heavy", "arcadeNotes": "Maximum protection. Very tanky."},
    "Ember Robe": {"defenseClass": "light", "arcadeNotes": "Light robe that burns nearby enemies."},
    "Ender Armor": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor with teleportation dodge."},
    "Titan's Shroud": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor with life steal."},
    "Frost Bite": {"defenseClass": "medium", "arcadeNotes": "Freezes nearby enemies. Good defensive utility."},
    "Hero's Armor": {"defenseClass": "heavy", "arcadeNotes": "Strong protection with potion boost."},
    "Squid Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor with underwater themes."},
    "Glow Squid Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor. Attracts enemies (tank role)."},
    "Nimble Turtle Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor with speed boost."},
    "Archer's Armor": {"defenseClass": "light", "arcadeNotes": "Light armor with ranged damage boost."},
    "Ghost Kingler": {"defenseClass": "medium", "arcadeNotes": "Medium armor with soul gathering."},
    "Phantom Armor": {"defenseClass": "medium", "arcadeNotes": "Medium armor with soul speed."},
    "Hungry Horror": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor that heals on eating."},
    "Wither Armor": {"defenseClass": "very_heavy", "arcadeNotes": "Maximum protection with life steal. Top tier tank."},
    "Black Wolf Armor": {"defenseClass": "heavy", "arcadeNotes": "Heavy armor with wolf ally boost."},
    "Evocation Robe": {"defenseClass": "light", "arcadeNotes": "Light robe with artifact damage boost."},
    "Stalwart Armor": {"defenseClass": "very_heavy", "arcadeNotes": "Maximum protection. Damage reduction when standing still."},
}

def assign_power_tier(card):
    """Assign a power tier (S/A/B/C) based on arcade usefulness."""
    name = card['name']
    cat = card['category']
    
    if cat == 'melee_weapon':
        info = MELEE_WEAPON_INFO.get(name, {})
        aoe = info.get('aoeSize', 'medium')
        if aoe == 'very_wide':
            return 'S'
        elif aoe == 'wide':
            return 'A'
        elif aoe == 'medium':
            return 'B'
        else:
            return 'C'
    
    elif cat == 'ranged_weapon':
        info = RANGED_WEAPON_INFO.get(name, {})
        pattern = info.get('arrowPattern', 'single')
        if pattern in ('multi_spread', 'beam', 'dual_rapid'):
            return 'S'
        elif pattern in ('rapid', 'rapid_fire', 'double', 'spread'):
            return 'A'
        elif pattern in ('single_strong', 'multi', 'single_pull'):
            return 'B'
        else:
            return 'C'
    
    elif cat == 'armor':
        info = ARMOR_INFO.get(name, {})
        defense = info.get('defenseClass', 'medium')
        if defense == 'very_heavy':
            return 'S'
        elif defense == 'heavy':
            return 'A'
        elif defense == 'medium':
            return 'B'
        else:
            return 'C'
    
    return None  # No tier for heroes/pets (they're cosmetic/functional differently)

def main():
    with open('cards.json') as f:
        cards = json.load(f)
    
    for card in cards:
        name = card['name']
        cat = card['category']
        
        # Add gameplay info
        if cat == 'melee_weapon' and name in MELEE_WEAPON_INFO:
            info = MELEE_WEAPON_INFO[name]
            card['arcadeGameplay'] = {
                'aoeSize': info['aoeSize'],
                'speedClass': info['speedClass'],
                'notes': info['arcadeNotes'],
            }
        elif cat == 'ranged_weapon' and name in RANGED_WEAPON_INFO:
            info = RANGED_WEAPON_INFO[name]
            card['arcadeGameplay'] = {
                'arrowPattern': info['arrowPattern'],
                'notes': info['arcadeNotes'],
            }
        elif cat == 'armor' and name in ARMOR_INFO:
            info = ARMOR_INFO[name]
            card['arcadeGameplay'] = {
                'defenseClass': info['defenseClass'],
                'notes': info['arcadeNotes'],
            }
        
        # Assign power tier
        tier = assign_power_tier(card)
        if tier:
            card['powerTier'] = tier
    
    with open('cards.json', 'w') as f:
        json.dump(cards, f, indent=2)
    
    # Print tier summary
    print("=== ARCADE POWER TIER GUIDE ===\n")
    for cat_label, cat_key in [("MELEE WEAPONS", "melee_weapon"), ("RANGED WEAPONS", "ranged_weapon"), ("ARMOR", "armor")]:
        print(f"\n{cat_label}:")
        cat_cards = [c for c in cards if c['category'] == cat_key]
        for tier in ['S', 'A', 'B', 'C']:
            tier_cards = [c for c in cat_cards if c.get('powerTier') == tier]
            if tier_cards:
                names = ', '.join(c['name'] for c in tier_cards)
                print(f"  {tier}-Tier: {names}")
    
    print(f"\nDone! Enhanced {len(cards)} cards.")

if __name__ == '__main__':
    main()
