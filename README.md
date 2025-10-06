# CI/CD Ejemplo: Jenkins + Python + pytest

Proyecto mínimo para integrar **pruebas automatizadas** en un **pipeline de Jenkins**.
Incluye:
- `pytest` con cobertura (`pytest-cov`)
- Publicación de resultados JUnit en Jenkins
- Publicación de cobertura mediante XML (Cobertura)
- `Jenkinsfile` listo para usar (con y sin Docker)

## Estructura
```
.
├── Jenkinsfile
├── Jenkinsfile.sin-docker
├── README.md
├── requirements.txt
├── pytest.ini
├── src/
│   └── calculadora.py
└── tests/
    └── test_calculadora.py
```
