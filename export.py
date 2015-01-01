    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import word
    import config
    import service
    import sys

    email = config.auth.get('email')
    password = config.auth.get('password')

#def exportFromWordsFile():
    try:
        path = 'G:\Programming\PycharmProjects\lingualeo.export\words.txt'
        handler = word.Text(path)

        # export_type = sys.argv[1]
        #if export_type == 'text':
        #    handler = word.Text(config.sources.get('text'))
        #elif export_type == 'kindle':
        #    pass
        #    #handler = word.Kindle(config.sources.get('kindle'))
        #else:
        #    raise Exception('unsupported type')

        handler.read()

        lingualeo = service.Lingualeo(email, password)
        lingualeo.auth()

        list_added_words = []
        list_exists_words = []

        for word in handler.get():
            word = word.lower().replace('\n', '')
            translate_dict = lingualeo.get_translates(word)

            add_word_result = lingualeo.add_word(translate_dict["word"], translate_dict["tword"])

            if not add_word_result["is_new"]:
                #result = "Add word: "
                list_exists_words.append(translate_dict)
            else:
                #result = "Already exists: "
                list_added_words.append(translate_dict)

                #result = result + word
                #print(result)
        print('Добавленные слова:')
        for translate_dict in list_added_words:
            print(translate_dict['word'] + ' ' + translate_dict['tword'])

        print('Слова, которые уже были ранее:')
        for translate_dict in list_exists_words:
            print(translate_dict['word'] + '\t' + translate_dict['tword'])

    except Exception as e:
        pass
        print(e.args, e.message)