import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Laden des Datensatzes von der URL
url = 'https://raw.githubusercontent.com/WHPAN0108/BHT-DataScience-S23/main/clustering/data/country.txt'
df = pd.read_csv(url, sep=',')

# Überblick über die Daten
print(df.head())

# Daten standardisieren
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.iloc[:, 1:])

# Elbow-Methode zur Bestimmung der optimalen Anzahl von Clustern für K-means
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    sse.append(kmeans.inertia_)

# Plot der Elbow-Methode
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Sum of Squared Distances')
plt.title('Elbow-Methode zur Bestimmung der optimalen Anzahl von Clustern')
plt.show()

# Anzahl der Cluster basierend auf der Elbow-Methode
n_clusters = 3  # Beispielwert, basierend auf dem Elbow-Plot

# K-means Clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['kmeans_cluster'] = kmeans.fit_predict(df_scaled)

# Hierarchisches Clustering
hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
df['hierarchical_cluster'] = hierarchical.fit_predict(df_scaled)

# PCA zur Reduktion der Dimensionen auf 2D
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
df['pca1'] = df_pca[:, 0]
df['pca2'] = df_pca[:, 1]

# Cluster-Namen basierend auf den Analysen
cluster_names = {
    0: "Entwickelte Länder",
    1: "Mittel entwickelte Länder",
    2: "Weniger entwickelte Länder"
}

# Cluster-Namen zuweisen
df['kmeans_cluster_name'] = df['kmeans_cluster'].map(cluster_names)
df['hierarchical_cluster_name'] = df['hierarchical_cluster'].map(cluster_names)

# Visualisierung der Cluster mit Namen
plt.figure(figsize=(14, 6))

# K-means Cluster
plt.subplot(1, 2, 1)
sns.scatterplot(x='pca1', y='pca2', hue='kmeans_cluster_name', data=df, palette='viridis', s=100)
plt.title('K-means Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')

# Hierarchische Cluster
plt.subplot(1, 2, 2)
sns.scatterplot(x='pca1', y='pca2', hue='hierarchical_cluster_name', data=df, palette='viridis', s=100)
plt.title('Hierarchical Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')

plt.show()

# Empfehlungen für den CEO basierend auf den Cluster-Ergebnissen
for cluster in range(n_clusters):
    print(f"\nEmpfehlungen für Cluster {cluster} ({cluster_names[cluster]}):")
    cluster_data = df[df['kmeans_cluster'] == cluster]
    print(cluster_data[['income', 'child_mort', 'life_expec']].describe())
