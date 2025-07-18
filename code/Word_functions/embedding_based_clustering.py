import json
import os
import sys
import numpy as np
import pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_samples, silhouette_score
import umap
import matplotlib.pyplot as plt

# ======================================================================================


def embedding_clustering(input_df, output_folder, batch_size = 32):
    
    # 1.1 Prepare Data ----
    df = pd.DataFrame({
        "id" : input_df.record_id,
        "keywords" : input_df.cat_keywords
    })
    df.keywords = df.keywords.apply(lambda x: " ".join(x))
    
    # 1.2 Load SciBERT ----
    DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    MODEL_NAME = "allenai/scibert_scivocab_uncased"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME).to(DEVICE)
    model.eval()
    
    
    # 2. Compute Embeddings -----------------------------------------------------------
    BATCH_SIZE = batch_size
    keyword_list = [
        k for k in df['keywords']
        if isinstance(k, str) and k.strip() and not pd.isna(k)
    ]
    
    ids = df['id'].tolist()
    all_keywords = []
    document_embeddings = []
    
    for i in tqdm(range(0, len(keyword_list), BATCH_SIZE), desc="Embedding documents"):
        batch_keywords = keyword_list[i:i+BATCH_SIZE]
        texts = batch_keywords  # each is a single char string
        all_keywords.extend(texts)
    
        with torch.no_grad():
            inputs = tokenizer(
                texts,
                padding='max_length',
                truncation=True,
                max_length=64,
                return_tensors='pt'
            )
            inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
            outputs = model(**inputs)
            cls_embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
            document_embeddings.extend(cls_embeddings)
    document_embeddings = np.stack(document_embeddings)
    
    
    
    # 3. Agglomarative Clustering ----------------------------------------------
    
    ## 3.1 Calculate Silhouette Widths for different Cluster numbers (2-20) ---
    range_n_clusters = np.arange(2,21)
    scores = []
    
    for n_clusters in range_n_clusters:
        clustering = AgglomerativeClustering(n_clusters=n_clusters)
        labels = clustering.fit_predict(document_embeddings)
        score = silhouette_score(document_embeddings, labels)
        scores.append(score)
        print(f"Computing cluster {n_clusters}/20...")
    
    ## Plotting
    plt.figure(figsize= (9,5))
    plt.plot(range_n_clusters, scores, marker='o')
    plt.xlabel("Number of clusters")
    plt.ylabel("Silhouette width/score")
    plt.ylim([-1,1])
    plt.xticks(range(1,21))
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    
    plt.savefig(f"{output_folder}/embedding_clusters_1.png", dpi=300)
    #plt.show()
    
    
    ## 3.2 Plot Silhouette scores for the best solution (here: 2 cluster solution) ---
    if range_n_clusters[np.argmax(scores)] == 2:
        
        n_clusters = 2 #range_n_clusters[np.argmax(scores)]
        clustering = AgglomerativeClustering(n_clusters=n_clusters)
        cluster_labels = clustering.fit_predict(document_embeddings)
        silhouette_avg = silhouette_score(document_embeddings, cluster_labels)
        sample_silhouette_values = silhouette_samples(document_embeddings, cluster_labels)
        
        y_lower = 10
        colors = ("blue", "darkorange")
        cluster_means = []
    
        print(f"Computing individual silhouette scores for {n_clusters} clusters...")
        plt.figure(figsize=(9, 5))
        for i in range(n_clusters):
            ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
            ith_cluster_silhouette_values.sort()
            mean_val = ith_cluster_silhouette_values.mean()
            cluster_means.append(mean_val)
            #print(f"Average Silhouette score for Cluster {i}: {mean_val:.3f}")
            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i
        
            plt.fill_betweenx(
                np.arange(y_lower, y_upper),
                0, ith_cluster_silhouette_values,
                facecolor=colors[i], edgecolor=colors[i], alpha=0.7
            )
            plt.text(-0.1, y_lower + 0.5 * size_cluster_i, str(i), fontsize=11, fontweight = "bold")
            
            plt.text(
                0.05,
                y_lower + 0.5 * size_cluster_i,
                f"{mean_val:.2f}",
                va='center',
                ha='left',
                fontsize=10,
                color='black',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.9, boxstyle='round,pad=0.2')
            )
            y_lower = y_upper + 10
        
        plt.xlabel("Silhouette width/score")
        plt.ylabel("Clusters")
        plt.xticks(np.arange(-0.2, 1.1, 0.1))
        plt.axvline(x=silhouette_avg, color="black", linestyle="--")
        
        plt.text(
            silhouette_avg, 0,
            f"{silhouette_avg:.2f}",
            va='bottom',
            ha='center',
            fontsize=11,
            color='black',
            bbox=dict(facecolor='white', edgecolor='black', alpha=1, boxstyle='round,pad=0.2')
        )
        
        plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.savefig(f"{output_folder}/embedding_clusters_2.png", dpi=300)
        #plt.show()

    return



