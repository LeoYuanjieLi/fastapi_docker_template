import os


def test_read_data(test_data_dir):
    f = os.path.join(test_data_dir, "temp.txt")
    with open(f, "r") as f_in:
        lines = [int(l.strip()) for l in f_in.readlines()]
    print(lines)
    assert lines == [1, 2, 3]
