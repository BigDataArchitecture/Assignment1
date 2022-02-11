import warnings
warnings.filterwarnings("ignore")
import sys
sys.path.append('/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment_1/eie-sevir/') # enter path to sevir module if not installed.
from sevir.generator import *
print('hi')
vil_seq = SEVIRGenerator(x_img_types=['vil'],batch_size=16)
print(vil_seq)