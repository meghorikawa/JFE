# a function to help dynamically load all rules for the matching

import os
import importlib

rule_modules = {}
rule_dir = os.path.dirname(__file__)

for filename in os.listdir(rule_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"rules.{filename[:-3]}"
        module = importlib.import_module(module_name)
        rule_modules[module_name] = module
