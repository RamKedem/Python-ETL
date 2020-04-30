def justify(sentence, required_line_width):
    for sub_sentence in sentence.split('.'):
        if 0 < len(sub_sentence) <= required_line_width:
            sub_sentence = sub_sentence[1:] + '.' if sub_sentence[0] == ' ' \
                                                  else sub_sentence + '.'
            spaces_left = (required_line_width - len(sub_sentence))//2 + 2
            spaces_right = required_line_width - len(sub_sentence) - spaces_left + 2
            output = sub_sentence.split(' ')[0] +  \
                                                + spaces_left * ' '\
                                                + ' '.join(sub_sentence.split(' ')[1:-1]) \
                                                + spaces_right * ' '\
                                                + sub_sentence.split(' ')[-1]
            yield output


if '__name__'=='main':

    string = "Don't wish to be normal. Wish to be yourself. To the hilt. Find out what you're best at, and develop it, and hopscotch your weaknesses. Wish to be great at whatever you are."
    line_width = 40
    for sentence in justify(string,line_width):
        print(sentence)