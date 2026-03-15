#!/usr/bin/env python3
"""
Scrape Minecraft Dungeons item stats from the wiki and build cards JSON.
Uses the MediaWiki API to avoid Cloudflare blocks.
"""
import json
import csv
import re
import time
import urllib.request
import urllib.parse

WIKI_API = "https://minecraft.wiki/api.php"

# Card categories based on barcode prefix analysis from the repo
# First char after 'a'/'b'/'c'/'d' indicates type:
# 0 = melee weapon, 1 = ranged weapon, 2 = armor, 3 = hero/skin, 4 = pet/companion
# The letter prefix (a/b/c/d) indicates the series

def determine_category(card_name, barcode, card_number):
    """Determine card category from barcode pattern and card number."""
    if len(barcode) < 2:
        return "unknown"
    
    series_char = barcode[0]  # a, b, c, d
    type_char = barcode[1]    # 0-4
    
    series_map = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    series = series_map.get(series_char, 'unknown')
    
    type_map = {
        '0': 'melee_weapon',
        '1': 'ranged_weapon',
        '2': 'armor',
        '3': 'hero',
        '4': 'pet',
    }
    category = type_map.get(type_char, 'unknown')
    
    return category, series

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
        print(f"  Error fetching {title}: {e}")
    return None

def parse_weapon_stats(wikitext):
    """Extract stats from weapon wiki page wikitext."""
    stats = {}
    
    if not wikitext:
        return stats
    
    # Look for infobox templates
    # Common fields: damage, speed, area, type
    text = wikitext
    
    # Try to find damage values
    damage_match = re.search(r'\|\s*damage\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if damage_match:
        stats['damage'] = damage_match.group(1).strip()
    
    # Speed
    speed_match = re.search(r'\|\s*speed\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if speed_match:
        stats['speed'] = speed_match.group(1).strip()
    
    # Area
    area_match = re.search(r'\|\s*area\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if area_match:
        stats['area'] = area_match.group(1).strip()
    
    # Type/class
    type_match = re.search(r'\|\s*type\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if type_match:
        stats['weaponType'] = type_match.group(1).strip()
    
    # Rarity
    rarity_match = re.search(r'\|\s*rarity\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if rarity_match:
        stats['rarity'] = rarity_match.group(1).strip()
    
    # Description
    desc_match = re.search(r'\|\s*description\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if desc_match:
        stats['description'] = desc_match.group(1).strip()
    
    # Special ability / unique effect
    ability_match = re.search(r'\|\s*ability\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if ability_match:
        stats['ability'] = ability_match.group(1).strip()
    
    # Power
    power_match = re.search(r'\|\s*power\s*=\s*(.+?)[\n|]', text, re.IGNORECASE)
    if power_match:
        stats['power'] = power_match.group(1).strip()
    
    # Unique (bool)
    if re.search(r'unique', text[:500], re.IGNORECASE):
        stats['isUnique'] = True
    
    return stats

def get_wiki_title(card_name, category):
    """Map card name to wiki page title."""
    # Clean up the name
    name = card_name.strip()
    
    # Remove "(Hero)" suffix for hero cards
    if '(Hero)' in name:
        name = name.replace('(Hero)', '').strip()
    
    # Skip pets and heroes that don't have weapon/armor pages
    if category in ('pet', 'hero'):
        return None
    
    # Wiki format: Dungeons:Item_Name
    wiki_name = name.replace(' ', '_').replace("'", "%27")
    return f"Dungeons:{wiki_name}"

def main():
    cards = []
    
    # Read the CSV
    with open('card_info.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            card_num = int(row['Card Number'])
            card_name = row['Card Name']
            barcode = row['Barcode Data']
            
            category, series = determine_category(card_name, barcode, card_num)
            
            card = {
                'cardNumber': card_num,
                'name': card_name,
                'barcodeData': barcode,
                'category': category,
                'series': series,
            }
            
            # Try to get wiki stats for weapons and armor
            wiki_title = get_wiki_title(card_name, category)
            if wiki_title:
                print(f"Fetching #{card_num}: {card_name} -> {wiki_title}")
                wikitext = get_wiki_page(wiki_title)
                if wikitext:
                    stats = parse_weapon_stats(wikitext)
                    if stats:
                        card['consoleStats'] = stats
                        print(f"  Found stats: {list(stats.keys())}")
                    else:
                        print(f"  No stats parsed")
                else:
                    # Try alternate title formats
                    alt_title = f"Dungeons:{card_name.replace(' ', '_')}"
                    print(f"  Trying alternate: {alt_title}")
                    wikitext = get_wiki_page(alt_title)
                    if wikitext:
                        stats = parse_weapon_stats(wikitext)
                        if stats:
                            card['consoleStats'] = stats
                            print(f"  Found stats: {list(stats.keys())}")
                
                time.sleep(0.3)  # Rate limit
            else:
                print(f"Skipping #{card_num}: {card_name} ({category})")
            
            cards.append(card)
    
    # Write JSON
    with open('cards.json', 'w') as f:
        json.dump(cards, f, indent=2)
    
    print(f"\nDone! {len(cards)} cards written to cards.json")
    
    # Stats summary
    with_stats = sum(1 for c in cards if 'consoleStats' in c)
    print(f"Cards with console stats: {with_stats}/{len(cards)}")

if __name__ == '__main__':
    main()
