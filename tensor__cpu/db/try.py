import pymysql
import pymysql.cursors


def load_params(configure_file):
    dbdict = {}
    ques_dict = {}
    VideoFileToQuesID = {}
    transfer_paperNo = {}

    with open(configure_file, 'r') as f:
        content_dict = {line.strip().split('=')[0]: line.strip().split('=')[1]   for line in f.readlines()}
        dbdict['dbIP'] = content_dict['dbIP']
        dbdict['dbname'] = content_dict['dbname']
        dbdict['dbuser'] = content_dict['dbuser']
        dbdict['dbpsd'] = content_dict['dbpsd']
        dbdict['dbport'] = content_dict['dbport']
        processNum = content_dict['processNum']
        run_user = content_dict['run_user']
        lm_other = content_dict['lm_other']

        # content = f.readlines()
        # dbdict['dbIP'] = content[0].strip().split('=')[1]
        # dbdict['dbname'] = content[1].strip().split('=')[1]
        # dbdict['dbuser'] = content[2].strip().split('=')[1]
        # dbdict['dbpsd'] = content[3].strip().split('=')[1]
        # dbdict['dbport'] = content[4].strip().split('=')[1]
        # processNum = content[5].strip().split('=')[1]
        # run_user = content[6].strip().split('=')[1]
        # lm_other = content[7].strip().split('=')[1]

    # Connect to the database
    connection = pymysql.connect(host=dbdict['dbIP'],
                                 user=dbdict['dbuser'],
                                 password=dbdict['dbpsd'],
                                 db=dbdict['dbname'],
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `itemno`, `itemcode`, `itemtype` FROM `AI_itemdict`"
            cursor.execute(sql)
            results = cursor.fetchall()

            sql1 = "SELECT `papercode`, `lm_postfix` FROM `AI_paperdict`"
            cursor.execute(sql1)
            results1 = cursor.fetchall()

            # print(results1)
    finally:
        connection.close()

    # for result in results:
    #     ques_dict[result['itemno']] = result['itemtype']
    #     VideoFileToQuesID[result['itemcode']] = result['itemno']

    # for result in results1:
    #     transfer_paperNo[result['papercode']] = result['lm_postfix']

    ques_dict = {result['itemno']: result['itemtype'] for result in results}
    VideoFileToQuesID = {result['itemcode']: result['itemno'] for result in results}
    transfer_paperNo = {result['papercode']: result['lm_postfix']  for result in results1}
    print(dbdict, ques_dict, transfer_paperNo, VideoFileToQuesID, processNum, lm_other, run_user)

    return dbdict, ques_dict, transfer_paperNo, VideoFileToQuesID, processNum, lm_other, run_user


load_params('./config.txt')

