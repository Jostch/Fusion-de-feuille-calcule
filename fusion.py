import pandas as pd

fichier_excel = r"C:\Users\aaa\Documents\ISAU\PRELICENCE_2025.xlsx"

# Lire les frais d’atelier
atelier_df = pd.read_excel(
    fichier_excel,
    sheet_name="Sheet_1", # Le nom de la feuille
    header=0
)
# Nettoyer les noms de colonnes
atelier_df.columns = atelier_df.columns.str.strip().str.upper()
print("Colonnes atelier_df :", atelier_df.columns.tolist())

# Lire les frais académiques
academique_df = pd.read_excel(
    fichier_excel,
    sheet_name="Sheet_2",  # Le nom de la feuille
    header=0
)
# Nettoyer les noms de colonnes
academique_df.columns = academique_df.columns.str.strip().str.upper()
print("Colonnes academique_df :", academique_df.columns.tolist())

# Renommer les colonnes pour la fusion
atelier_df = atelier_df.rename(columns={"MONTANT": "FRAIS ATELIER"})
academique_df = academique_df.rename(columns={"MONTANT": "FRAIS ACADÉMIQUES"})

# Fusionner sur la colonne NOMS
fusion_df = pd.merge(atelier_df, academique_df, on="NOMS", how="outer", suffixes=('', '_ACADEM'))

# Fusionner sur la colonne NOMS
fusion_df = pd.merge(atelier_df, academique_df, on="NOMS", how="outer", suffixes=('', '_ACADEM'))

# Garder uniquement les étudiants ayant payé les deux frais
fusion_df = fusion_df.dropna(subset=["FRAIS ATELIER", "FRAIS ACADÉMIQUES"])

# Nettoyer et trier par nom
fusion_df["NOMS"] = fusion_df["NOMS"].str.strip()
fusion_df = fusion_df.sort_values(by=["NOMS"])

# Exporter le résultat
fusion_df.to_excel("fusion_frais_etudiants_1.xlsx", index=False)

print("✅ Fusion terminée. Fichier généré : fusion_frais_etudiants_1.xlsx")