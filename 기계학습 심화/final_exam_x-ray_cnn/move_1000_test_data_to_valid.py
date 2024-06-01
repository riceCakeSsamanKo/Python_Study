import os
import random
import shutil

# 경로 설정
train_images_dir = 'E:/GitHub/Python_Study/기계학습 심화/final_exam_x-ray_cnn/pidray/train/images/'
train_labels_dir = 'E:/GitHub/Python_Study/기계학습 심화/final_exam_x-ray_cnn/pidray/train/labels/'
valid_images_dir = 'E:/GitHub/Python_Study/기계학습 심화/final_exam_x-ray_cnn/pidray/valid/images/'
valid_labels_dir = 'E:/GitHub/Python_Study/기계학습 심화/final_exam_x-ray_cnn/pidray/valid/labels/'

# 유효한 파일 목록을 가져오기
train_images = sorted(os.listdir(train_images_dir))
train_labels = sorted(os.listdir(train_labels_dir))

# 파일 이름에서 확장자를 제거한 후 매칭
train_files = [os.path.splitext(f)[0] for f in train_images]

# 랜덤하게 1000개의 파일 선택
random.seed(123)  # 결과 재현성을 위해 시드 고정
selected_files = random.sample(train_files, 1000)

# 대상 디렉토리 생성
os.makedirs(valid_images_dir, exist_ok=True)
os.makedirs(valid_labels_dir, exist_ok=True)

# 선택된 파일들을 validation 디렉토리로 이동
for file in selected_files:
    image_path = os.path.join(train_images_dir, f"{file}.png")
    label_path = os.path.join(train_labels_dir, f"{file}.txt")
    
    valid_image_path = os.path.join(valid_images_dir, f"{file}.png")
    valid_label_path = os.path.join(valid_labels_dir, f"{file}.txt")
    
    # 이미지와 라벨 파일 이동
    shutil.move(image_path, valid_image_path)
    shutil.move(label_path, valid_label_path)

print(f"Moved {len(selected_files)} files from train to valid directories.")
