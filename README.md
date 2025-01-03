Dick Smith System 80 Restoration
================================

This repository chronicles my exploits in restoring a Dick Smith System 80
that I got off eBay.

## Technical specifications

* Z-80 8-bit CPU, running at 1.79MHz.
* 12K of ROM containing BASIC.
* 1K of video RAM for 64 x 16 text mode or 128 x 48 graphics mode.
* 16K of user program RAM, expandable to 48K using the expansion connector.

### Initial condition of the unit

TBD

### Conclusion

Here is a summary of the changes that I made:

* TBD

Costings:

* AUD$500 for the System 80 off eBay, plus AUD$60 shipping.
* TBD

And here it is in all of its restored glory:

TBD

## Schematics

I have reproduced some of the schematics from the Technical Manual in KiCad
and generated PDF versions.  The original schematics can be hard to read.

* [System 80 Main Board](schematics/System_80_Main_Board/PDF/System_80_Main_Board.pdf)

## Adapting the schematic

In theory the KiCad schematics could be modernised and then laid out on
brand new PCB's.  But a lot of work would be required to add footprints
and lay everything out.

The components in the System 80 are all bog-standard Z-80, memory, and
TTL logic chips.  Making a new System 80 from scratch wouldn't be
impossible.  But some things would be easier with modern components:

* Use a single 16K EEPROM instead of separate 4K EPROM's.
* Use static RAM chips like the 32K 62256 for system memory, instead of
dynamic RAM.  This removes a lot of complexity in the memory interface.
* Replace the 5-pin monitor connector with a standard composite video RCA jack.

## Resources

* TBD

## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">System 80 Restoration</span> by <span property="cc:attributionName">Rhys Weatherley</span> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

## Contact

For more information on this project, to report bugs, or to suggest
improvements, please contact the author Rhys Weatherley via
[email](mailto:rhys.weatherley@gmail.com).
