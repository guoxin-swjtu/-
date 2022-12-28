import cv2
import pandas as pd
import numpy as np
bio_path=r'D:\desktop\yhl-rg prediction\bio.tif'
pisr_path=r'D:\desktop\yhl-rg prediction\pisr.tif'
bio = cv2.imread(bio_path,-1)
pisr = cv2.imread(pisr_path,-1)
data_bio = np.reshape(bio,(3527773,1))
data_pisr = np.reshape(pisr,(3527773,1))
data = np.hstack((data_bio, data_pisr))
data = pd.DataFrame(data)
data.to_csv(r'D:\desktop\yhl-rg prediction\res12281400.csv')