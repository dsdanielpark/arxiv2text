Development Status :: 3 - Alpha

# arxiv2text

<p align="left">
<a href="https://github.com/dsdanielpark/Bard-API"><img alt="PyPI package" src="https://img.shields.io/badge/pypi-arXiv2text-black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2Farxiv2text&count_bg=%23000000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
<a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-orange.png" height="20px"></a>
</p>

A Python package that converts arXiv documents into structured text using arXiv PDF URLs.

<br>

## Install
```
$ pip install arxiv2text
```
```
$ pip install git+https://github.com/dsdanielpark/arxiv2text.git
```

<br>

## Usage 
We use the PDF link as input, not the arXiv abs link. The functionality is incomplete due to the diversity of PDF structures.
Example paper: Attention Is All You Need
- PDF URL: https://arxiv.org/pdf/1706.03762
- Abstract URL: https://arxiv.org/abs/1706.03762

<br>

*arxiv_to_text*

```python
from arxiv2text import arxiv_to_text

pdf_url = "https://arxiv.org/pdf/1706.03762"

extracted_text = arxiv_to_text(pdf_url)
```

*arxiv_to_html*

```python
from arxiv2text import arxiv_to_html

pdf_url = "https://arxiv.org/pdf/1706.03762"

output_dir = "output_folder"
arxiv_to_html(pdf_url, output_dir)
```

*arxiv_to_md*
```python
from arxiv2text import arxiv_to_md

pdf_url = "https://arxiv.org/pdf/1706.03762"

output_dir = "output_folder"
arxiv_to_md(pdf_url, output_dir)
```



<br>

## License
[MIT](https://opensource.org/license/mit/) <br>
```
The MIT License (MIT)

Copyright (c) 2023 Minwoo Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
- Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>

  
*Copyright (c) 2023 MinWoo Park, South Korea*<br>
