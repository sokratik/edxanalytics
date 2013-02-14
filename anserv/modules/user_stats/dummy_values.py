from modules.decorators import view, query, event_handler, cron, memoize_query

# Dummy values for queries; useful for off-line development
# Took real queries, then changed all numbers, and reshuffled. 

@query('global', 'total_user_count')
def total_user_count_query():
    return 750000

@query(name = 'course_enrollment')
def total_course_enrollment_query(fs, db, params):
    return {'course_id': (u'BerkeleyX/CS169.1x/2012_Fall',
                          u'BerkeleyX/CS169.1x/2013_Spring',
                          u'BerkeleyX/CS169.2x/2012_Fall',
                          u'BerkeleyX/CS169.2x/2013_Spring',
                          u'BerkeleyX/CS169/fa12',
                          u'BerkeleyX/CS184.1x/2012_Fall',
                          u'BerkeleyX/CS184.1x/2013_Spring',
                          u'BerkeleyX/CS188.1x/2012_Fall',
                          u'BerkeleyX/CS188.1x/2013_Spring',
                          u'BerkeleyX/CS188/fa12',
                          u'BerkeleyX/CS191x/2013_Spring',
                          u'BerkeleyX/Stat2.1x/2013_Spring',
                          u'HarvardX/CB22x/2013_Spring',
                          u'HarvardX/CS50/2012H',
                          u'HarvardX/CS50x/2012',
                          u'HarvardX/ER22x/2013_Spring',
                          u'HarvardX/HLS1x/2013_Spring',
                          u'HarvardX/PH207x/2012_Fall',
                          u'HarvardX/PH278x/2013_Spring',
                          u'MITx/14.73x/2013_Spring',
                          u'MITx/3.091/MIT_2012_Fall',
                          u'MITx/3.091x/2012_Fall',
                          u'MITx/3.091x/2013_Spring',
                          u'MITx/6.00/MIT_2012_Fall',
                          u'MITx/6.002x-EE98/2012_Fall_SJSU',
                          u'MITx/6.002x-NUM/2012_Fall_NUM',
                          u'MITx/6.002x/2012_Fall',
                          u'MITx/6.002x/2013_Spring',
                          u'MITx/6.00short/2013_IAP',
                          u'MITx/6.00x/2012_Fall',
                          u'MITx/6.00x/2013_Spring'),
            'students': (30000L,
                         4897L,
                         60123L,
                         12234L,
                         321L,
                         16431L,
                         1754L,
                         48001L,
                         6123L,
                         8943L,
                         122L,
                         15212L,
                         24551L,
                         7561L,
                         101011L,
                         8L,
                         12311L,
                         212L,
                         7651L,
                         4566L,
                         4532L,
                         155412L,
                         45L,
                         21L,
                         233L,
                         8765L,
                         12L,
                         43112L,
                         179L,
                         34652L,
                         12154L)}

# Note: This query takes a few minutes
@query(name = 'active_students', category = 'global')
@memoize_query(cache_time=15*60)
def active_course_enrollment_query(fs, db, params):
    import time
    time.sleep(15)
    return {'COUNT(DISTINCT student_id)': (121L,
                                           341L,
                                           4532L,
                                           12L,
                                           3221L,
                                           7L,
                                           10212L,
                                           212L,
                                           789L,
                                           7L,
                                           9L,
                                           9111L,
                                           8L,
                                           21L,
                                           8L,
                                           1234L,
                                           4321L),
            'course_id': (u'BerkeleyX/CS169.1x/2012_Fall',
                          u'BerkeleyX/CS169.2x/2012_Fall',
                          u'BerkeleyX/CS169/fa12',
                          u'BerkeleyX/CS184.1x/2012_Fall',
                          u'BerkeleyX/CS188.1x/2012_Fall',
                          u'BerkeleyX/CS188/fa12',
                          u'HarvardX/CS50x/2012',
                          u'HarvardX/PH207x/2012_Fall',
                          u'MITx/14.73x/2013_Spring',
                          u'MITx/3.091x/2012_Fall',
                          u'MITx/6.002x-EE98/2012_Fall_SJSU',
                          u'MITx/6.002x-NUM/2012_Fall_NUM',
                          u'MITx/6.002x/2012_Fall',
                          u'MITx/6.002x/2013_Spring',
                          u'MITx/6.00short/2013_IAP',
                          u'MITx/6.00x/2012_Fall',
                          u'MITx/6.00x/2013_Spring')}