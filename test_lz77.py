import lz77

lookahead_buffer_size=150
window_size=150
def test_endode():
    abra_test = lz77.encode("ABRACADABRA",lookahead_buffer_size,window_size)
    pet_test = lz77.encode("Peter Piper picked a peck of pickled peppers;A peck of pickled peppers Peter Piper picked;If Peter Piper picked a peck of pickled peppers,Where's the peck of pickled peppers Peter Piper picked?",lookahead_buffer_size,window_size)
    assert pet_test == [[0, 0, 'P'], [0, 0, 'e'], [0, 0, 't'], [2, 1, 'r'], [0, 0, ' '], [6, 1, 'i'], [0, 0, 'p'], [6, 3, 'p'], [6, 1, 'c'], [0, 0, 'k'], [7, 1, 'd'], [7, 1, 'a'], [9, 2, 'e'], [9, 2, ' '], [0, 0, 'o'], [0, 0, 'f'], [17, 5, 'l'], [18, 3, 'p'], [4, 1, 'p'], [32, 3, 's'], [0, 0, ';'], [0, 0, 'A'], [26, 24, ' '], [71, 18, ';'], [0, 0, 'I'], [38, 2, 'P'], [93, 43, ','], [0, 0, 'W'], [0, 0, 'h'], [6, 2, 'e'], [0, 0, "'"], [75, 2, 't'], [8, 2, ' '], [103, 42, '?']]
    assert abra_test == [[0, 0, 'A'], [0, 0, 'B'], [0, 0, 'R'], [3, 1, 'C'], [2, 1, 'D'], [7, 4, '-']]