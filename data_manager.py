import database_common




@database_common.connection_handler
def get_feedbacks(cursor):
    cursor.execute("""
                    select feedback from feedbacks
                   
                   """)
    data = cursor.fetchall()
    return data



