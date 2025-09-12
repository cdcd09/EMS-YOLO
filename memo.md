https://github.com/cdcd09/EMS-YOLO.git


#사전작업
conda env create -f environment.yml
conda activate coco
pip install -r requirements.txt

python download_dataset.py

dataset의 yaml 파일 밖으로 뺄것.

python train.py \
  --data data.yaml \
  --cfg models/resnet10.yaml \
  --weights '' \
  --epochs 100 --batch-size 8 --imgsz 640 --device 0