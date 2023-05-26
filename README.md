# P.R. Data Correlations

For our final project in CCOM6995/4995, we will explore if there is a positive correlation between crime statistics and unemployment.

This project provides a valuable opportunity for us to enhance our statistical skills, reinforce our understanding of the techniques learned in class, and apply them to a real-world scenario.

We will apply various techniques learned in class, such as p-value tests, confidence interval tests, and data cleaning and wrangling, to thoroughly examine this relationship.

## Installation

We provide options for package management. Our manager of choice is [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer), a modern environment and package installer for Python.

```bash
# Install the Poetry package manager for Python
make get-poetry

# Install our dependencies
make install

# Enter the virtual environment
poetry shell
```

**If Poetry isn't your thing, that's fine!** We also provide a `requirements.txt` file you can use:

```bash
make install-reqs
```

## Contributing

All contributions from team members are welcome. However, some guidelines are in place to make sure the project stays clean and compliant with best practices.

Our coding style follows the Python Software Foundation's endorsed autoformatter, [Black](https://github.com/psf/black).

- Install the automatic formatter by running `poetry run pre-commit install`.
- Set up your editor to auto-format on save.
- Avoid absolute paths in favor of relative paths when committing.
- Commit any assets into the tree, but make sure your results are reproducible.
- Inspect your code carefully.

Our formatter allows for standards compliance with minimal hassle. All your commits will be autoformatted after installation.

## Folder structure

- `./src`: Contains scripts or notebooks
- `./data/raw`: Contains the unprocessed data
- `./data/clean`: Contains data after preprocessing/cleanup
- `./results/visual`: Contains visual analyses or representations

## Data Sources

There are a number of datasets here which are not part of the final product. We analyzed them for exploration before choosing a final analysis subject.
Here is the list of assigned topics converted into bold markdown items with links:

- **[Empleos y Desempleos](https://estadisticas.pr/files/inventario/empleo_y_desempleo/2023-04-27/DTRH-EmpleoDesempleo-2023-03.zip)**
- **[Quiebras](https://estadisticas.pr/files/inventario/quiebras/2023-04-17/USBC-BankruptcyFilings-2023-03.pdf)**
- **[Delitos Tipo 1](https://estadisticas.pr/files/inventario/delitos_tipo_i/2023-04-17/Policia-DelitosTipoI-2023-03.zip)**
- **[HIV](https://estadisticas.pr/files/inventario/pr_hiv_aids_surveillance_summary/2023-04-10/DS-HIV-AIDS-2023-03.zip)**
- **[Cambios en precio de gasolina](https://estadisticas.pr/files/inventario/precios_mayoristas_gasolina/2023-04-10/DACO-PrecioMayoristas-2023-04-06.pdf)**
- **[Precios al consumidor](https://estadisticas.pr/files/inventario/indice_de_precios_al_consumidor/2023-03-31/DTRH-IPC-2023-02.zip)**
- **[Outages de energia en PR por LUMA (2021-)](https://luma-outages.jpadilla.com/data?sql=select+*+from+customers)**
- **[Generacion, consumo, costo, incresos y clientes del sistema electrico de PR (LUMA)](https://www.indicadores.pr/dataset/generacion-consumo-costo-ingresos-y-clientes-del-sistema-electrico-de-puerto-rico/resource/8025f821-45c1-4c6a-b2f4-8d641cc03df1)**
- **[Clases Presenciales por Municipio](https://datos.pr.gov/datacard/clases-presenciales-por-municipio?parent=RWR1Y2FjacOzbiAoRENDKQ==&parentPath=ZGF0YWNhcmRzY29sbGVjdGlvbi9lZHVjYWNpb24tZGNj)**
- **[Cambio poblacional 2020-2022](https://censo.estadisticas.pr/node/517)**
- **[Actividad Sismica](https://redsismica.uprm.edu/spanish/sismicidad/catalogos/catalogo_general.php)**
- **[Defunciones Registradas](https://datos.estadisticas.pr/dataset/defunciones-registradas)**
