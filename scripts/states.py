# Helper mappings to the directory name for each state.

import tomlkit
import os

by_postal_code = {}
by_fips = {}

for fn in os.listdir("states/"):
    info_fn = os.path.join("states", fn, "info.toml")
    if not os.path.exists(info_fn):
        continue
    with open(info_fn, "r") as f:
        state_info = tomlkit.loads(f.read())
    if "fips_code" in state_info:
        by_fips[state_info["fips_code"]] = fn
    if "postal_code" in state_info:
        by_postal_code[state_info["postal_code"]] = fn
