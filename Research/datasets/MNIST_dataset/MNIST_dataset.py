import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from tensorflow.keras.datasets import mnist

class MNIST_dataset:
  
  @staticmethod
  def load_data():
    return mnist.load_data()
  
  def __init__(self):
    (self.train_images, self.train_labels)\
      , (self.test_images, self.test_labels) = self.load_data()


  def show_digits(self, n=5, 
                  colormap='cividis', 
                  custom_colors=None,
                  gray_scale=False):
    num_digits_to_plot = min(n, len(self.train_images))

    fig_width = 1.2  # Width of each subplot in inches
    fig_height = 1.2  # Height of each subplot in inches
    plt.figure(figsize=(fig_width * num_digits_to_plot, fig_height))
    
    for i in range(num_digits_to_plot):
        plt.subplot(1, num_digits_to_plot, i + 1)
        if gray_scale:
          plt.imshow(self.train_images[i], cmap='gray')
        elif custom_colors:
          cmap = LinearSegmentedColormap.from_list("CustomColormap", custom_colors, N=256)
          plt.imshow(self.train_images[i], cmap=cmap)
        else:
          plt.imshow(self.train_images[i], cmap=colormap)
        plt.title(f"Label: {self.train_labels[i]}")
        plt.axis('off')

    plt.tight_layout()  # Adjust subplots to fit in the figure
    plt.show()

  def get_digit(self, index):
    return self.train_images[index], self.train_labels[index]

  def get_num_digits(self):
    return len(self.train_images)

if __name__ == "__main__":
    # Example Usage:
    mnist_data = MNIST_dataset()
    mnist_data.show_digits(gray_scale=True)

# # Display the total number of digits in the dataset
# total_digits = mnist_data.get_num_digits()
# print(f"Total number of digits in the dataset: {total_digits}")
