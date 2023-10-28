Steps To be followed:
	1.	Install required packages using “ pip install -r requirements.txt” command
	2.	Download dataset from http://www.vision.caltech.edu/Image_Datasets/Caltech256/
	3.	Place the Dataset folder in the project folder and rename as Caltech256.
	4.	Run movefiles.py
	5.	A database will be formed from the dataset
	6.	Later run index.py, for features extraction. 
	7.	Run query.py, change the features  index file name from featureCNN.h5 to featureCNN_map.h5
		parser.add_argument("-index", type=str, default='featureCNN_map.h5' , help="Path to index") 
	8.	Run compute_mAP.py file 
	9.	Finally run server.py
