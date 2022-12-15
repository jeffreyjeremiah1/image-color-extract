from collections import Counter
from sklearn.cluster import KMeans
import cv2


class Palette:

    def __init__(self, numb_of_color, file, delta):
        super().__init__()
        self.number = int(numb_of_color)
        self.file = file
        self.delta = delta
        image = cv2.imread(self.file)
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def rgb_to_hex(self, rgb_color):
        hex_color = "#"
        for i in rgb_color:
            i = int(i)
            hex_color += ("{:02x}".format(i))
        return hex_color

    def prep_image(self, raw_img):
        modified_img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
        modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
        return modified_img

    def color_analysis(self, img):
        clf = KMeans(n_clusters=self.number)
        color_labels = clf.fit_predict(img)
        center_colors = clf.cluster_centers_
        counts = Counter(color_labels)
        counts_val = [(counts[col]/1000000) for col in counts]
        print(counts_val)
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [self.rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
        print(hex_colors)
        return hex_colors, counts_val

    def show_colors(self):
        modified_image = self.prep_image(self.image)
        return self.color_analysis(modified_image)


#
# palette = Palette()
# print(type(palette.show_colors()))
