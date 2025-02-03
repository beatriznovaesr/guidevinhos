import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

class Kmeans:

    def lista_dados(self, favoritos, vinhos):
        if favoritos:
            self.dados_favoritos = favoritos["vinhos_favoritos"]
            self.dados_vinhos = vinhos
            self.converter_df()
            self.codifica_df()
            self.normaliza_df()
            vinhos_sugeridos = self.aplica_kmeans()
        else:
            vinhos_sugeridos = None
        return vinhos_sugeridos  

    def converter_df(self):
        self.df_favoritos = pd.DataFrame(self.dados_favoritos)
        self.df_vinhos = pd.DataFrame(self.dados_vinhos)
    
    def codifica_df(self):
        label_encoder = LabelEncoder()
        self.df_favoritos["categoria_encoded"] = label_encoder.fit_transform(self.df_favoritos["categoria"])
        self.df_favoritos["safra_encoded"] = label_encoder.fit_transform(self.df_favoritos["safra"])
        self.df_favoritos["uva_encoded"] = label_encoder.fit_transform(self.df_favoritos["uva"])

        self.df_vinhos["categoria_encoded"] = label_encoder.fit_transform(self.df_vinhos["categoria"])
        self.df_vinhos["safra_encoded"] = label_encoder.fit_transform(self.df_vinhos["safra"])
        self.df_vinhos["uva_encoded"] = label_encoder.fit_transform(self.df_vinhos["uva"])
    
    def normaliza_df(self):
        scaler = StandardScaler()
        features = ["categoria_encoded", "safra_encoded", "uva_encoded"]
        self.df_favoritos_scaled = scaler.fit_transform(self.df_favoritos[features])
        self.df_vinhos_scaled = scaler.fit_transform(self.df_vinhos[features])

    def aplica_kmeans(self):
        k = 10
        kmeans = KMeans(n_clusters=k, random_state=42)
        self.df_vinhos["Cluster"] = kmeans.fit_predict(self.df_vinhos_scaled)

        self.df_favoritos = self.df_favoritos.merge(
        self.df_vinhos[["_id", "Cluster"]],  
        on="_id",
        how="left"
    )
        favoritos_clusters = self.df_favoritos["Cluster"].unique()
        vinhos_sugeridos = self.df_vinhos[self.df_vinhos["Cluster"].isin(favoritos_clusters)]
        return vinhos_sugeridos

        


