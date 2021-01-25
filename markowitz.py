#!/usr/bin/env python

import traceback2 as traceback
import matplotlib
matplotlib.use('Agg')
import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import dx
import seaborn as sns
import settings as st
import meanvarianceportfolio as mvp
from threading import Thread
import uuid

sns.set()

taskDict = {}

ZERO = dt.timedelta(0)
HOUR = dt.timedelta(hours=1)

# A UTC class.
class UTC(dt.tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


utc = UTC()


def main():
    print('run via webapp.py')


def findSource(source):
    if 'upload_type' in st.config["common"]:
        uploadType = st.config["common"]["upload_type"]
    else:
        uploadType = ''

    if source == 'upload' and uploadType != 'allcolumns':
        retVal = 'upload'
    elif source == 'upload' and uploadType == 'allcolumns':
        retVal = 'upload1'
    else:
        retVal = source

    print(f'upload_type = "{uploadType}, source="{source}"')
    return retVal


def sharpeAndCml(source, riskFree, symbols):
    ma = dx.market_environment('ma', dt.date(2010, 1, 1))
    ma.add_list('symbols', symbols)
    ma.add_constant('source', findSource(source))
    # ma.add_constant('final date', dt.date(2014, 3, 1))
    ma.add_constant('final date', dt.datetime.now())

    retVal = '{\n'
    retVal += '"EfficientPortfolios":'
    try:
        port = mvp.MeanVariancePortfolio(source + '_stocks', ma)
        effFrontier = port.get_efficient_frontier_bl(st.config["efficient_frontier"]["points_number"])

        retVal += effFrontier.toJson()
        retVal += ',\n'

        try:
            cpl = port.get_capital_market_line_bl_1(effFrontier.vols, effFrontier.rets, riskless_asset=riskFree)
            retVal += '"CML":' + cpl.toJson()
        except Exception as e:
            retVal += '"CML": {{"error":"{}"}}'.format(str(e).replace('"', '\''))
            traceback.print_exc()

    except Exception as e:
        retVal += '{{"error":"{}"}}'.format(str(e).replace('"', '\''))
        traceback.print_exc()

    retVal += "\n}"

    print(retVal)
    return retVal


def sharpeAndCmlAsync(sourceName, riskFree, placeHolderOnly):
    uid = uuid.uuid4()
    t = Thread(target=threadFunc, args=(sourceName, riskFree, uid))
    t.start()
    return '{{"response":{{"uid":"{}","success":true}}}}'.format(str(uid))


def threadFunc(sourceName, riskFree, uid):
    taskDict[uid] = (False, '') #not completed yet but started
    jsonStr = sharpeAndCml(sourceName, riskFree, [])
    taskDict[uid] = (True, jsonStr) #completed and result is there


def getAsyncTaskStatus(uid):
    task = taskDict.get(uuid.UUID(uid), None)
    return '{{"response":{{"taskexists":{}, "taskcompleted":{}}}}}'.\
        format(str(task is not None).lower(), str(task[0]).lower())


def getAsyncTaskResult(uid):
    task = taskDict.get(uuid.UUID(uid), None)
    if task is None:
        return '{"response":{"taskexists":false, "taskcompleted":false}}'
    else:
        if task[0]:
            taskDict.pop(uuid.UUID(uid))
            return task[1]
        else:
            return '{"response":{"taskexists":true, "taskcompleted":false}}'


def getListAsyncTasks():
    uidsList = list(taskDict.keys())
    csvList = ",".join(map(str, uidsList))
    return '{{"response":{{"tasklist":"{}"}}}}'.format(csvList)



if __name__ == "__main__":
    main()
