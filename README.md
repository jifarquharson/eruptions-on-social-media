# Eruptions in the Attention Economy  
**Tracking volcanic eruptions and public engagement through multilingual social media analysis**

## Overview  
This repository contains the code and data used in the research project *"Eruptions in the Attention Economy"*, which investigates how volcanic eruptions are perceived and discussed on social media across different languages. The project focuses on Twitter (𝕏) data and includes tools for data collection, multilingual analysis, and figure preparation for academic publication.

## Contents  
- `crawler.py`: Python script for collecting tweets using the Twitter API (𝕏 API), filtered by keyword and language.  
- `Eruptions-social-media_review.ipynb`: Jupyter Notebook for cleaning, analysing, and visualising tweet data.  
- Partially processed datasets in CSV format (tweet counts for different keywords/languages).
- `Figures/`: Directory containing Figures output by the Notebook.

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/eruptions-on-social-media.git
   cd eruptions-on-social-media
<!-- pip install -r requirements.txt -->

## Usage  

### 1. Crawling Tweets  
#### Please note that free use of the Twitter standard API has been discontinued as of March 2025.
Edit the `crawler.py` file to specify:
- API credentials (Twitter/𝕏 API keys)  
- Keywords  
- Languages  
- Time range  

Then run:  
```tcsh
python crawler.py
```

### 2. Analysing Data
Open the Jupyter notebook:

```
jupyter notebook Eruptions-social-media_review.ipynb
```

The notebook walks through:

Processing the CSV datasets

Time series analysis of keyword datasets

Statistical tests on keyword datasets

Generating figures for publication



---

## Data Availability  
The repository includes **partially processed CSV datasets**. Original raw data in JSON format (downloaded via the Twitter API) are excluded due to storage limits, but can be provided on request.

## Disclaimer
This research makes use of publicly available data from the Twitter (𝕏) platform for the purpose of studying patterns of public engagement with volcanic eruptions. Only publicly shared tweets were accessed using the official API, and no attempts were made to identify or contact individual users unless their posts were exceptionally widely shared and formed part of aggregate trends. <!-- Any quoted content is anonymised where appropriate, and identifying information has been removed or redacted unless explicit permission was granted by the original poster. This project adheres to ethical standards for research involving social media data, as outlined by our institutional review board and relevant international guidelines.-->


## Citation  
If you use this code or data in your own work, please cite:  
>Farquharson, J. I. *Eruptions in the Attention Economy: Tracking volcanic eruptions and public engagement through multilingual social media analysis*. (Under Review) [2025]

BibTeX and full citation info will be added upon publication.

## License  
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact  
For questions or collaboration inquiries, please contact:  
Jamie Farquahrson, jfarquharson@gs.niigata-u.ac.jp
Niigata University

研究統括機構

新潟大学 災害・復興科学研究所
〒950-2181　新潟市西区五十嵐2の町8050
電話　025-262-7263
