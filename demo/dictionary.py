dictionary = {}
flag = 'a'
page = 'a'
off  = 'a'

while flag == 'a' or 'c':

    flag = raw_input("add or search word?(a/c)")
    if flag == 'a':
        word = raw_input("enter word:")
        defintion = raw_input("enter value:")
        dictionary[str(word)] = str(defintion) #add
        print 'success'
        page = raw_input('do you need search dic?(a/0)')
        if page == 'a':
            print dictionary
        else:
            continue
    elif flag == 'c':
        search_word = raw_input("word?")
        for key in sorted(dictionary.keys()):
            print dictionary.keys()
            print search_word
            if str(search_word) == key:
                print "exist:",key,dictionary[key]
                break
            else:
                off == 'b'
        if off == 'b':
            print 'sorry'
    else:
        print  'error'
        break