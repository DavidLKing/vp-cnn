import sys
import string
import pdb

class Convert:
    def __init__(self):
        pass

    def load_labels(self, labels_file):
        label_dict = {}
        for line in labels_file:
            line = line.strip().split('\t')
            num = line[0]
            text = line[1]
            assert(text not in label_dict)
            label_dict[text] = num
        return label_dict

    def main(self, labels, dialogs):
        outlines = []
        for line in dialogs:
            if not line.startswith('#S'):
                line = line.strip().split('\t')
                turn = line[0].lower()
                turn = turn.translate(str.maketrans('', '', string.punctuation))
                label = line[1]
                if label in labels:
                    outlines.append('\t'.join([labels[label], turn]) + '\n')
                else:
                    outlines.append('\t'.join(['999', turn]) + '\n')
        return outlines


if __name__ == '__main__':
    c = Convert()
    labels = open(sys.argv[1], 'r')
    dialogs = open(sys.argv[2], 'r')
    labels = c.load_labels(labels)
    outlines = c.main(labels, dialogs)
    outfile = open(sys.argv[3], 'w')
    for line in outlines:
        outfile.write(line)
