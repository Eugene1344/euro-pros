# Euro Pros

Static frontend prototype prepared for a later WordPress/ACF integration.

## Structure

- `components/<name>/<name>.html` — homepage component markup.
- `components/<name>/<name>.css` — styles owned by that component.
- `components/<name>/<name>.js` — optional component behavior.
- `css/variables.css` and `css/main.css` — shared tokens and page-agnostic styles.
- `build_index.py` — assembles the homepage from the component folders.
- `gen_site.py` and `build_pages.py` — generate the current interior-page prototypes.

Keep new homepage sections self-contained in `components/`. This maps cleanly to
WordPress template parts or ACF flexible-content blocks and avoids growing a
single global stylesheet.

## Rebuild

```sh
python3 build_index.py
```

Run the command after changing homepage component markup or after adding or
removing a component asset.
