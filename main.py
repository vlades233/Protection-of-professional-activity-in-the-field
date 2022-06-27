import hashlib


def password_hack(hashed_string, word_list, output_file_name):
    try:
        words = open(word_list, "r")
        output_file = open(output_file_name, 'w')
    except:
        print("\n File Not Found")
        quit()

    counter = 1
    for word in words:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()

        print('Trying Password %d: %s ' % (counter, word.strip()))
        output_file.write('Trying word %d: %s ' % (counter, word.strip()))
        output_file.write('\nPossible word hash: %s ' % calculated_hash)
        output_file.write('\nActual hash: %s ' % hashed_string)
        output_file.write('\n-------------------------------\n')

        counter += 1

        if calculated_hash == hashed_string:
            print('\nPassword found: %s ' % word)
            break

    else:
        print('\nPassword Not Found, try another wordlist or hash')


def main():
    hashed_string ="0c3f20fc51e14a381ebb6241abe16a0d6c188bc9e320abaddf5813baceb6b251"
    word_list = "files/all_passphrase.txt"
    output_file_name = "Veselovskyi_sh256"

    password_hack(hashed_string, word_list, output_file_name)


if __name__ == '__main__':
    main()
