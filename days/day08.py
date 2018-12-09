from helpers import *

d = get_aoc_data(day=8)


def part1_and_2():
    reader = iter(d.as_ints)

    def read_part(reader: typing.Iterator[int]):
        child_count = next(reader)
        metadata_count = next(reader)
        child_values = defaultdict(int)
        meta_sum = 0

        for child_position in range(child_count):
            child_metasum, child_value = read_part(reader)
            meta_sum += child_metasum

            # one-based child numbering!
            child_values[child_position + 1] = child_value

        this_value = 0
        for _ in range(metadata_count):
            metavalue = next(reader)
            meta_sum += metavalue
            if child_count:
                this_value += child_values[metavalue]
            else:
                this_value += metavalue

        return meta_sum, this_value

    meta_sum, this_value = read_part(reader)
    return meta_sum, this_value
