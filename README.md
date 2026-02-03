# ctd-ingest

CTD (Comparative Toxicogenomics Database) is a robust, publicly available database that aims to advance understanding about how environmental exposures affect human health. It provides manually curated information about chemical-gene/protein interactions, chemical-disease and gene-disease relationships. These data are integrated with functional and pathway data to aid in development of hypotheses about the mechanisms underlying environmentally influenced diseases.

- [CTD Bulk Downloads](http://ctdbase.org/downloads/)

## Chemical to Disease

This ingest takes only the chemical to disease rows where a direct evidence label is applied, and creates ChemicalEntity and Disease nodes connected by a ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation. The chemical ID row is expected to need a 'MESH:' prefix added, the disease id is used as-is.

Rows are included only if the direct evidence field is 'therapeutic' and the `biolink:affects` predicate is used to avoid making too strong a claim.

**Biolink Captured:**

- `biolink:ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation`
    - id (random uuid)
    - subject (chemical id)
    - predicate (`biolink:affects`)
    - object (disease id)
    - publication (pubmed ids provided by file)
    - aggregating_knowledge_source (`["infores:monarchinitiative"]`)
    - primary_knowledge_source (`infores:ctd`)

## Setup

```bash
just setup
```

## Usage

### Download source data

```bash
just download
```

### Run transforms

```bash
# Run all transforms
just transform-all

# Run specific transform
just transform <transform_name>
```

### Run tests

```bash
just test
```

## Adding New Ingests

Use the `create-koza-ingest` Claude skill to add new ingests to this repository.

## Citation

Davis AP, Wiegers TC, Johnson RJ, Sciaky D, Wiegers J, Mattingly CJ. Comparative Toxicogenomics Database (CTD): update 2023. Nucleic Acids Res. 2022 Sep 28.

## License

BSD-3-Clause
