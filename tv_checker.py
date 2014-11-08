#!/bin/env python3

import sys
from bs4 import BeautifulSoup
import requests
import json
from docopt import docopt

USAGE = """Addic7ed TV series subtitles checker

Usage:
  tv_checker.py check [--config=<config>] [--no-update]
  tv_checker.py add --name=<name> --base=<base> [--config <config>]

Options:
  --config <config>             Config file in JSON format. Contained object should have attributes named as 
                                    followed TV series. Their values should be objects with attribute "base_address", 
                                    which is URL of episodes list and air dates on Addic7ed, and "last_path" with
                                    URL path of last episode watched by you (for example, if you watched episode with 
                                    subtitles that can be found at "http://addic7ed.com/blah/bla/bluh", this should 
                                    be "/blah/bla/bluh") [default: ./tv_config.json]
  -n, --no-update               Use this flag if you only want to check whether there are any new episodes, and not 
                                    download subtitles and watch those episodes now. Without this flag this script will 
                                    assume that just after running it, you'll watch episodes that it found as new.
  --name=<name>                 Name of TV series that you want to start to follow. Technically, it doesn't really
                                    matter, it is used only while notifying you.
  --base=<base>                 Base URL of added series. See --config explanation for details.
  -h, --help                    Show this.
  -v, --version                 Show version of this script. WARNING: That will not be very helpful."""
  
VERSION = "one and only"

def last_link(base_address):
    response = requests.get(base_address)
    assert response.status_code
    content = response.text
    soup = BeautifulSoup(content)
    episode_links = soup.find_all("tr", "hoverme")
    return episode_links[-1].find_all("td")[-1].a["href"]

def notify(name, path):
    print('New subtitles for "'+name+'" found:')
    print("\thttp://addic7ed.com"+path)

def check(update_config, config):
    for name in sorted(config.keys()):
        descriptor = config[name]
        
        last = last_link(descriptor["base_address"])
        
        if not last==descriptor["last_path"]:
            notify(name, last)
            if update_config:
                descriptor["last_path"] = last

def add(name, base, config):
    config[name] = {
            "base_address": base,
            "last_path": last_link(base)
        }

def main(args):
    parsed = docopt(USAGE, args, True, VERSION)
    
    with open(parsed["--config"], "r") as f:
        config = json.load(f)
    
    if parsed["check"]:
        check(not parsed["--no-update"], config)
        if not parsed["--no-update"]:
            with open(parsed["--config"], "w") as f:
                json.dump(config, f, indent=4, sort_keys=True)
    elif parsed["add"]:
        add(parsed["--name"], parsed["--base"], config)
        with open(parsed["--config"], "w") as f:
            json.dump(config, f, indent=4, sort_keys=True)
        
if __name__=="__main__":
    main(sys.argv[1:])