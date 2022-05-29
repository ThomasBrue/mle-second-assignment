myText = """
<div style="max-width: 700px">
The following tables display the best results (f1, accuracy, jaccard and precision) that were achieved with certain classifier input parameters. 
<br>
The tables display the train and test time that was required to achieve the highest f1 scores. 
<br>
<h5>Image Dataset</h5>
From the four provided image datasets the dataOpenCV_3D yielded the best results.
<br>
The highest f1 score of 0.485 was achieved with random_forest. As input parameters a number_of_trees of 100 and a max_features equal to log2 was provided.
<br>
With the same input configuration for random_forest the highest precision of 0.417 and the highest accuracy of 0.489 could be achieved.
<h5>Heart Failure Dataset</h5>
Random_forest outperformed all other classifiers when it comes to effectiveness (accuracy, jaccard, f1 and precision). 
<br>
However, when it comes to efficiency (train and test time) then random_forest performs worse than the other classifier. This can be seen by comparing the train and test time of the classifier. Random_forest requires longer to train and test times.
<h5>Covertype Dataset</h5>
A similar result could be found for the covertype dataset. Random_forest outperforms the other classifier when it comes to effectiveness but takes longer to train and test.
</div>
"""
