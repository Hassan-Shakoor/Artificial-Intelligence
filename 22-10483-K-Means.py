#  22-10483
# Muhammad Hassan Shakoor Rana
# Submitted on Wed before deadline.
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

colors = 10*["g","r","c","b","k"]

def K_Means(k,max_movement,max_iter,data):
    centroids = {}                  # max_movement means the tolerance for we will check the centroid movement.
    for i in range(k):
        centroids[i] = data[i]
    for i in range(max_iter):
        cluster_dict = {}   # clusters dictionary

        for i in range(k):
            cluster_dict[i] = []  #Creating lists for cluster points in cluster dictionary

        eucledian_distance(data,centroids,cluster_dict)  #passing  data points, centroids for eucledian distance and cluster list so that minimum distance points
                                                                                                    #could store in list  in clusters dictionary


        old_centroids = dict(centroids)


        for cluster in cluster_dict:
            new_centroid= np.average(cluster_dict[cluster],axis=0)  # Taking the average of all the clusters mean it is finding the mean of all data points
            centroids[cluster]=new_centroid                                                                                                             # and recreating centroids.


        optimized = True

        for x in centroids:
            original_centroid = old_centroids[x]
            current_centroid = centroids[x]

            check_tolerance=np.sum((current_centroid-original_centroid)/original_centroid*100.0)
            '''if any of the centroids in their movement move more than their toleraance (0.001)
            then we will say that this is not optimized. and if optimized= False then it will do max iterations'''
            
            if check_tolerance > max_movement:                                                                                            
                print( "movement of centroid",np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                optimized = False
            

        if optimized:
            print("\n")
            print("Centroids and its clusters are below: ")
            print("\n")
            print(cluster_dict)
            visualisation(centroids,cluster_dict)
            break

def visualisation(centroids,cluster_dict):
    for centroid in centroids:
            plt.scatter(centroids[centroid][0], centroids[centroid][1],color="purple",s=110)
    for classification in cluster_dict:
        color = colors[classification]
        for featureset in cluster_dict[classification]:
            plt.scatter(featureset[0], featureset[1],color=color)
    plt.show()


def eucledian_distance(dataset,centroids,classifications):
    
        for data in dataset:
            distances = [np.linalg.norm(data - centroids[centroid]) for centroid in centroids] #  eucledian distance formula
            classification = distances.index(min(distances)) # minimum distance value index

            classifications[classification].append(data) # adding the minimum distance point from centrid in clusters dictionary against that particular centroid.


def main():
    a=np.random.uniform(-5,10,50)
    data=np.resize(a, 50).reshape(25,2)
    print("data",data)

    K_Means(2,0.001,100,data)


main()
