

texts = [
    "We've got to the bottom of the ocean but it's not the end of the journey."
                    " Because the power of the earth machine beneath the seafloor affects the lives of millions of people."
                    " As the seafloor spreads out from the Mid Ocean ridge it eventually collides with the land."
                    " Massive pressure builds up.  Until suddenly it gives. "
                    "This is what happened off the coast of Japan in March, 2011. "
                    "An earthquake beneath the sea floor created the devastating tsunami that hit Japan. "
                    "It was a horribly power reminder that the whole of the pacific region is very "
                    "unstable and earthquakes are frequent.",
    'Where will you stay?',
    'Is this your first time to come to England?',
    'Where have you ever lived?',
    'She comes here to attend a conference.',
    'She can stay here for fourteen days at most.',
    "It's located in the center of the capital.",
    'Seven years.',
    'In the United States.',
    '''John Smith was an old porter. He worked at the station. Every day he was busy carrying heavy things for people. He was careful with his work. He was kind to everyone. He was always ready to help others.One morning he stood in the station. He was waiting for the train. Just then he saw a man running towards the trains with a big bag in his hand."No train is starting. Why is he in such a hurry?" John said to himself.He went up to the man and asked, "May I help you?"As soon as the man saw John, he stopped running. "Can I catch the 10:35 train to London?" the man asked. He looked worried.John looked at him for a few seconds and said, "Well, sir. I'd like to help you, but I can't answer your question because I don't know how fast you can run." Then he explained to the man, "The 10:35 train to London left five minutes ago. Can you run fast enough to catch it?"John Smith was an old porter who worked in a station. He is kind and always ready to help others. One day when he was waiting for the train at the station, he saw a man running hurriedly. He came to him and asked whether he needed any help. The man asked whether he could catch the 10:35 train to London. John told the man in a humorous way that the train had just left five minutes ago and it would be possible if he could run fast enough to catch the train.'''
]

item_types = ['Read', 'QA', 'QA', 'QA', 'QA', 'QA', 'QA', 'QA', 'QA', 'Retell']
examID = 20171013
paths = [
    './QT-742440ans.mp3',
    './QT-325748ans.mp3',
    './QT-665ans.mp3',
    './QT-330053ans.mp3',
    './QT-774991ans.mp3',
    './QT-342100ans.mp3',
    './QT-493379ans.mp3',
    './QT-382820ans.mp3',
    './QT-741155ans.mp3',
    './QT-713336ans.mp3'
]

arg0 = {
    'interface': '/voice/eval/',
    'text': texts[0],
    'type': item_types[0],
    'examUniqueID': examID,
    'path': paths[0]
}

arg1 = {
    'interface': '/voice/eval/',
    'text': texts[1],
    'type': item_types[1],
    'examUniqueID': examID,
    'path': paths[1]
}
arg2 = {
    'interface': '/voice/eval/',
    'text': texts[2],
    'type': item_types[2],
    'examUniqueID': examID,
    'path': paths[2]
}
arg3 = {
    'interface': '/voice/eval/',
    'text': texts[3],
    'type': item_types[3],
    'examUniqueID': examID,
    'path': paths[3]
}
arg4 = {
    'interface': '/voice/eval/',
    'text': texts[4],
    'type': item_types[4],
    'examUniqueID': examID,
    'path': paths[4]
}
arg5 = {
    'interface': '/voice/eval/',
    'text': texts[5],
    'type': item_types[5],
    'examUniqueID': examID,
    'path': paths[5]
}
arg6 = {
    'interface': '/voice/eval/',
    'text': texts[6],
    'type': item_types[6],
    'examUniqueID': examID,
    'path': paths[6]
}
arg7 = {
    'interface': '/voice/eval/',
    'text': texts[7],
    'type': item_types[7],
    'examUniqueID': examID,
    'path': paths[7]
}
arg8 = {
    'interface': '/voice/eval/',
    'text': texts[8],
    'type': item_types[8],
    'examUniqueID': examID,
    'path': paths[8]
}
arg9 = {
    'interface': '/voice/eval/',
    'text': texts[9],
    'type': item_types[9],
    'examUniqueID': examID,
    'path': paths[9]
}

args = [arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9]


