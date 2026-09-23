# Data

## What was collected

Daily prices scraped from the online stores of four large Colombian retailers. Collection started on 7 August 2023 and ended on 18 July 2024. A Python and Selenium scraper did the collection, scheduled on a server at Universidad ICESI.

| Store code | Business type                                  | Days observed | Products | Observations |
|------------|------------------------------------------------|--------------:|---------:|-------------:|
| A1         | Multichannel large supermarket (GSM)           | 317           | 7,610    | 412,234      |
| A2         | Multichannel large supermarket (GSM)           | 301           | 4,595    | 304,336      |
| B          | Price-comparison website / delivery app (PCW)  | 83            | 1,914    | 66,433       |
| C          | Multichannel hard-discount store (TDM)         | 307           | 359      | 36,278       |
| **Total**  |                                                | 339           | 14,425   | 819,281      |

These counts are after the filters in `21_filter_data`.

## Folder layout

The pipeline expects these folders. Only `sample/` and `product_classification.xlsx` are included in the repository.

```
data/
├── raw/            A1_raw.csv, A2_raw.csv, B_raw.csv, C_raw.csv         ← scraped files (not published)
├── interim/        A1_clean.csv … C_clean.csv, Retailer_data.csv        ← created by notebooks 11–15
├── processed/      Filter_Data_<case>.csv, Data_Regular_Price_<case>_<w>_<w>.csv ← created by 21–23
├── sample/         Retailer_data_sample.csv                              ← included
└── product_classification.xlsx                                           ← included
```

## Full dataset

The raw and intermediate files add up to about 1.5 GB, which is more than GitHub allows, so they are not in the repository.

The published dataset is the anonymized, cleaned panel `Retailer_data.csv`: about 1.3 million rows, 17 MB zipped, with the columns `fecha`, `descripcion`, `tienda` and `precio`. The raw scraped files contain store URLs and page fields, so they are not published.

> **Download:** _link pending (Zenodo DOI)_. Save the file as `data/interim/Retailer_data.csv`, then run `notebooks/20_estimations.ipynb` and `30_results.ipynb`, or steps 2–3 of `00_master.ipynb`.

## Sample

`sample/Retailer_data_sample.csv` has 12,987 rows: 50 products from each retailer, with their full price history, in the same format as `interim/Retailer_data.csv`. If the full file is missing, `21_filter_data` switches to the sample automatically. This means steps 20–32 of the pipeline run right after cloning the repo. The results won't match the paper, which used the full dataset.

| Column        | Type   | Description                                                                 |
|---------------|--------|-----------------------------------------------------------------------------|
| `Unnamed: 0`  | int    | Row id left over from the join step (sample only; dropped in `21_filter_data`) |
| `fecha`       | date   | Collection date (YYYY-MM-DD)                                                  |
| `descripcion` | string | Normalized product description (lower case, no accents); the product key    |
| `tienda`      | string | Store code: `A1`, `A2`, `B`, `C` (see table above)                          |
| `precio`      | float  | Posted price in Colombian pesos (COP), the lowest price shown that day      |

## Product classification

`product_classification.xlsx` assigns 8,761 product descriptions to COICOP / DANE CPI groups (`Descripcion`, `Code`, `Group`). The first pass used a local Llama 3 model (`src/classify_products_llm.R`), and the results were then reviewed by hand. The tables and figures by product category use this file.

## Anonymization

The paper refers to stores only by business type, and the published data follow the same rule:

- Store names are replaced by the codes `A1`, `A2`, `B` and `C`.
- Platform B lists products from many different shops, and each product key starts with the shop's name. That name is replaced by a short hash, for example `store_3acafd_…`, so products stay distinct without naming the shops. Notebook `14_clean_store_B` applies the same hash.
- If one of the four store names appears inside a product description, it is replaced by that store's code.
- The code uses generic patterns for URLs, so it doesn't name the stores either.

## Terms of use

The prices were publicly visible on the retailers' websites when they were collected, and they are shared only for academic research. The retailers own their product names and trademarks.
