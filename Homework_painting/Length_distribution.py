import matplotlib.pyplot as plt


plt.rcParams['savefig.bbox'] = 'tight'
plt.figure(figsize=(10, 8))
path = input('Enter path to fastq file: ')


def length_distribution(path_to_fastq):
    with open(path_to_fastq, 'r') as f:
        lines = f.readlines()
        lens = []
        for i in range(1, len(lines), 4):
            lens.append(len(lines[i].rstrip()))
        plt.hist(lens, bins=20, color='green')
        plt.title('Sequence length distribution')
        plt.xlabel('Sequence length')
        plt.ylabel('Frequency')
        plt.grid()
        plt.savefig('Sequence_length.png')
        plt.show()


length_distribution(path)