import os
import random
import shutil
import argparse

def split_dataset(dataset_path, dest_path, train_split_ratio : float):
    # Create a folder for the training dataset and a folder for the test dataset
    train_path = os.path.join(dest_path, "train")
    test_path = os.path.join(dest_path, "test")
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)

    # Loop through each class folder in the dataset
    for class_folder in os.listdir(dataset_path):
        if not os.path.isdir(os.path.join(dataset_path, class_folder)):
            continue

        # Create a subfolder for the class in both the training and test datasets
        train_class_path = os.path.join(train_path, class_folder)
        test_class_path = os.path.join(test_path, class_folder)
        os.makedirs(train_class_path, exist_ok=True)
        os.makedirs(test_class_path, exist_ok=True)

        # Loop through each image in the class folder
        images = os.listdir(os.path.join(dataset_path, class_folder))
        random.shuffle(images)
        num_train = int(len(images) * train_split_ratio)

        # Move the first num_train images to the training dataset
        for i in range(num_train):
            image_name = images[i]
            src_path = os.path.join(dataset_path, class_folder, image_name)
            dest_path = os.path.join(train_class_path, image_name)
            shutil.copyfile(src_path, dest_path)

        # Move the remaining images to the test dataset
        for i in range(num_train, len(images)):
            image_name = images[i]
            src_path = os.path.join(dataset_path, class_folder, image_name)
            dest_path = os.path.join(test_class_path, image_name)
            shutil.copyfile(src_path, dest_path)

    print("Dataset split into training and test sets.")

if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Split an image classification dataset into training and test sets.")
    parser.add_argument("dataset_path", type=str, help="Path to the classification dataset folder.")
    parser.add_argument("dest_path", type=str, help="Path to the destination folder where the split datasets will be saved.")
    parser.add_argument("train_split_ratio", type=float, required=False, default=0.9, help="Ratio of the dataset to use for training (between 0 and 1).")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the split_dataset function with the command-line arguments
    split_dataset(args.dataset_path, args.dest_path, args.train_split_ratio)
