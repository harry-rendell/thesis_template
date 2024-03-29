# PhD thesis template for Astrophysics, University of Edinburgh

## How to use this template
1. Download this repository (do not clone or fork as it would prevent you from setting it up as your own git repo later)
2. Create new project in Overleaf and upload the folder (may need to be zipped first)
3. Add figures to the `graphics` folders and all references to `main.bib`
4. Optional: read the section below for some neat tips!

## Faster compiling and better plot management
**The following is optional but may be useful to those with many plots in their thesis.**

* An Overleaf project with many pdfs can become very unweidly and slow to compile.
* A solution to this is to have png copies of all pdfs and place them in a draft_graphics
which goes alongside the graphics folder. 
* For this, it is advised to have a custom figure saving script which outputs the png and pdf plots. I have provided one in this repo: `scripts/save_figure.py`
* Put this script alongside your code and import it via: 'from save_figure import savefigs'

This method is most efficient if you combine it with git for Overleaf. This is a premium feature, but Overleaf Premium is free as an Edinburgh student!
* Overleaf Premium: https://www.overleaf.com/edu/edinburgh
* Overleaf Git integration: https://www.overleaf.com/learn/how-to/Git_integration

\
By making your Overleaf project a Git repository, you can have it as a folder alongside your code 
which enables you to output plots DIRECTLY to the Overleaf git folder, which can be 
commited and pushed directly to Overleaf, even if you are creating plots on a cluster such as cuillin!
No more dragging and dropping plots into Overleaf...

Here is an example of my folder structure:
```
path/to/project
│
├── mycode
│   ├── save_figure.py
│   └── some_analysis_code.py
│
└── thesis_template
    ├── chap1_intro
    │   ├── draft_graphics
    │   │   └── plot.png
    │   ├── graphics
    │   │   └── plot.pdf
    │   └── intro.tex
    ├── chap2
    │   ├── chap2.tex
    │   ├── draft_graphics
    │   └── graphics
    ├── chap3
    │   ├── chap3.tex
    │   ├── draft_graphics
    │   └── graphics
    ├── chap4
    │   ├── chap4.tex
    │   ├── draft_graphics
    │   └── graphics
    ├── chap5_conclusion
    │   ├── conclusion.tex
    │   ├── draft_graphics
    │   └── graphics
    ├── customisations.sty
    ├── main.bib
    ├── main.tex
    ├── mnras.bst
    ├── scripts
    │   └── generate_graphics_paths.py
    └── thesis-frontmatter
        ├── abstract.tex
        ├── acknowledgements.tex
        ├── crest.pdf
        └── lay_summary.tex
```

`some_analysis_code.py` is whatever code I would use to generate plots,
and `save_figure.py` is the custom plotting function found in the `scripts` folder
(I recommended you move it to your code folder for easier importing).
In this example, `path/to/project/thesis_template` is the path you would use for the 
`thesis_dir` argument in the `savefigs` function.

Note that this template does not include `draft_graphics` folders by default,
however, `savefigs` will generate these automatically as needed.

### Nested directories and updating the graphics path (even more optional)
If you decide to organise your plots into subdirectories inside `draft_graphics/graphics`, you will need to add these directories to the graphics path.
Run `scripts/generate_graphics_path.py` from the `thesis_template folder`, (eg `python scripts/generate_graphics_path.py`) to generate a new latex graphics path and copy & paste it over the previous one in `customisations.sty`.
