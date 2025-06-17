# Fusion des frais étudiants

Ce script Python permet de fusionner deux feuilles d’un fichier Excel contenant les informations de frais d’atelier et de frais académiques des étudiants.

## Fonctionnement

1. **Lecture des feuilles Excel**  
   Le script lit deux feuilles (`Sheet_1` et `Sheet_2`) du fichier `PRELICENCE_2025.xlsx`.

2. **Nettoyage des colonnes**  
   Les noms de colonnes sont nettoyés (suppression des espaces, mise en majuscules).

3. **Renommage des colonnes**  
   Les colonnes `MONTANT` sont renommées en `FRAIS ATELIER` et `FRAIS ACADÉMIQUES` pour plus de clarté.

4. **Fusion des données**  
   La fusion se fait sur la colonne `NOMS` présente dans les deux feuilles.

5. **Tri et export**  
   Le résultat est trié par nom d’étudiant puis exporté dans le fichier `fusion_frais_etudiants.xlsx`.

## Utilisation

- Place le script Python et le fichier Excel dans le même dossier.
- Exécute le script avec Python :
  ```
  python fusion.py
  ```
- Le fichier fusionné sera généré dans le même dossier.

## Prérequis

- Python 3
- pandas

# Installe pandas si besoin :
```
pip install pandas
```