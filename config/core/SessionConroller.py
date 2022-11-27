from pymongo.collection import ObjectId


import datetime

db = None

def get_auth_user(request):
    try:
        session = request.COOKIES.get('pars_session')
        if session:
            session_user = db.get_database('reviews').get_collection('sessions').find_one(
                {
                    '_id': ObjectId(session),
                    'life':{
                        '$gt':datetime.datetime.utcnow()
                    }
                }
            )
            if session_user:

                return session_user
            else:
                return False
    except Exception as e:
        return False
        # log
