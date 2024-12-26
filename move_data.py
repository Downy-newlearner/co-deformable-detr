import os
import shutil

# 기존 경로
base_path = "Car-Damage-Images-1"
new_base_path = "data/coco"

# COCO 데이터 경로 생성
os.makedirs(f"{new_base_path}/annotations", exist_ok=True)
os.makedirs(f"{new_base_path}/train2017", exist_ok=True)
os.makedirs(f"{new_base_path}/val2017", exist_ok=True)
os.makedirs(f"{new_base_path}/test2017", exist_ok=True)

# 파일 이동 함수
def move_files(src_folder, dst_folder, annotation_file, annotation_name):
    # 이미지 파일 이동
    for file in os.listdir(src_folder):
        if file.endswith((".jpg", ".jpeg", ".png")):
            shutil.move(os.path.join(src_folder, file), os.path.join(dst_folder, file))
    # 어노테이션 파일 이동 및 이름 변경
    shutil.move(os.path.join(src_folder, annotation_file), os.path.join(f"{new_base_path}/annotations", annotation_name))

# 파일 이동 작업
move_files(f"{base_path}/train", f"{new_base_path}/train2017", "_annotations.coco.json", "instances_train2017.json")
move_files(f"{base_path}/valid", f"{new_base_path}/val2017", "_annotations.coco.json", "instances_val2017.json")
move_files(f"{base_path}/test", f"{new_base_path}/test2017", "_annotations.coco.json", "instances_test2017.json")

print("데이터 구조 변환이 완료되었습니다!")
