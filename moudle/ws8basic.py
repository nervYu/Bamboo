'''
Powered by Panda Yu
E-mail: yutao@workshop8.cn
'''
import gazu
import os

def loopPrintEXP(colum, keyName, keyId):
    n = 0
    tempdict = {}
    while n <= len(colum)-1:
        tempdict[colum[n][keyName]] = colum[n][keyId]
        n += 1            
    return tempdict

def logIn(userName, passwd, host="kistu.workshop8.cn"):
    gazu.client.set_host("https://"+host+"/api")
    try:
        gazu.log_in(userName+"@workshop8.cn", passwd)
    except:
        return ['Bad UserName or Password Refill Again', 1]
    else:    
        return ['Hello '+gazu.client.get_current_user()["first_name"], 0]


def getProject4User():
    projects = gazu.user.all_open_projects()
    projectsDict = loopPrintEXP(projects, 'name', 'id')
    return projectsDict

def getSeq(project):
    sequence = gazu.user.all_sequences_for_project(project)
    sequenceDict = loopPrintEXP(sequence, 'name', 'id')
    return sequenceDict

def getShot4User(sequence):
    shots = gazu.user.all_shots_for_sequence(sequence)
    shotDict = loopPrintEXP(shots, 'name', 'id')
    return shotDict

def getVer4User(project, shot, kind):
    path = f"d:/project/{project}/shot/{shot}/{kind}/task"
    version = os.listdir(path)
    return version

def getAssets(project, label):
    labelName = label.lower()
    path = f"d:/project/{project}/{labelName}"
    return path

def getTools4User():
    pass

def getUser():
    return gazu.client.get_current_user()

def getTaskDict(colum, ids):
    n = 0
    taskdict = {}
    while n <= len(colum)-1:
        taskType = colum[n] + '_task'
        shotName = ids[0] + "_" + ids[1] + "_" + ids[2]
        taskList = getVer4User(ids[0], shotName, colum[n])
        taskdict[taskType] = taskList
        n += 1            
    return taskdict