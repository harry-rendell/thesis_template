# PhD thesis template for Astrophysics, University of Edinburgh

### Set up thesis overleaf project
1. Download this repository
    (do not clone or fork as it would prevent you from setting it up as your own git repo later)
2. Create a new project in Overleaf and upload the zipped folder
3. Add your text to the .tex files in each chapter
    (Note: abstract, acknowledgements, and lay summary can be found in `thesis-frontmatter`)
3. Add your figures to the `graphics` folders in each chapter
4. Add your references to the `main.bib` file

### Connect the overleaf project to git
**1. Get [https://www.overleaf.com/edu/edinburgh](Overleaf Premium) if you do not already have it**
* it's free as an Edinburgh student!
* 
**2. Make a git repository**
* Click on overleaf menu -> click on Git to get the git clone command
* Navigate to where you generate plots (ie. cuillin or your local machine)
* type git clone command 
    i.e. `git clone https://git.overleaf.com/123abc123abc123abc`
* this will create a git repository in your working directory
* if you want to clone the repo in a subfolder then add the folder name to the end of the command
    i.e. `git clone https://git.overleaf.com/123abc123abc123abc thesis`
* for more information on Overleaf Git integration: https://www.overleaf.com/learn/how-to/Git_integration

\
By making your Overleaf project a Git repository, you can have it as a folder alongside your code 
which enables you to output plots DIRECTLY to the Overleaf git folder, which can be 
commited and pushed directly to Overleaf, even if you are creating plots on a cluster such as cuillin!
No more dragging and dropping plots into Overleaf...


## Optional Neat Tips!

### Faster compiling and better plot management
**Make png versions of plot pdfs**
* An Overleaf project with many pdfs can become very unweidly and slow to compile.
* A solution to this is to have png copies of all pdfs and place them in a draft_graphics
which goes alongside the graphics folder. 
* For this, it is advised to have a custom figure saving script which outputs the png and pdf plots. I have provided one in this repo: `scripts/save_figure.py`
* Put this script alongside your code and import it via: 'from save_figure import savefigs'


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

### Latex Customisations
You can make customisations to make shortcuts for long latex commands. The example [https://github.com/harry-rendell/thesis_template/blob/626066b9c4d6a1a6ea0f66d23c9cc83c158a5a39/customisations.sty#L10](here) allows you to make colorful notes to yourself as you work on the text.
