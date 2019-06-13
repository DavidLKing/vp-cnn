import sys
import string
import pdb

class Convert:
    def __init__(self):
        pass

    def rebuild_dialogs(self, corrected):
        dialog = -1
        turn = 0
        num_src = []
        for sent in [x.split('\t')[0] for x in corrected]:
            turn += 1
            if sent.startswith("#START"):
                dialog += 1
                turn = 0
                num_src.append("FORGET")
            else:
                num_src.append("({}, {})".format(str(dialog), str(turn)))
            # TODO this was from the old dict system
            # if sent not in num_src:
            #     num_src[sent] = []
            # num_src[sent].append([dialog - 1, turn - 1])
        return num_src

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
        originals = []
        outlines = []
        dialogs = dialogs.readlines()
        num_dias = self.rebuild_dialogs(dialogs)
        assert(len(dialogs) == len(num_dias))
        for line, nums in zip(dialogs, num_dias):
            if not line.startswith('#S'):
                origline = line
                line = line.strip().split('\t')
                turn = line[0].lower()
                turn = turn.translate(str.maketrans('', '', string.punctuation))
                label = line[1]
                if label in labels:
                    outlines.append((nums + '\n', '\t'.join([labels[label], turn]) + '\n'))
                    originals.append(origline)
                # TODO ADD LATER ONCE BASIC EVAL IS FINISHED
                # else:
                #     outlines.append('\t'.join(['999', turn]) + '\n')
            else:
                originals.append(line)
        return outlines, originals


if __name__ == '__main__':
    c = Convert()
    labels = open(sys.argv[1], 'r')
    dialogs = open(sys.argv[2], 'r')
    labels = c.load_labels(labels)
    outlines, original_dialogs = c.main(labels, dialogs)
    outfile = open(sys.argv[3], 'w')
    outidxes = open(sys.argv[4], 'w')
    outdias = open(sys.argv[5], 'w')
    for tuples in outlines:
        line = tuples[1]
        num = tuples[0]
        outfile.write(line)
        outidxes.write(num)
    for line in original_dialogs:
        outdias.write(line)
