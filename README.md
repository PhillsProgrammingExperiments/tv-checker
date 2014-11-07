tv-checker
================

Simple python script for checking whether you favourite TV series has any new episodes.

This script has 2 modes:

* Checking followed series for new episodes (tv_checker.py check ...)
* Adding new series to followed (tv_checker.py add ...)

Use flag -h/--help to see full usage.

Script assumes you use it properly. It's UI is really simple, so there are no real error handlers - if something goes wrong, you'll
see fugly stacktrace, but I think you'll figure it out.

"New" episode means "episode that isn't one that is saved in config". I wrote this, because I couldn't really remember when do new 
episodes come out, so instead of checking manually I automatized it. It won't be really useful, when you want to watch some series 
from the very beginning.

Frankly, this should be GIST, not full-blown repo, but I wanted to provide example configuration (tv_config.json) too.

This is too simple to provide real setup.py. Here are its dependencies (exact version I used are shown too, but it will work with most
versions of those packages):

* requests (2.4.3)
* bs4 (4.3.2)
* docopt (0.6.2)

Whole tool is licensed as MIT-ish beerware.

