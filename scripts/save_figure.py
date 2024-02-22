# Originally created by Rokas Žemaitis and developed by Harry Rendell-Bhatti

import os

def savefigs(fig, imgname, chap_dir, thesis_dir, dpi=100, noaxis=False, **kwargs):
    """
    Save a low-res png and high-res pdf for fast compiling of thesis.
    Subdirectories (except for chapter folders) are created if they don't already exist.

    Example use 1: savefigs(fig, 'venn_diagram', 'chap2', 'home/username/thesis_template')
        Creates the following files: chap2/graphics/venn_diagram.pdf
                                     chap2/draft_graphics/venn_diagram.png

    Example use 2: savefigs(fig, 'section3/venn_diagram', 'chap2', 'home/username/thesis_template')
        Creates the following files: chap2/graphics/survey/venn_diagram.pdf
                                     chap2/draft_graphics/survey/venn_diagram.png

    Parameters
    ----------
    fig : matplotlib figure handle
    imgname : str
        name for plot without extension. Prefix with a folder to create a subdirectory.
    chap_dir : str
        Relative path from thesis_dir to chapter folder, eg 'chap2' or 'chap2/section3'
        Creates directories if output path does not exist.
    thesis_dir : str
        Absolute path to thesis directory, eg '/home/username/thesis_template'.
    dpi : int
        Resolution for png file.
    """
    
    # Remove extension if user has accidentally provided one
    imgname = imgname.replace('.png', '').replace('.pdf', '')

    chap_dir = os.path.join(thesis_dir, chap_dir)

    # Check that the chapter folder exists
    assert os.path.exists(chap_dir), f"Path {chap_dir} does not exist"

    pdf_path = os.path.join(chap_dir, 'graphics')
    png_path = os.path.join(chap_dir, 'draft_graphics')
    
    if noaxis:
        #https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image - Richard Yu Liu
        fig.subplots_adjust(0,0,1,1,0,0)
        for ax in fig.axes:
            ax.axis('off')
        kwargs['pad_inches'] = 0

    kwargs['bbox_inches'] = 'tight'
    if "/" in imgname:
        # create subdirectories if they don't exist
        os.makedirs(os.path.join(png_path, os.path.dirname(imgname)), exist_ok=True)
        os.makedirs(os.path.join(pdf_path, os.path.dirname(imgname)), exist_ok=True)

    fig.savefig(os.path.join(pdf_path,imgname)+'.pdf', **kwargs)
    fig.savefig(os.path.join(png_path,imgname)+'.png', dpi=dpi, **kwargs)
