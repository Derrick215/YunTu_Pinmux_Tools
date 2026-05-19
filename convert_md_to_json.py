#!/usr/bin/env python3
"""
Convert YTM32 PINMUX markdown files to a single JS data file.
Reads all .md files from YTM32_PINMUX_MD_Files/ and outputs pinmux_data.js
Usage: python convert_md_to_json.py
"""

import os
import re
import json
from pathlib import Path

MD_DIR = Path(__file__).parent.parent / "YTM32_PINMUX_MD_Files"
OUTPUT_FILE = Path(__file__).parent / "pinmux_data.js"


def classify_pin_type(name):
    """Classify pin type based on its name."""
    if not name:
        return "UNKNOWN"
    name_upper = name.strip()
    # Power
    if re.match(r'^(VDD\d*|VDDA|VREF[HRL]|VDD\d+)$', name_upper):
        return "POWER"
    # Ground
    if re.match(r'^(VSS\d*|VSSA|VREFL)$', name_upper):
        return "GND"
    # Clock / XTAL
    if re.match(r'^(EXTAL\d*|XTAL\d*)$', name_upper, re.IGNORECASE):
        return "CLOCK"
    # Debug / JTAG / Reset
    if re.match(r'^(JTAG_|RCU_RESET|SWD_|SWO)', name_upper, re.IGNORECASE):
        return "DEBUG"
    # GPIO (starts with PT)
    if re.match(r'^PT[A-Z]_', name_upper):
        return "GPIO"
    return "OTHER"


def parse_md_file(filepath):
    """Parse a single PINMUX markdown file and return chip data dict."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract chip name and version from the title line
    title_match = re.match(r'^#\s+(\S+)_PINMUX_V(\S+)', content)
    if not title_match:
        return None

    chip_name = title_match.group(1)
    version = title_match.group(2)

    # Find the IOMUX or PINMUX section
    section_match = re.search(r'##\s+(IOMUX|PINMUX)\s*\n', content)
    if not section_match:
        return None

    # Find the table: from the section header, find the next pipe-delimited lines
    section_start = section_match.end()
    lines = content[section_start:].strip().split('\n')

    # Locate table header and separator
    header_line = None
    separator_line = None
    data_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('|') and '---' in stripped:
            if header_line is None:
                # This is the separator; the previous line was the header
                header_line = lines[i - 1].strip()
                separator_line = stripped
                data_start = i + 1
            break
        elif stripped.startswith('|') and header_line is None and '---' not in stripped:
            # Some files might have header without --- separator? Unlikely but handle
            pass

    if header_line is None:
        return None

    # Parse header columns
    header_cells = [c.strip() for c in header_line.split('|')]
    header_cells = [c for c in header_cells if c]  # Remove empty from leading/trailing pipes

    # Classify each column
    alt_indices = []
    package_cols = {}  # {index: package_name}
    name_idx = None
    drive_idx = None
    wku_idx = None
    default_func_idx = None
    default_state_idx = None
    note_idx = None
    hd_idx = None

    for idx, cell in enumerate(header_cells):
        cell_upper = cell.upper()
        if re.match(r'^ALT\d+$', cell):
            alt_indices.append(idx)
        elif re.search(r'(LQFP|QFN|BGA|WLCSP)', cell_upper):
            package_cols[idx] = cell
        elif cell_upper == 'NAME':
            name_idx = idx
        elif 'DRIVE' in cell_upper:
            drive_idx = idx
        elif cell_upper == 'WKU':
            wku_idx = idx
        elif cell_upper == 'DEFAULT FUNCTION':
            default_func_idx = idx
        elif cell_upper == 'DEFAULT STATE':
            default_state_idx = idx
        elif cell_upper == 'NOTE':
            note_idx = idx
        elif cell_upper == 'HD':
            hd_idx = idx

    # Parse data rows
    pins = []
    for line in lines[data_start:]:
        stripped = line.strip()
        if not stripped.startswith('|'):
            break  # End of table

        cells = [c.strip() for c in stripped.split('|')]
        cells = [c for c in cells if c or cells.index(c) == 0]  # Preserve empty cells

        # Rebuild cells list properly: first and last pipe create empty strings
        raw_cells = stripped.split('|')
        # Remove first and last empty if the line starts/ends with pipe
        if raw_cells and raw_cells[0] == '':
            raw_cells = raw_cells[1:]
        if raw_cells and raw_cells[-1] == '':
            raw_cells = raw_cells[:-1]
        cells = [c.strip() for c in raw_cells]

        if name_idx is None or name_idx >= len(cells):
            continue

        pin_name = cells[name_idx].strip()
        if not pin_name:
            continue

        # Collect ALT functions (excluding empty strings)
        alt_functions = []
        for ai in alt_indices:
            if ai < len(cells) and cells[ai].strip():
                alt_func = cells[ai].strip()
                # Remove "WKU[n]" or "WKU[n]" annotation from function names
                alt_func = re.sub(r'\s*WKU\[\d+\]\s*', '', alt_func).strip()
                if alt_func and alt_func not in alt_functions:
                    alt_functions.append(alt_func)

        # Collect package pin numbers
        package_pins = {}
        for pi, pkg_name in package_cols.items():
            if pi < len(cells) and cells[pi].strip():
                try:
                    package_pins[pkg_name] = int(cells[pi].strip())
                except ValueError:
                    package_pins[pkg_name] = cells[pi].strip()

        # Determine pin type
        pin_type = classify_pin_type(pin_name)

        # Drive strength
        drive = None
        if drive_idx is not None and drive_idx < len(cells):
            drive = cells[drive_idx].strip() or None
        if drive is None and hd_idx is not None and hd_idx < len(cells):
            hd_val = cells[hd_idx].strip().upper()
            if hd_val == 'HD':
                drive = 'HD'
            elif hd_val:
                drive = 'NORMAL'

        # WKU
        wku = None
        if wku_idx is not None and wku_idx < len(cells):
            wku_val = cells[wku_idx].strip()
            if wku_val:
                wku = wku_val

        # Default state
        default_state = None
        if default_state_idx is not None and default_state_idx < len(cells):
            default_state = cells[default_state_idx].strip() or None

        # Default function (if separate column exists)
        if default_func_idx is not None and default_func_idx < len(cells):
            df = cells[default_func_idx].strip()
            if df and df not in alt_functions:
                alt_functions.insert(0, df)

        pin_obj = {
            "name": pin_name,
            "type": pin_type,
            "packagePins": package_pins,
            "altFunctions": alt_functions,
        }

        if drive:
            pin_obj["drive"] = drive
        if wku:
            pin_obj["wku"] = wku
        if default_state:
            pin_obj["defaultState"] = default_state

        pins.append(pin_obj)

    # Collect package names across all pins (some pins may not have all packages)
    all_packages = set()
    for p in pins:
        all_packages.update(p["packagePins"].keys())

    # Sort packages by name (larger pin count first)
    sorted_packages = sorted(all_packages, key=lambda x: (
        -max(p["packagePins"].get(x, 0) for p in pins if x in p["packagePins"])
    ))

    return {
        "version": version,
        "packages": sorted_packages,
        "pins": pins,
    }


def main():
    md_files = sorted(MD_DIR.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {MD_DIR}")
        return

    chips = {}
    for filepath in md_files:
        print(f"Parsing: {filepath.name} ... ", end="")
        data = parse_md_file(filepath)
        if data:
            chips[data["version"]] = data
            chips[filepath.stem.split('_')[0]] = data  # Use full name as key
            print(f"OK ({len(data['pins'])} pins, {len(data['packages'])} packages)")
        else:
            print("FAILED")

    # Re-key by chip name from filename
    chips_by_name = {}
    for filepath in md_files:
        stem = filepath.stem  # e.g., YTM32B1HA0x_PINMUX_V1.1
        chip_name = stem.split('_')[0]  # e.g., YTM32B1HA0x
        data = parse_md_file(filepath)
        if data:
            # Store chip name in the data
            data["name"] = chip_name
            chips_by_name[chip_name] = data
            print(f"  {chip_name}: {len(data['pins'])} pins, packages: {data['packages']}")

    # Write JS output
    json_str = json.dumps(chips_by_name, indent=2, ensure_ascii=False)
    js_content = f"// Auto-generated from YTM32_PINMUX_MD_Files/*.md\n// Generated by convert_md_to_json.py\nconst PINMUX_DATA = {json_str};\n"

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\nOutput written to: {OUTPUT_FILE}")
    print(f"Total chips: {len(chips_by_name)}")


if __name__ == "__main__":
    main()
