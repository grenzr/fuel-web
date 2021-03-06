# Add any Sphinx extension module names here, as strings.
# They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions += ['sphinx.ext.inheritance_diagram', 'sphinxcontrib.blockdiag',
               'sphinxcontrib.actdiag', 'sphinxcontrib.seqdiag',
               'sphinxcontrib.nwdiag']

# The encoding of source files.
source_encoding = 'utf-8-sig'
#source_encoding = 'shift_jis'

# The language for content autogenerated by Sphinx.
language = 'en'
#language = 'ja'

# The theme to use for HTML and HTML Help pages.
#html_theme = 'default'
#html_theme = 'sphinxdoc'
#html_theme = 'scrolls'
#html_theme = 'agogo'
#html_theme = 'traditional'
#html_theme = 'nature'
#html_theme = 'haiku'

# If this is not the empty string, a 'Last updated on:' timestamp
# is inserted at every page bottom, using the given strftime() format.
# Default is '%b %d, %Y' (or a locale-dependent equivalent).
html_last_updated_fmt = '%Y/%m/%d'

# Enable Antialiasing
blockdiag_antialias = True
acttdiag_antialias = True
seqdiag_antialias = True
nwdiag_antialias = True

extensions += ['rst2pdf.pdfbuilder']
pdf_documents = [
    (master_doc, project, project, copyright),
]
pdf_stylesheets = ['sphinx', 'kerning', 'a4', 'en']
pdf_language = "en"
# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
#pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
pdf_use_toc = True

# How many levels deep should the table of contents be?
pdf_toc_depth = 2

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'
