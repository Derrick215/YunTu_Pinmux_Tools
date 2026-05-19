"""Validate pinmux data for JS safety and parsePeriph coverage."""
import json, re

with open('pinmux_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content.split('const PINMUX_DATA = ')[1].rstrip(';\n')
data = json.loads(json_str)

# Same logic as parsePeriph in HTML
def parsePeriph(funcName):
    if not funcName: return None
    m = None
    if (m := re.match(r'^SPI(\d+)_(.+)$', funcName)): return ('SPI', int(m.group(1)), m.group(2))
    if (m := re.match(r'^CAN(\d+)_(TX|RX)$', funcName)): return ('CAN', int(m.group(1)), m.group(2))
    if (m := re.match(r'^LINFlexD(\d+)_(TX|RX)$', funcName)): return ('UART', int(m.group(1)), m.group(2))
    if (m := re.match(r'^UART(\d+)_(TX|RX|RTS|CTS)$', funcName)): return ('UART', int(m.group(1)), m.group(2))
    if (m := re.match(r'^eTMR(\d+)_(.+)$', funcName)): return ('eTMR', int(m.group(1)), m.group(2))
    if (m := re.match(r'^I2C(\d+)_(SCL|SDA)$', funcName)): return ('I2C', int(m.group(1)), m.group(2))
    if (m := re.match(r'^MPWM(\d+)_(.+)$', funcName)): return ('MPWM', int(m.group(1)), m.group(2))
    if (m := re.match(r'^QSPI_(.+)$', funcName)): return ('QSPI', 0, m.group(1))
    if (m := re.match(r'^ENET_(.+)$', funcName)): return ('ENET', 0, m.group(1))
    if (m := re.match(r'^SAI(\d+)_(.+)$', funcName)): return ('SAI', int(m.group(1)), m.group(2))
    if (m := re.match(r'^TMU_(.+)$', funcName)): return ('TMU', 0, m.group(1))
    if (m := re.match(r'^ADC(\d+)_SE(\d+)', funcName)): return ('ADC', int(m.group(1)), 'SE'+m.group(2))
    if (m := re.match(r'^ADC(\d+)_S(\d+)', funcName)): return ('ADC', int(m.group(1)), 'S'+m.group(2))
    if (m := re.match(r'^DAC(\d+)_OUT', funcName)): return ('DAC', int(m.group(1)), 'OUT')
    if (m := re.match(r'^ACMP(\d+)_(.+)', funcName)): return ('ACMP', int(m.group(1)), m.group(2))
    if (m := re.match(r'^ACMP_(.+)', funcName)): return ('ACMP', 0, m.group(1))
    if (m := re.match(r'^ETM_(.+)$', funcName)): return ('ETM', 0, m.group(1))
    if (m := re.match(r'^SENT(\d+)_(.+)$', funcName)): return ('SENT', int(m.group(1)), m.group(2))
    if (m := re.match(r'^SENT_(.+)$', funcName)): return ('SENT', 0, m.group(1))
    if (m := re.match(r'^FMU_(.+)$', funcName)): return ('FMU', 0, m.group(1))
    if (m := re.match(r'^(SCU_CLKOUT|CLKOUT_RUN|CLKOUT_STANDBY|RTC_CLKOUT|CFMU_CLKOUT|CLKOUT)$', funcName)): return ('CLKOUT', 0, m.group(1))
    if (m := re.match(r'^RTC_CLKIN$', funcName)): return ('CLKOUT', 0, 'RTC_CLKIN')
    if (m := re.match(r'^[Ll]PTMR(\d+)_ALT(\d+)$', funcName)): return ('LPTMR', int(m.group(1)), 'ALT'+m.group(2))
    if (m := re.match(r'^TCLK_(.+)$', funcName)): return ('TCLK', 0, m.group(1))
    if (m := re.match(r'^(JTAG_.*|SWD_.*|SWO)$', funcName)): return ('JTAG', 0, m.group(1))
    if (m := re.match(r'^SWD_(.+)$', funcName)): return ('JTAG', 0, m.group(1))
    return None

# Collect unique functions
all_funcs = sorted(set(f for chip in data.values() for p in chip['pins'] for f in p.get('altFunctions',[])))

# Filter out pin names, power/gnd/clock/debug/reset/NMI
skip = re.compile(r'^(PT[A-Z]_\d+|VDD|VSS|VDDA|VSSA|VREF[HRL]|XTAL|EXTAL|RCU_RESET|CORE_NMI|EWDG|NMI_b|CM33_NMI_b|RESET_b)$')

unmatched = []
groups = {}
for f in sorted(all_funcs):
    if skip.match(f):
        continue
    g = parsePeriph(f)
    if g:
        groups[g[0]] = groups.get(g[0], 0) + 1
    else:
        unmatched.append(f)

if unmatched:
    print(f"Unmatched ({len(unmatched)}):")
    for f in unmatched:
        print(f"  {f}")
else:
    print("ALL functions matched!")

print(f"\nCoverage ({sum(groups.values())} functions):")
for g in sorted(groups.keys()):
    print(f"  {g}: {groups[g]}")
